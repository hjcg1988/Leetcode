pal=''
        for i in s:
            if i.isalnum() :
                pal += i.lower()
        return pal == pal[::-1]
