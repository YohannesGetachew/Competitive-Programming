def sockMerchant(n, ar):
    if(n >= 1 and n <= 100):
        number_of_pairs = 0
        temp_pair_holder = []
        for i in range(0, n):
            if(ar[i] >= 1 and ar[i] <= 100):
                does_other_pair_exist = ar[i] in temp_pair_holder
                if(does_other_pair_exist):
                    number_of_pairs += 1
                    temp_pair_holder.remove(ar[i])
                else:
                    temp_pair_holder.append(ar[i])
        return number_of_pairs


number_of_shock = 8
socks = [2, 3, 5, 2, 4, 9, 2, 4]
print(sockMerchant(number_of_shock, socks), "Sock pair found")
