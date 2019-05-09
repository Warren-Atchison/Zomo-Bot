if __name__ == "__main__":
    main()

if __name__ == "__help__":
    help()


def main():
    #Splitting the message content into parts
    order = message.content.split()

    if order[0] == "%god":

        if len(order) > 1:
            #If the user is dictating what classes to include
            if order[1][0] == "+":
                order[1] = order[1].upper()
                for i in order[1][1::]:
                    if i=="G": roles.append("Guardians")
                    elif i=="W": roles.append("Warriors")
                    elif i=="A": roles.append("Assassins")
                    elif i=="H": roles.append("Hunters")
                    elif i=="M": roles.append("Mages")
                    else:
                        await message.channel.send("Invalid class selection.")
                        return
                #Removing this portion of the order, as it has been done
                del order[1]

            elif order[1][0] == "-":
                roles = ["Guardians", "Warriors", "Assassins", "Hunters", "Mages"]
                order[1] = order[1].upper()
                for i in order[1][1::]:
                    if i=="G": roles.remove("Guardians")
                    elif i=="W": roles.remove("Warriors")
                    elif i=="A": roles.remove("Assassins")
                    elif i=="H": roles.remove("Hunters")
                    elif i=="M": roles.remove("Mages")
                    else:
                        await message.channel.send("Invalid class deselection.")
                        return
                #Removing this portion of the order, as it has been done.
                del order[1]

            else:
                roles = ["Guardians", "Warriors", "Assassins", "Hunters", "Mages"]
        else:
            roles = ["Guardians", "Warriors", "Assassins", "Hunters", "Mages"]
        
        # Creating the list of gods having been restricted
        gods = []
        for i in roles:
            if i == "Guardians":
                for god in guardians:
                    gods.append(god)
                    
            if i == "Warriors":
                for god in warriors:
                    gods.append(god)
            
            if i == "Assassins":
                for god in assassins:
                    gods.append(god)
                
            if i == "Hunters":
                for god in hunters:
                    gods.append(god)
            
            if i == "Mages":
                for god in mages:
                    gods.append(god)

        #If there are additional arguments after roles
        if len(order) > 1:
            gods_by_pan = []

            #Removing %god for ease
            del order[0]

            #Putting the user's command in lowercase because users are dumb
            for i in range(len(order)):
                order[i] = order[i].lower()

            #Iterating through the user's command
            for i in order:
                #Iterating through the pantheon dictionary
                for j in pandict:
                    #Iterating through the list associated with each key
                    for k in pandict[j][0]:
                        #If one of the elems in the list was given by the user
                        if i == k:
                            #Add the KEY to the pantheons list
                            pantheons.append(j)
        
            pantheons = sorted(pantheons)
            #Removing any gods that are not in the proper pantheon
            #Iterating through the pantheons
            for i in pantheons:
                #Iterating through the gods in the pantheon
                for god in pandict[i][1]:
                    #Adding the god to new god list
                    gods_by_pan.append(god)


            #Editing the god list to be the intersection of the two lists
            gods = intersection(gods, gods_by_pan)

        if len(gods) == 0:
            await message.channel.send("No gods match those criteria!")
        else:
            selection = gods[secrets.randbelow(len(gods))]
            await message.channel.send(selection)

def help();
     await message.channel.send("To use me, call %god. Optional arguments are:\n\
\t1) +<args>. This will specify which classes you would like to include.\n\
\t2) -<args>. This will specify which classes you would like to exclude.\n\
\t3) <pantheon name>. This will specify which pantheons you would like to include.\n\
Please do NOT combine arguments 1 and 2.")
