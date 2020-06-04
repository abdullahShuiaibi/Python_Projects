def main():
    def add_video(arg1):
        video_list = []
        print("Enter the running times for each video.")
        for i in range(arg1):
            print("Video #",i+1,": ",end="")
            num = float(input(""))
            video_list.append(str(num))
            video.write(video_list[i]+"\n")
        

    video = open("video_times.txt","w")
    print("How many videos are in the project? ",end="")
    num = int(input(""))
    add_video(num)
    print("The times have been saved to video_times.txt. ")
    video.close()
main()