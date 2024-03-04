
For this GCC CTF 2024, I have done many work, even though not that much of work has concluded.
It has been my first CTF, and I thanks my mates for being so patient with me and my noobie questions.
I'll describe it here, trying to be concise and precise too.
I've tried : Pwn, Web3, Web, Forensic, Reverse, Osint, Crypto
And successed : Web3, Forensic, Osint, Crypto

Here are my explainations to the code :

Pwn - Flag Roulette 
# ----------------------------------------------------- #

I've been able to decompile the Assembly code with Ghidra.
I've found that it wanted the chars to be 'G', 'C', 'C'.
But, it seemed the chars were random. So, why not try to bruteforce ?
And I tried it. After more than 3000 tries (computated), no results.
But the bruteforce was too late, I've not been able to come to a better solution,
I tried it and lost.

# ----------------------------------------------------- #

Web3 - Synthatsu katana thief 
# ----------------------------------------------------- #

We have used the remix.ether tool to start contracts.
We then connected the contract to the given address, from whom we started the other contract.
There, we have been able to become beyond, then transfer ourself the crypto.

# ----------------------------------------------------- #

Web3 - TOOTB
# ----------------------------------------------------- #

We have used the remix.ether tool to start contracts.
We then set up the contracts, the contract.sol with the given address,
Then some other contract with the address of the target. This contract contained
Some functions and ressources to create cubes.
We then started the attack contract, and linked it.
Deployed it, and tried to start the attack. The issue ?
We have not been able to end the chall after that, and find a solution.

Why ?
The contract was always blocked for any reason. Sometimes not enough ressources,
Sometimes for gas fees issues, and no idea why the issue was here this way.
On the other hand, I tried using a try/catch statement to avoid having crashes.
At this moment : Contracts were going with absolutely NO problem,
But no withdraw was possible. We have not been able to get the ownership of contracts to
Get the withdraw possible.
The functions were taking the crypto from the Wallet, storing it, and giving it back to me.

# ----------------------------------------------------- #

Web - Frenzy Flask
# ----------------------------------------------------- #

I failed on this one too, tbh. (No spoil)
I tried exploring the deployed website, the code,
And found nothing at this time.
After some time (today, writing this) I found out that the website was in DEBUG
So I could have tried the DEBUG exploit on Flask to hack it.

# ----------------------------------------------------- #

Forensic - BipBipBiiip
# ----------------------------------------------------- #

This one is my proudest, I've done it alone, fast, and kinda easily.

How ? Kinda simple : reading the csv file,
I tried using some char exclusion.
Python, with open, if "" in datas[index] and it's done.
Tbh, it was trying 2 things : If it had less than 10 numbers in the phone number, and
If it had a char out of the "0123456789-+ ()." (list that have been affined with 3 or 4 tries)
When I found out the results were somewhat encoded. First try, found the solution. It seemed hexadecimal, and was hex.
So in the loop, added to the flag the conversion from hex of the sus numbers, and the flag was there.

# ----------------------------------------------------- #

Reverse - Array Programming Rocks
# ----------------------------------------------------- #

I failed this one, tried some things but did not last too long on this one.
I tried understanding the file and lost.
Tried to split every numbers of lines with the underscore, then convert it from ASCII or Binary
Failed. No solution found from me.

# ----------------------------------------------------- #

OSINT - But they so tasty

# ----------------------------------------------------- #

I came when my team found out the Strava account.
I looked up when I found some suspicious path into a weird corner of the city,
I checked on Google Maps and seen it was a Carrefour market, so I checked up their website,
And found the exact good product in the website, with the nutritional values for 100g of it.
Then, we just did the calculus to get the value for the portion, and we got the flag.

# ----------------------------------------------------- #

Crypto - GCC News
# ----------------------------------------------------- #

I did not score the flag, but I have been able to do it.
How did I find the flag ? Pretty simple : 
I found out in the source code that the post request contained a token, and a 'message'.
What did contain the token ? Username and key.
I got that, fine. GCC account exists and is there, fine too.
Just get this part, but let's just make it too.
So I took the functions from the source code, and scrapped it, editing it to remove the Flask part,
And made it a little more "adaptable" to my task.
Just used and reversed the generate hash, key, login, and signature generation.
But what's the signature ? It's the whole token part.
For the second part, the message, it contained username and authorization encrypted in b64.
So, I had to modify the post request to say I'm allowed. Unhashing the request,
It made me realize the encryption was [Name : True/False]. Then, as simple it appears,
I made my code to encrypt the same way my [GCC : True] instead of False (as it was actually the case).
I struggled a bit with the "message" part, but was able to do it, and got the flag.

# ----------------------------------------------------- #

Special mentions to Too Many Leaks, Baby Bof, that I downloaded and tried to resolve, but could not come to any solution, too much algorithm for my tired brain at this time.

But also, obviously, speical thanks to everyone that made those challs, 
I know my write-up isn't that glorious, and maybe doesn't bring the challs to the light, but I tried, and I'm glad I could try.