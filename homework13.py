class webStore(object):
    addresses_list = list()

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, address):
        self.address = address
        self.list_ex = webStore.addresses_list.append(address)
     
    @staticmethod
    def count_addresses():
        return len(set(webStore.addresses_list))
    
    @staticmethod
    def count_times(address_):
        return webStore.addresses_list.count(address_)
    
    @staticmethod
    def top_addresses():
        count_ = 0
        element = webStore.addresses_list[0]
        
        for i in webStore.addresses_list:
            most_used_address = webStore.addresses_list.count(i)

            if(most_used_address > count_):
                count_ = most_used_address
                element = i
    
        return element


a = webStore('a')
b = webStore('a')
c = webStore('b')
d = webStore('c')



print(webStore.count_addresses())
print(webStore.count_times('a'))
print(webStore.top_addresses())