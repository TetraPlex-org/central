# Authentication

## Account Creation
As outlined in **voting**, all sensitive data is stored and handled separately through LegalEntity. The Account on the other hand represents the login of a user, with no sensitive data attached to it. A **User** is a person who has an Account or wants to interact with the system in some way.
At first, all Accounts are anonymous, with no sensitive data attached to them. The user can choose to attach sensitive data in order to gain access to more features, but this is not required. The main purposes of attaching sensitive data is to gain access to the voting system (as only identified users can vote), being able to regain access to the account in case of having lost access to the account as well as being able to use parts of the system that require credits or financial data.

So, how to get an Account?



```mermaid
  journey
    title Getting an Account
    section Registering
      Ask friend for an invite: 3: User
      Get invitation link: 3: User
      Follow link: 3: User
      Safe key in Chrome as password: 3: User
```

## Invitation Link
The invitation link is generated and saved by the user who wants to invite another user. The link contains a unique identifier, which is used to identify the user who invited the new user. The link is sent to the new user, who can then follow the link to register an account. By default the link can only be used once, but

```mermaid
---
title: Account Creation
---
%%{init: {"flowchart": {"htmlLabels": false}} }%%
flowchart TB
  TRIGGER(["User wants to have an account"])-->S1
  S1["User asks someone who has an account to get invited"]-->S2
  S2["User gets invitation link"]-->S3
  S3["User follows invitation link"]-->S4
  S4["User Client and System exchange public keys"]-->S5
  S5["System creates account without asking for any personal information"]-->S6 & S6a1
  S6a1[/"System sends User an encrypted honeypot token"/]
  S6["System sends User an encrypted jwt for login"]-->S7
  S7["User Client decrypts jwt and stores the token in a password manager"]-->S8
  S8["User Client logs in using the jwt"]-->S9
  S9(["User is happy"])

```

```mermaid
---
title: Honeypot Token
---
%%{init: {"flowchart": {"htmlLabels": false}} }%%
flowchart TB
  TRIGGER(["System sends User an encrypted honeypot token, indistinguishable to a real access key"])-->S1
  S1["User Client decrypts the token and stores it in plaintext on disk"]-->S1a1
  S1a1["Intruder steals the token"]-->S2
  S2["Intruder tries to use plaintext jwt to login"]-->S3
  S3[System detects the use of the honeypot token and lets the connection time out with no error.]-->S4 & S5
  S4[/Intruder is confused/]
  S5[System logs the intrusion attempt and alerts the User] --> SUCCESS
  SUCCESS([User is happy to get a chance to actively counter the attack])

```

## Login

### The user logs into the system

The Key is an encrypted jwt token. The user can choose to store the key in the browser, or to store it in a password manager.

```mermaid
---
title: Login
---
%%{init: {"flowchart": {"htmlLabels": false}} }%%
flowchart TB
   TRIGGER(["`User asks the system to log them in`"])-->S1
  S1["`The system renders the login screen and asks the user to provide Key`"]-->S2

```

---

The system renders the login screen and asks the user to provide their credentials
The user provides its credentials (email and password) and asks the system to log them in
The system asks the backend API to verify users’ credentials
The backend API confirms that the provided credentials are valid
The backend API confirms that the user has an active subscription
The backend API provides the system with an authentication token for the user
The system logs the user in
The main success scenario ends.

Extension 2a: The user authenticates via 3rd party system (Google, Facebook)
---
2a1. The user asks the system to authenticate it via 3rd party authentication system (Google or Facebook)

2a2. The system redirects the user to the appropriate 3rd party authentication system

2a3. The user successfully authenticates using 3rd party authentication system and the 3rd party authentication system provides the system with the user’s identification information

2a4. The system asks the backend API to confirm that the user has a valid account and a valid subscription

2a5. The backend API confirms that the user indeed has a valid account and a subscription

2a6. The backend system provides the system with the appropriate authentication token

2a7. The main success scenario resumes from step 7

Extension 2a4a: The user does not have a valid account
---

2a4a1. The backend system determines that the user does not have a valid account and informs the System of that fact

2a4a2. The system informs the user that their credentials are not valid

2a4a3. The main success scenario restarts from step 1

Extension 2a4b: The user does not have a valid subscription
---

2a4b1. The backend system determines that the user does have an account but does not have a valid subscription and informs the System of that fact

2a4b2. The system informs the user that it does not have a valid subscription, and instructs them to go to the web to buy a subscription

2a4b3. The main success scenario terminates


```mermaid
---
title: Login
---
%%{init: {"flowchart": {"htmlLabels": false}} }%%
flowchart TB
   TRIGGER(["`The user asks the system to log them in using their Google or FB accounts`"])-->S1

   %% Main success scenario
   S1["`The system redirects the user to the appropriate 3rd party authentication system`"]-->S2
   S2{"`The user successfully authenticates using 3rd party authentication system?`"}
   S2--Yes-->S3
   S2--No-->FAILURE
   S3["`the 3rd party authentication system provides the system with the user's identification information`"]-->S4
   S4["`The system asks the backend system to confirm that the user has a valid subscription`"]-->S5
   S5{"`The backend API confirms that the user has an active subscription?`"}
   S5--Yes-->S6
   S6["`The backend system provides the system with the appropriate authentication token`"]-->SUCCESS

   %% Extension 5a: The user does not have a valid account
   S5--No-->EXT5a1
   EXT5a1["`The backend system determines that the user either does have an account or does not have a valid subscription and informs the System of that fact`"]-->EXT5a2;
   EXT5a2["`The system informs the user that it does not have a valid subscription and instructs them on how to get one`"]

   EXT5a2-->WEB_SUBSCRIPTION_PURCHASE

   SUCCESS([System logs the user in])

   FAILURE(Scenario terminates)

   WEB_SUBSCRIPTION_PURCHASE(User buys subscription on web)
```
