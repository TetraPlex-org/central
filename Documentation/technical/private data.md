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

We should use [GDPR Subject Rights](https://www.gdprsummary.com/data-subject-rights) as a starting point for private data storage requirements. The Data storage system shall at minimum be secure and auditable but should be also be able to allow the system to address as much of what the  GDPR Data Subject stipulate. They are as follows:

1. The right to be informed
2. The right of access
3. The right to rectification
3. The right to erasure
4. The right to restrict processing
5. The right to data portability
6. The right to object
7. Rights about automated decision making and profiling.



## Solutions under Consideration

# Discussion

# Conclusion
