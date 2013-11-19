def main():
    longest = 0
    max_chain_length = 0

    for i in range(1, 1000000):
        current_num = i
        chain_length = 1

        while current_num != 1:
            chain_length += 1

            if(chain_length > max_chain_length):
                max_chain_length = chain_length
                longest = i

            if current_num % 2 == 0:
                current_num = current_num / 2
            else:
                current_num = 3 * current_num + 1

    print("longest:", longest, "max_chain_length:", max_chain_length)

if __name__ == "__main__":
    main()
