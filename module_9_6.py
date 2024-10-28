def all_variants(text):
    i_ = 1
    start_ = 0
    end_ = 1

    text = str(text)

    while i_ <= len(text):
        while end_ <= len(text):
            yield text[start_:end_]
            start_ += 1
            end_ += 1

        i_ += 1
        start_ = 0
        end_ = i_

# Ещё один вариант, но последовательности будут упорядочены не так как в задании
# def all_variants(text):
#     for i_ in range(len(text)):
#         for j_ in range(i_ + 1, len(text) + 1):
#             yield text[i_ : j_]


a = all_variants("abcdefghijklmno")
for i in a:
    print(i)