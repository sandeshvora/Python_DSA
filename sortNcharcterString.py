def sort_by_last_letter(strings):
    def last_letter(s):
        return s[2]
    return sorted(strings,key=last_letter)

print(sort_by_last_letter(["hello","from","last","letter","abcd"]))