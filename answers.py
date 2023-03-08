import logging
import asyncio
import requests
logging.basicConfig(level=logging.INFO)


# 1. Anagram
def make_hash(s):
    s = s.lower()
    h = {}
    for letter in s:
        if letter in h:
            h[letter] += 1
        else:
            h[letter] = 1
    return h

def is_anagram(s1, s2):
    s1_hash = make_hash(s1)
    s2_hash = make_hash(s2)
    if s1_hash == s2_hash:
        return True
    return False

# 2. Even integers
def sum_evens(nums):
    return sum([num for num in nums if num % 2 == 0])

# 3. Maximum contiguous subarray
def max_cont_subarray(array):
    p = 0
    curr_max_sum = total_max_sum = array[p]
    p += 1
    while p < len(array):
        if curr_max_sum + array[p] > array[p]:
            curr_max_sum = curr_max_sum + array[p]
        else:
            curr_max_sum = array[p]
        if curr_max_sum > total_max_sum:
            total_max_sum = curr_max_sum
        p += 1
    return total_max_sum
            
#4. MAC addresses
class DeviceStatusChecker:

    def __init__(self, mac_addresses_file, base_url, use_status_fn=None):
        self.mac_addresses_file = mac_addresses_file
        self.base_url = base_url
        self.use_status_fn = use_status_fn

    def iter_addresses(self):
        # handle reading addresses from file
        if type(self.mac_addresses_file) is str:
            for line in open(self.mac_addresses_file_path, "r"):
                yield line.replace("\n", "")
        # handle reading addresses from previously opened byte stream
        else:
            for line in self.mac_addresses_file:
                yield line.replace("\n", "")

    def get_device_status(self, mac_address, *args, **kwargs):
        resp = requests.get(f"{self.base_url}/device/check/{mac_address}")
        if resp.status_code == 200:
            return resp.text if not self.useStatusFn else self.useStatusFn(resp.text, *args, **kwargs)
        else:
            logging.info(f"Unable to check status of device with mac address {mac_address}")
            return None

    async def process_mac_addresses(self):
        results = await asyncio.gather(*(self.get_device_status(mac_address) for mac_address in self.iter_addresses(self.mac_addresses_file)))
        return results

    
if __name__ == "__main__":
    print(is_anagram("Silent", "Listen"))
    print(is_anagram("Restful", "Fluster"))
    print(is_anagram("iceman", "cinema"))
    print(is_anagram("state", "taste"))
    print(is_anagram("bored", "robed"))

    print(sum_evens([i for i in range(11)]))

    print(max_cont_subarray([1, -2, 3, 4, -5, 8]))
    print(max_cont_subarray([-1, -2, -3, -4]))
    print(max_cont_subarray([5, -1, -2, 10, -7]))
