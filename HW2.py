def main():
    #print(roubles(input('Enter roubles: ')))
    #print(coins(input('Enter coins: ')))
    #print(numM(input('Enter number: ')))
    #print(numF(input('Enter number: ')))
    sum(input('Enter sum: '))

def roubles(rubs):
    rubs = str(rubs)    # If input value is not string
    if (int(rubs) < 5 or int(rubs) > 15):   
        if rubs[len(rubs)-1] == '1':
            return 'рубль'
        elif rubs[len(rubs)-1] in ('2', '3', '4'):
            return 'рубля'
    return 'рублей'

def coins(coins):
    coins = str(coins)     # If input value is not string
    if (int(coins) < 5 or int(coins) > 15):
        if coins[len(coins)-1] == '1':
            return 'копейка'
        elif coins[len(coins)-1] in ('2', '3', '4'):
            return 'копейки'
    return 'копеек'

def numM(num):
    num = str(num)     # If input value is not string
    num_str = ''
    
    # Dictionaries for getting a word of units, tens and hundreds according to their values
    
    units = {'1':'один', '2':'два', '3':'три', '4':'четыре', '5':'пять', '6':'шесть', '7':'семь', '8':'восемь', '9':'девять', '0':''}
    tens = {'2':'двадцать', '3':'тридцать', '4':'сорок', '5':'пятьдесят', '6':'шестьдесят', '7':'семьдесят', '8':'восемьдесят', '9':'девяносто', '0':''}
    second_tens = {'1':'одиннадцать', '2':'двенадцать', '3':'тринадцать', '4':'четырнадцать', '5':'пятнадцать', '6':'шестнадцать', '7':'семнадцать', '8':'восемнадцать', '9':'девятнадцать', '0':'десять'}
    hundreds = {'1':'сто', '2':'двести', '3':'триста', '4':'четыреста', '5':'пятьсот', '6':'шестьсот', '7':'семьсот', '8':'восемьсот', '9':'девятьсот', '0':''}
    if len(num) == 3:
        if num[1] == '1':  
            num_str += hundreds[num[0]] + ' ' + second_tens[num[2]]
        else:
            num_str += hundreds[num[0]] + ' ' + tens[num[1]] + ' ' + units[num[2]]
        if num[1] == '0':
            num_str = num_str.replace(' ', '', 1)
    elif len(num) == 2:
        if num[0] == '1':
            num_str += second_tens[num[1]]    
        else:
            if num[1] == '0':
                num_str += tens[num[0]]
            else:
                num_str += tens[num[0]] + ' ' + units[num[1]]
    elif len(num) == 1:
        if num == '0':
            num_str += 'ноль'
        num_str += units[num]
    return num_str
    
def numF(num):
    num = str(num)
    num_str = ''

    # Dictionaries for getting a word of units, tens and hundreds according to their values
    
    units = {'1':'одна', '2':'две', '3':'три', '4':'четыре', '5':'пять', '6':'шесть', '7':'семь', '8':'восемь', '9':'девять', '0':''}
    tens = {'2':'двадцать', '3':'тридцать', '4':'сорок', '5':'пятьдесят', '6':'шестьдесят', '7':'семьдесят', '8':'восемьдесят', '9':'девяносто', '0':''}
    second_tens = {'1':'одиннадцать', '2':'двенадцать', '3':'тринадцать', '4':'четырнадцать', '5':'пятнадцать', '6':'шестнадцать', '7':'семнадцать', '8':'восемнадцать', '9':'девятнадцать', '0':'десять'}
    hundreds = {'1':'сто', '2':'двести', '3':'триста', '4':'четыреста', '5':'пятьсот', '6':'шестьсот', '7':'семьсот', '8':'восемьсот', '9':'девятьсот', '0':''}
    if len(num) == 3:
        if num[1] == '1':
            num_str += hundreds[num[0]] + ' ' + second_tens[num[2]]
        else:
            num_str += hundreds[num[0]] + ' ' + tens[num[1]] + ' ' + units[num[2]]
        if num[1] == '0':
            num_str = num_str.replace(' ', '', 1)
    elif len(num) == 2:
        if num[0] == '1':
            num_str += second_tens[num[1]]    
        else:
            if num[1] == '0':
                num_str += tens[num[0]]
            else:
                num_str += tens[num[0]] + ' ' + units[num[1]]
    elif len(num) == 1:
        if num == '0':
            num_str += 'ноль'
        num_str += units[num]
    return num_str
    
def sum(sum_):
    sum_ = str(sum_).replace('.', ',')    # If input value is float
    rubs_ = sum_.split(',')[0] if ',' in sum_ else sum_     #Separete roubles from coins if value is float
    coins_ = sum_.split(',')[1] if ',' in sum_ else '0'     #Separete coins from roubles if value is float
    print("Your sum:", numM(rubs_), roubles(rubs_), numF(coins_), coins(coins_))

if __name__ == "__main__":
    main()