import random
import json
import os

class HitCounter:
    """Records hits."""
    def __init__(self, limit=100):
        """Create a HitCounter with default "limit" log items in memory."""
        self.totalcount = 0
        self.timestamps = []
        self.limit = limit

    @property
    def total(self):
        """Get total hits."""
        return self.totalcount

    def record(self, timestamp):
        """Record a timestamp."""
        self.totalcount += 1
        self.timestamps.append(timestamp)
        # Dump to persistent storage if limit is reached
        if len(self.timestamps) % self.limit == 0:
            self.dump()

    def range(self, lower, upper):
        """Get inclusive number of hits that occured between two timestamps."""
        count = 0

        # get records from persistent store
        f = self.get_file_index()

        for file in f:
            fstart, fend = file[0], file[1]
            filename = f"{fstart}-{fend}.delme"

            # reject out of range files
            if lower > int(fend) or upper < int(fstart):
                continue

            # files that fully encapsulate our range
            elif (lower <= int(fstart)) and (upper >= int(fend)):
                print(f"file {filename} has {self.limit} hits in range.")
                count += 100
                continue

            # add relevant hits for files partially in range
            elif (lower <= int(fstart)) or (upper >= int(fend)):

                with open(filename) as fh:
                    filehits = 0
                    data = json.loads(fh.read())

                    for potential in data:
                        if lower <= int(potential) <= upper:

                            filehits += 1

                print(f"file {filename} has {filehits} hits in range.")
                count += filehits

        # count hits in memory
        memhits = len([x for x in self.timestamps if lower <= x <= upper])
        print(f"Hits in memory: {memhits}")
        count += memhits
        return count


    @staticmethod
    def get_file_index():
        # build index from files on disk
        files = (f[:-6] for f in os.listdir() if f.endswith(".delme"))
        return sorted(tuple(f.split("-")) for f in files)


    def dump(self):
        """Dump "limit" timestamps to disk, clear internal log."""
        limit = self.limit
        data = json.dumps(self.timestamps[:limit])
        earliest, latest = self.timestamps[0], self.timestamps[limit - 1]
        self.timestamps = self.timestamps[limit:]
        filename = f"{earliest:06}-{latest:06}.delme"

        with open(filename, "w") as outfile:
            outfile.write(data)


def setup(starttime=1, interval=20, num_hits=620):
    """Log some hits."""

    hc = HitCounter()
    timestamp = 1

    # log num_hits random but ascending hits, this may write a few files
    # to current directory with extension ".delme"
    while hc.total < num_hits:
        timestamp += random.randint(1,interval)
        hc.record(timestamp)

    return hc


def main(hc, a, b):
    # Get number of hits between a and b
    print(f"searching for hits between {a} and {b}:")
    hits = hc.range(a, b)
    print(f"{hits} hits in range ({hc.total} total hits)\n")


def teardown():
    """Clean up log files."""
    for x in os.listdir():
        if x.endswith(".delme"):
            os.unlink(x)


hc = setup()
main(hc, 2020, 4040)
main(hc, 5200, 6500)
teardown()
