def mutualFriends(set1, set2):
    result = list(set1.intersection(set2))
    result.sort()
    return result

def ourFriends(set1, set2):
    result = list(set1.union(set2))
    result.sort()
    return result

def theirFriends(set1, set2):
    result = list(set2.difference(set1))
    result.sort()
    return result

if __name__ == "__main__":
    myfriendinput = input("Enter your friends on your friend list:")
    myFriendsList = myfriendinput.split()
    yourfriendinput = input("Enter the friends on your friend's friend list:")
    yourFriendsList = yourfriendinput.split()
    myFriends = set(myFriendsList)
    yourFriends = set(yourFriendsList)
    print("Your mutual friends are:", mutualFriends(myFriends, yourFriends))
    print("All of your friends combined are:", ourFriends(myFriends, yourFriends))
    print("Their friends are:", theirFriends(myFriends, yourFriends))