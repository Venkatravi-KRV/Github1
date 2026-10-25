


source_name = input("Enter the source name:")
recieved =  int(input("Enter number of recieved record:"))
rejected =  int(input("Enter number of rejected record:"))


successfully_loaded = recieved-rejected


print("\n---- Task 3 record validation------")
print("source:",source_name)
print("received:",recieved)
print("rejected:",rejected)
print("successfully loaded:", successfully_loaded)


