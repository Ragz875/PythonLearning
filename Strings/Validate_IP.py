import string
class Solution:
    def validIPAddress(self, IP: str) :

        if IP.count('.') == 3:
            return self.validIPAddressIPv4(IP)
        elif IP.count(':') == 7:
            return self.validIPAddressIPv6(IP)
        else:
            return 'Neither'

    def validIPAddressIPv4(self, IP: str) -> str:
        nums = IP.split('.')
        print(nums)
        for ele in nums:
            print(ele)
            if len(ele) == 0 or len(ele) > 3:
                return 'Neither'
            if (ele[0]=='0' and len(ele) > 1) or (ele.isnumeric() and int(ele) > 255) or not ele.isdigit():
                print(ele[0])
                return 'Neither'
        return 'IPv4'

    def validIPAddressIPv6(self, IP: str) -> str:
        nums = IP.split(':')
        for ele in nums:
            if (len(ele) > 4) or (len(ele) == 0) :
                print('came first if ')
                return 'Neither'
            if all([c in string.hexdigits for c in ele]) == False :
                print('came second if ')
                return 'Neither'
        return 'IPv6'

    def fact(self,n):
        fact=1
        while n >= 1:
            fact*=n
            n=n-1
        return fact
s=Solution()
ip=['20EE:FGb8:85a3:0:0:8A2E:0370:7334',
    '2001:0db8:85a3:0:0:8A2E:0370:7334',
    '01.01.01.01',
    '20EE:FGb8:85a3:0:0:8A2E:0370:7334']

for ip1 in ip:
    print(f'IP address given : {ip1} , validation : ', s.validIPAddress(ip1))
for i in range(10):
    print(f'Factorinal of : {i} is',s.fact(i))