# Credits
Credits represent real-life money. Real-life money is needed to pay for server expenses and developers, thus it is crucial to offer End-Users and businesses value they are willing to pay for. Usually, buying credits is a one-way street, so that the money is not lost to the system. However, if someone is registered as a member of the club or the company, their credits can be converted back to real-life money for certain purposes. This is to ensure that the system is not used for money laundering. Inside the system, credits can only be used for things such as cosmetics, advertising, bounties and so on that are not directly related to community-building or the core functionality.
Credits can be traded via the **exchange** into karma and vice versa. The exchange is a Vickrey-Clarke-Groves auction that is run every 8 hours. The exchange is described in more detail in this [document](https://github.com/TetraPlex-org/basics/blob/main/Documentation/technical/exchange.md).
Let's call *credits* **Tc** (TetraPlex credits) and *karma* **Tk** (TetraPlex karma) in short.

```mermaid
classDiagram
direction LR
    class LegalEntity{
        -str legal_name
        -str legal_address
        ...
    }
    LegalEntity "1" --> "n" Account : identifies
    class Account{
        -Fraction credits
    }

    class Bargain{
        -int bargain_id
        -str bargain_description
        -int start_time
        -int end_time
        -Fraction factor
        -int region_id
    }
    class Region{
        -int region_id
        -str region_name
        -str region_description
        -str region_currency
        -Fraction region_base_price
    }


```


## How to get Credits?
Finding a good price that is acceptable for everyone is a very difficult task. Since this is about buying a virtual commodity with real-life money, we have to be very careful to not be seen as a scam or otherwise fraudulent, immoral or illegal. This means that prices need to be adjusted to regional differences in income while making it difficult for rich people to circumvent regional price differences using VPNs and multiple straw-man accounts or buying in bulk and selling at a higher price later or causing inflation and thus cheapening the value for everyone.


## What's the price?
So, let's assume we have established strong identity via LegalEntity and the user has a verified bank account. The user can now buy credits via the **shop**. How to price credits? Let's bootstrap the process with a price of 10 $ for a *standard bucket* of 10 credits. In the process of buying said credits, the user is asked following question: "Guess which price other people within your region think is fair on average! If your guess is closest to the result, you win an extra bucket!", to be evaluated every week.

This kind of "game" is derived from [Guess 2/3 of the average](https://en.wikipedia.org/wiki/Guess_2/3_of_the_average), which is similar to the "Keynesian beauty contest", a thought-experiment published by John Maynard Keynes in *The General Theory of Employment, Interest and Money* (1936). This solves the problem of finding the best price per region

Next problem results from rich people being able to use a VPN to the cheapest region and buy credits there. We don't combat this kind of behaviour in general, but instead we keep track of daily purchases. Once a user has bought more than 10 buckets (100 Tc), no more time-limited action factors are applied and instead, we apply a factor of

    log(current_daily_sum_of_purchased_credits) * base_region_price

to the price. This means that the price increases logarithmically with the amount of credits bought per day. This is to prevent rich people from buying lots of cheap credits in a region and then selling them at a higher price later. There is also no automatic way to buy credits in bulk, but except for increments of 10 credits (a bucket). So if you want to buy 1000 credits, you would buy 10 buckets at the flat, local, reduced price and then 90 buckets at the logarithmically increased price, one at a time, so overall, with a base price of 10 $ per 10 Tc, you would pay

    10 $ * 10 = 100 + sum(log(x)*x for x in range(100, 1010, 10)) $ = 322121 $

for 1000 credits. This is a lot of money, if you are not willing to wait between purchases, which would cause the logarithmic price to drop again.