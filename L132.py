#Rosemary, Krista, and Saerin
my_file=open("ourfile.txt","w")
line7="#hello\n"
my_file.write(line7)
line8="#how are you?\n"
my_file.write(line8)
line9="#I hope you are well\n"
my_file.write(line9)
line10="#It is a nice day outside\n"
my_file.write(line10)
line11="#I hope you are enjoying the weather today\n"
my_file.write(line11)
line12="#goodbye\n"
my_file.write(line12)

my_file.close()
# def list_hashtags(y):
#     list=[]
#     for line in y:
#         if len(line)=="#":

my_file1=open("ourfile.txt","r")
import re

def get_hashtag_ranking(input_sentence):
    hashtag_list = re.findall(r"#\w+", input_sentence)
    hashtag_count = {}
    for hashtag in hashtag_list:
        if hashtag in hashtag_count:
            hashtag_count[hashtag] += 1
        else:
            hashtag_count[hashtag] = 1
    def get_frequency(hashtag_count_pair):
        return hashtag_count_pair[1]

    sorted_hashtags = sorted(hashtag_count.items(), key=get_frequency, reverse=True)

    output_list = [hashtag for (hashtag, count) in sorted_hashtags]

    return output_list

for line in my_file1:
    print(get_hashtag_ranking(line))
