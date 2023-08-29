# Private Data

As outlined in **voting**, all sensitive data is stored and handled separately through LegalEntity.

```mermaid
classDiagram
direction LR
    class LegalEntity{
        -str legal_name
        -str phone_number
        -str email_address
        %% original key, not accessible by the user. derived keys can be used to reclaim the account
        -str restoration_key
    }
    class Address{
        -str street_address
        -str city
        -str state
        -str country
        -str zip_code
        -str what3words
    }
    LegalEntity --* Address : has

    LegalEntity --|> Person
    LegalEntity --|> Organization
    LegalEntity --* FinancialDetails
    Person --* PersonalDetails

    class FinancialDetails
    class PersonalDetails{
        -str birth_date
        -str social_security_number
        -str legal_id
    }
```
## Use Cases



## Requirements

## Solutions under Consideration

# Discussion

# Conclusion