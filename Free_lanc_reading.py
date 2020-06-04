


def main():
    video_len = open("video_times.txt","r")
    total = 0
    for i in range(1,7):
        num = float(video_len.readline())
        print("Video #",i,end=": ", sep="")
        print(num)
        total = num + total
    print("The total running time is ",total," seconds")   
   

main()