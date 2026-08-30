class Solution(object):
    def readBinaryWatch(self, turnedOn):

        result = []

        for hour in range(12):

            for minute in range(60):

                # Count ON LEDs
                if hour.bit_count() + minute.bit_count() == turnedOn:

                    result.append(
                        str(hour) + ":" + str(minute).zfill(2)
                    )

        return result