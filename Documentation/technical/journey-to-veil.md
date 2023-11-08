

- gets invite code
- congierge popup 1
    - what is tetraplex
    - you were invited by {invite_name}
    -
- concierge popup 2
  - what is veiled
  - (10 seconds overview)
  -
- concierge popup 3
  - click here to call me(concerge)
- start using
- when over(session ends)

```mermaid
---
title: First Contact
---
%%{init: {"flowchart": {"htmlLabels": false}} }%%
flowchart TB
    TRIGGER(["`User clicked an invitation link`"])-->S1
    S1["`Client opens up and concierge pops up`"]-->S2
    S2["`Concierge welcomes and explains his function or user can skip intro`"]-->intro & S5
    subgraph intro
    S3["`Concierge asks the user how they want to be addressed`"]-->S3a
    S3a["`Show account page with filled out 'call name' field`"]-->S3b
    S3b["`Concierge tells the user they don't have to fill out anything, but can if they want to reclaim the account at some point`"]-->S4
    S4["`Show Persona, concierge explains how they are perceived by other users`"]
    end
    intro -->S5
    S5["`Concierge asks the user if they want to perform a guided demo operation or skip`"]-->tutorial & SUCCESS

    subgraph tutorial
    S6["`User performs a guided demo operation`"]-->S7
    S7["`Concierge tells to call him via the icon for any help`"]
    end
    tutorial -->SUCCESS
    SUCCESS(["`User completes the introduction`"])
```




```mermaid
---
title: Getting into the system
---
%%{init: {"flowchart": {"htmlLabels": false}} }%%
flowchart TB
   TRIGGER(["`User wants to get in and start asking questions`"])-->S1
   %% Main success scenario
   S1["`Get an invitation`"]-->S2
   S2{"`Do you know someone who already is a member?`"}
   S2-- Yes -->S3
   S2-- No -->S4
   S3["`Ask them for a link`"]-->S5a
   S5a{"`User is permitted to generate invitations`"}
   S5a -- Yes -->S5
   S5a -- No -->S4
   S4["`Get into the Prancing Pony and ask there for a link`"]-->S5 & FAILURE
   S5{"`Get an invitation link`"} --> SUCCESS
   SUCCESS([You're in!])
   FAILURE([User couldn't get an invitation])
```



```mermaid
journey
    title How to get an invite - Failure!
    section Website
        Google find website, need to go to page 2: 1: User, Google
        Webchat doesn't work properly: 1: User, Webchat
        Getting trolled when asking for invite: 1: User, Other Users
        Wait for ages and never get an invite: 1: User, Moderation
```
```mermaid

journey
    title Make account - Success
    section Website
        Google, find website, first hit: 4: User
        Open webchat: 4: User
        Ask for invitation: 4: User
        Get immediate invitation link: 5: User
        Senpai takes care of you: 5: User, Senpai
```

```mermaid
---
title: Answering a question
---
%%{init: {"flowchart": {"htmlLabels": false}} }%%
flowchart TD
    TRIGGER("`Marked self 'Ready' to answer question`")-->|"`System auto-adds to session `"|S1
    S1["`Get message displayed from the questioneer side`"]--> S2
    S2["`Write a response`"] --> S3
    S3["`Hit 'Ready to Send' button`"] --> S4
    S4["`Start 30 sec Timer & notify others for review`"] --> S5
    S5["`Wait for review`"] --> S6
    S6{"`Did anyone veto within the time limit?`"}
    S6 -- Yes --> S7
    S6 -- No --> S8
    S7["`Get feedback from other participants`"] --> S2
    S8["`Message is send through the veil to the Questioneer`"] --> S9
    S9{"`Is the questioneer happy with the response as an answer?`"}
    S9 -- No --> S1
    S9 -- Yes --> SUCCESS

    SUCCESS["User got a well-formulated, correct answer"]
    FAILURE["User couldn't get any answer"]
```