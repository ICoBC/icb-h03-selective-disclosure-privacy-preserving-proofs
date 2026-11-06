<!--
author:   ICoBC - International Council on Badges and Credentials
email:    info@icobc.net
version:  1.0.0
language: en
narrator: UK English Female
comment:  A Knowledge-stage course for HR, education IT and wallet community professionals on how selective disclosure works, how credential formats compare on privacy, why unlinkability needs more than disclosure, and what zero-knowledge proofs could add.
@style
:root { --icobc-navy:#02375B; --icobc-orange:#F78222; --icobc-cyan:#5DCAE7; --icobc-lime:#B1CF37; --icobc-mist:#F1F5F8; --icobc-line:#D8E2E9; --icobc-muted:#4F6576; }
body { font-family: "Open Sans", Arial, sans-serif; }
h1, h2, h3, h4 { color: var(--icobc-navy); }
a { color: var(--icobc-navy); }
table th { background: var(--icobc-mist); color: var(--icobc-navy); }
blockquote { border-left: 4px solid var(--icobc-orange); background: var(--icobc-mist); padding: 8px 16px; }
@end
-->

# Selective Disclosure and Privacy-Preserving Proofs

*What wallet privacy promises rest on.*

## About this course

Wallets promise that people can share only what is needed. This course explains the techniques behind that promise, shows where each technique stops, and helps you judge claims about privacy in credential systems. It is a Knowledge course: you learn to explain and recognise, and you check that understanding with a quiz.

**Who it is for**

- HR and learning technology owners who will receive credentials from wallets (audience C3).
- Education IT and credential operations staff who will issue them (audience E4).
- Members of the standards and wallet community who want a shared vocabulary (audience P3).

**Prerequisite:** ICB-F06 Digital Identity and the EUDI Wallet: Essentials.

**Framework alignment:** ICoBC Credentialing Skills Framework (ICSF), skill SECP "Security, privacy and data protection" (VRITE pillar: Trustworthiness), level L4 "Assure", stage K "Knowledge". At this level the skill is: leads threat modelling and fraud prevention for credential systems; advises on key management and long-term validity. This course builds the knowledge that supports that skill. It does not prove that you can do the work.

**Learning outcomes**

1. Explain the selective disclosure techniques used in wallet credentials.
2. Compare credential formats by their privacy properties.
3. Describe what zero-knowledge proofs could add and how mature they are.

**Workload:** self-paced, 3 hours notional learning. Live or workshop elements appear as facilitator notes.

**Assessment:** a knowledge check of 10 questions at the end of the course. Each module also has a short practice quiz that does not count towards the badge.

**Badge:** "Selective Disclosure and Privacy-Preserving Proofs (Knowledge, L4)", alignment code ICSF-SECP-L4-K. Evidence: passed knowledge check.

| Outcome | Module | How it is assessed |
|---|---|---|
| 1. Explain the selective disclosure techniques used in wallet credentials | Selective disclosure | Module quiz; final knowledge check, questions 1 to 3 |
| 2. Compare credential formats by their privacy properties | Formats compared | Module quiz; final knowledge check, questions 4 to 6 |
| 2. Compare credential formats by their privacy properties | Unlinkability | Module quiz; final knowledge check, questions 7 and 8 |
| 3. Describe what zero-knowledge proofs could add and how mature they are | Zero-knowledge proofs | Module quiz; final knowledge check, questions 9 and 10 |

**Status of the topics in this course**

| Topic | Status | Note |
|---|---|---|
| Wallet protocols and credential formats (OpenID4VC, SD-JWT VC, ISO mdoc) | Emerging | Specified for the EUDI Wallet; tooling and education profiles are still maturing. |
| EUDI Wallet (eIDAS 2.0) | Emerging | Member States must offer at least one wallet by 24 December 2026. Germany plans its state wallet ('d-you') for 2 January 2027 with basic functions first. Regulated private sectors must accept the wallet about one year after issuance starts. Readiness varies widely between Member States. |

Status as of November 2026; check before publishing.

<details><summary>Facilitator notes</summary>

**Optional live element (45 minutes, after Module 3):** a workshop where participants bring one credential use case from their own organisation and sketch what the verifier really needs to see. Close with a round in which each participant names one claim they would stop collecting.

Prepare a flipchart with the four module titles. Ask participants to place sticky notes for questions they still have after each module. Use these notes to steer the discussion.

</details>

## Selective disclosure

### Why share less

Think about a person who needs to prove one fact. A training provider wants to know that an applicant holds a professional certificate. The paper certificate also shows a full name, a date of birth, a home address and a grade. The provider needs one fact, and the paper shows five.

A wallet can do better. Selective disclosure lets the holder reveal only some of the claims in a credential while the verifier can still check that the credential is genuine and unchanged. The verifier receives less data, and the holder keeps control over the rest.

Three roles take part:

- The **issuer** creates and signs the credential.
- The **holder** keeps it in a wallet and decides what to show.
- The **verifier** asks for proof and checks it.

The central difficulty is this. A normal digital signature covers the whole document. If the holder removes a claim, the signature no longer matches, and the verifier cannot trust what is left. Selective disclosure techniques solve exactly this problem: they let a signature stay valid while some claims stay hidden.

Two ideas help you keep the topic clear:

- **Data minimisation** means collecting only the data you need for a stated purpose. Selective disclosure is a technical tool that supports it. The principle itself comes from data protection law and practice.
- **Disclosure** and **proof** are different things. A holder can disclose a claim, which reveals its value. A holder can also prove a statement about a claim, such as "over 18", without revealing the birth date. The second kind of proof needs extra support in the credential or in the wallet.

<!-- VERIFY: confirm that the wording of the data minimisation principle matches the wording the course owner wants to cite from the GDPR before publishing. -->

### Salted hashes: the main wallet technique

The technique most relevant to current wallet formats uses salted hashes. A hash function turns any input into a fixed-length fingerprint. The same input always gives the same fingerprint, and it is not practical to work backwards from the fingerprint to the input.

The issuer follows these steps:

1. For each claim, such as "family name" or "course title", the issuer adds a random value called a salt.
2. The issuer computes a hash of each salted claim.
3. The issuer signs the list of hashes, not the claims themselves.
4. The issuer gives the holder the signed list plus every claim with its salt.

When the holder presents the credential, the holder sends the signed list and only the chosen claims with their salts. The verifier hashes each disclosed claim, finds the matching fingerprint in the signed list, and checks the issuer's signature. Claims that stay hidden show up only as fingerprints. Because each has a random salt, the verifier cannot guess the hidden value by trying likely candidates.

This pattern is the basis of SD-JWT VC, one of the credential formats named for the EUDI Wallet. ISO mdoc uses a related idea: each data element is hashed and the hashes are signed, so the holder can release single elements. The details differ, and Module 2 compares them.

![A credential discloses only selected claims](data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" role="img"><title>A credential disclosing only selected claims</title><desc>A credential signed by an issuer holds four claims. The holder sends only two of them, family name and course title, to the verifier. Date of birth and home address stay hidden as fingerprints.</desc><rect x="0" y="0" width="800" height="450" fill="%23FFFFFF"/><rect x="30" y="60" width="260" height="330" rx="6" fill="%23F1F5F8" stroke="%23D8E2E9" stroke-width="2"/><text x="50" y="92" font-family="Open Sans, Arial, sans-serif" font-size="16" font-weight="bold" fill="%2302375B">Credential in the wallet</text><rect x="50" y="110" width="220" height="40" rx="6" fill="%23B1CF37" stroke="%2302375B" stroke-width="2"/><text x="60" y="135" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Family name: shown</text><rect x="50" y="165" width="220" height="40" rx="6" fill="%23B1CF37" stroke="%2302375B" stroke-width="2"/><text x="60" y="190" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Course title: shown</text><rect x="50" y="220" width="220" height="40" rx="6" fill="%23FFFFFF" stroke="%234F6576" stroke-width="2" stroke-dasharray="6 4"/><text x="60" y="245" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%234F6576">Date of birth: hidden</text><rect x="50" y="275" width="220" height="40" rx="6" fill="%23FFFFFF" stroke="%234F6576" stroke-width="2" stroke-dasharray="6 4"/><text x="60" y="300" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%234F6576">Home address: hidden</text><text x="50" y="350" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Signed by the issuer</text><path d="M290 160 L500 160" stroke="%2302375B" stroke-width="2" fill="none"/><path d="M490 152 L500 160 L490 168" stroke="%2302375B" stroke-width="2" fill="none"/><text x="300" y="145" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Holder sends 2 claims</text><rect x="510" y="110" width="260" height="130" rx="6" fill="%235DCAE7" stroke="%2302375B" stroke-width="2"/><text x="530" y="145" font-family="Open Sans, Arial, sans-serif" font-size="16" font-weight="bold" fill="%2302375B">Verifier receives</text><text x="530" y="175" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Family name, course title,</text><text x="530" y="197" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">fingerprints, signature</text><text x="530" y="270" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%234F6576">Hidden claims appear only as</text><text x="530" y="292" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%234F6576">fingerprints that cannot be reversed.</text></svg>)

### Other approaches and their limits

Salted hashes are one family of techniques. Others exist, and you may meet them in standards discussions.

**Per-claim signatures.** The issuer signs each claim separately. The holder can pass on single signed claims. This is simple, but the claims can lose their link to each other, and the credential becomes harder to manage.

**Signature schemes with built-in selective disclosure.** Some signature schemes let a holder derive a proof from the original signature that covers only the chosen claims. The verifier checks the derived proof against the issuer's public key. These schemes can also help with unlinkability, which Module 3 covers. They are less widely deployed in wallet profiles than salted-hash formats.

**Predicate proofs.** A predicate proof shows that a claim meets a condition, such as "birth date is before a given day", without showing the value. Zero-knowledge techniques make this possible, and Module 4 returns to it.

What selective disclosure with salted hashes does not do matters as much as what it does:

- The signature, the issuer's key and the structure of the credential stay visible and are the same each time the holder presents the credential. A verifier, or several verifiers who compare notes, can recognise the same credential again. This is a linkability problem.
- Disclosed claims are shown in full. A holder cannot show "over 18" from a birth date unless the issuer has also issued an "over 18" claim, or the format supports a proof about the value.
- The verifier can keep whatever it receives. The technique limits what is sent. It cannot limit what the verifier does afterwards. Policy, law and audit have to cover that.

> Selective disclosure reduces what a verifier receives. It does not control what the verifier does with it.

**Worked example: The corporate academy checks a safety certificate**

The learning technology owner at a manufacturing company, Ms Okafor, wants contractors to show a site safety certificate before they enter a plant. The certificate in the contractor's wallet holds four claims: full name, certificate title, expiry date and home address.

At the gate, the verification service asks for three things: certificate title, expiry date and whether the signature is valid. The contractor's wallet shows these three. The home address stays hidden, covered only by its fingerprint.

The plant keeps a log of each entry. Ms Okafor's team checks that the log holds the title and expiry date and not the address. The data protection officer notes that the plant never had a reason to hold the address, so the design removes a risk instead of managing one.

Ms Okafor asks: what could still be linked? The same signature and issuer key appear at every gate visit. If the plant shares its log with a second site, both could see that one contractor entered both. She records this as a question for Module 3.

**Practice activity: Minimise a request**

Choose a credential check from your own work, for example proof of employment, proof of a course completion or proof of a professional licence. Write down:

1. The one decision the verifier must make.
2. The claims the verifier would need to make it.
3. The claims the credential holds that the verifier does not need.
4. Which of the unneeded claims could be misused if the verifier stored them.

Keep your notes for the workshop or for your own use. There is no single right answer. The point is the habit of starting from the decision and not from the credential.

<details><summary>Facilitator notes</summary>

Ask participants to share their lists in pairs. Look for cases where the "needed" list is longer than it should be. Common examples are date of birth when only an age check is needed, and full name when only a membership check is needed. Note the cases where a predicate such as "over 18" would help and where a claim would have to be issued for it.

Time: 10 minutes for the activity and 10 minutes for discussion.

</details>

### Check your understanding

**Question 1.** Why does a normal digital signature on a whole document make selective disclosure difficult?

[( )] Signatures can only be created for documents that are shorter than one page.
[(X)] The signature covers the whole document, so removing any claim breaks it and the verifier can no longer trust the rest.
[( )] Signatures always reveal the holder's name to every verifier.
[( )] Signatures expire as soon as the holder opens the wallet.
[[?]] Think about what a signature is computed over.
****
A signature is computed over the complete content. If the holder removes a claim, the content changes and the signature no longer matches. Selective disclosure techniques, such as signing hashes of salted claims, solve this by letting the signature cover fingerprints that stay valid when some claims are hidden.
****

**Question 2.** In the salted hash technique, what does the issuer sign?

[( )] Only the holder's wallet identifier.
[( )] The full list of claims in readable form, together with every salt.
[(X)] The list of hashes of the salted claims.
[( )] Nothing: the holder signs the claims.
[[?]] The signed object must stay valid when claims are left out.
****
The issuer signs the list of hashes. The claims and their salts travel separately to the holder. The holder can then reveal a chosen claim and its salt, and the verifier checks that the hash matches an entry in the signed list.
****

**Question 3.** What is the purpose of the random salt added to each claim?

[( )] It makes the credential shorter.
[( )] It proves the holder's identity to the verifier.
[( )] It lets the verifier read hidden claims later.
[(X)] It stops a verifier from guessing a hidden value by hashing likely candidates and comparing the results.
[[?]] Consider a claim with few possible values, such as a grade.
****
Without a salt, a verifier could hash every likely value, for example every possible grade, and compare the results with the fingerprint. A random salt per claim makes such guessing impractical.
****

**Question 4.** Which statement about what selective disclosure with salted hashes does not do is correct?

[( )] It lets the verifier see hidden claims after a delay.
[(X)] It does not stop the verifier from keeping and reusing the claims it receives.
[( )] It removes the need for any data protection rules.
[( )] It hides the issuer's key from the verifier.
[[?]] Think about what happens after the data has been sent.
****
Selective disclosure limits what is sent. It cannot limit what the verifier stores or does afterwards. Law, policy and audit have to cover that part.
****

## Formats compared

### Three formats, three families

The EUDI Wallet specifications name credential formats and protocols that work together. Learners often mix up the format, which describes the credential, and the protocol, which moves it. This module looks at formats and keeps protocols to a short note at the end.

**SD-JWT VC.** A credential built on JSON Web Tokens with selective disclosure through salted hashes. The issuer signs a token that holds hashes of the claims. The holder receives the token and the claims with their salts, and chooses which to reveal. SD-JWT VC is a credential format that fits web-style systems well, because it builds on JSON, a common data format.

**ISO mdoc.** A credential format from the ISO/IEC 18013-5 family, first designed for mobile driving licences. Data elements are grouped by namespace, each element is hashed, and the issuer signs a structure that holds the hashes. The holder releases single elements. mdoc uses a compact binary encoding and was designed with proximity use in mind, such as a presentation at a counter.

**W3C Verifiable Credentials with data integrity proofs.** A credential model from the World Wide Web Consortium. It can use different proof types, including signature schemes that support selective disclosure and unlinkability by design. Whether a given deployment offers these properties depends on the proof type that the deployment chooses.

Two points apply to all three:

- A format sets the technical possibilities. A wallet, an issuer profile and a verifier policy decide what happens in practice.
- A format that supports a property does not guarantee it. For example, a format may allow single-use credentials, but an issuer may still issue one reusable credential.

<!-- VERIFY: confirm the current status and naming of the W3C Verifiable Credentials data model version and data integrity specifications before publishing. -->

### Comparing privacy properties

To compare formats you need a short list of properties. Use these:

- **Selective disclosure:** can the holder reveal single claims?
- **Predicate proofs:** can the holder prove a statement about a value without showing it?
- **Verifier unlinkability:** can two verifiers tell that the same credential was shown to both?
- **Issuer unlinkability:** can the issuer tell where a credential was shown?
- **Offline presentation:** can the holder present without a network connection?
- **Maturity in wallet profiles:** how settled is the format in the EUDI Wallet context?

The table below gives a cautious summary of the general position. It describes typical designs, and actual profiles may add or remove features.

![Format comparison table](data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" role="img"><title>Format comparison by privacy property</title><desc>A table with three formats in the columns: SD-JWT VC, ISO mdoc and a data integrity credential with an advanced signature. Rows show selective disclosure, same credential recognisable across verifiers, and typical use. SD-JWT VC and ISO mdoc support selective disclosure but a reused credential can be recognised. The advanced signature type can avoid this.</desc><rect x="0" y="0" width="800" height="450" fill="%23FFFFFF"/><rect x="30" y="40" width="740" height="50" rx="6" fill="%23F1F5F8" stroke="%23D8E2E9" stroke-width="2"/><text x="50" y="72" font-family="Open Sans, Arial, sans-serif" font-size="16" font-weight="bold" fill="%2302375B">Property</text><text x="250" y="72" font-family="Open Sans, Arial, sans-serif" font-size="16" font-weight="bold" fill="%2302375B">SD-JWT VC</text><text x="430" y="72" font-family="Open Sans, Arial, sans-serif" font-size="16" font-weight="bold" fill="%2302375B">ISO mdoc</text><text x="600" y="72" font-family="Open Sans, Arial, sans-serif" font-size="16" font-weight="bold" fill="%2302375B">Advanced signature</text><rect x="30" y="100" width="740" height="70" rx="6" fill="%23FFFFFF" stroke="%23D8E2E9" stroke-width="2"/><text x="50" y="140" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Selective disclosure</text><rect x="240" y="115" width="140" height="40" rx="6" fill="%23B1CF37" stroke="%2302375B" stroke-width="2"/><text x="255" y="140" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Yes, per claim</text><rect x="420" y="115" width="140" height="40" rx="6" fill="%23B1CF37" stroke="%2302375B" stroke-width="2"/><text x="435" y="140" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Yes, per element</text><rect x="590" y="115" width="160" height="40" rx="6" fill="%23B1CF37" stroke="%2302375B" stroke-width="2"/><text x="605" y="140" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Yes, derived proof</text><rect x="30" y="180" width="740" height="70" rx="6" fill="%23FFFFFF" stroke="%23D8E2E9" stroke-width="2"/><text x="50" y="205" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Same credential</text><text x="50" y="225" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">recognisable?</text><rect x="240" y="195" width="140" height="40" rx="6" fill="%23F78222" stroke="%2302375B" stroke-width="2"/><text x="255" y="220" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Yes, if reused</text><rect x="420" y="195" width="140" height="40" rx="6" fill="%23F78222" stroke="%2302375B" stroke-width="2"/><text x="435" y="220" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Yes, if reused</text><rect x="590" y="195" width="160" height="40" rx="6" fill="%235DCAE7" stroke="%2302375B" stroke-width="2"/><text x="605" y="220" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Can be avoided</text><rect x="30" y="260" width="740" height="70" rx="6" fill="%23FFFFFF" stroke="%23D8E2E9" stroke-width="2"/><text x="50" y="300" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Typical setting</text><text x="250" y="292" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Web and online</text><text x="250" y="312" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">presentation</text><text x="430" y="292" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Proximity and</text><text x="430" y="312" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">online presentation</text><text x="600" y="292" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Depends on the</text><text x="600" y="312" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">chosen profile</text><text x="30" y="370" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%234F6576">Typical designs only. Actual profiles may differ. Orange marks a privacy limit, lime a supported feature.</text><text x="30" y="395" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%234F6576">Cyan marks a property that depends on the proof type chosen.</text></svg>)

| Property | SD-JWT VC | ISO mdoc | Data integrity credential with an advanced signature |
|---|---|---|---|
| Selective disclosure | Yes, per claim, through salted hashes | Yes, per data element, through hashed elements | Yes, through a derived proof, depending on the proof type |
| Predicate proofs | Not by itself; needs an extra claim or an extra technique | Not by itself; needs an extra element or an extra technique | Possible in some designs |
| Verifier unlinkability | Limited: the issuer signature repeats when the credential is reused | Limited: the issuer signature repeats when the credential is reused | Possible, depending on the proof type |
| Issuer unlinkability | Limited | Limited | Possible, depending on the proof type |
| Offline presentation | Depends on the profile | Designed with proximity use in mind | Depends on the profile |
| Maturity in EUDI Wallet context | Emerging; specified for the EUDI Wallet | Emerging; specified for the EUDI Wallet | Less settled in the EUDI Wallet context |

Use this table as a starting point for questions, not as a procurement answer. Real decisions need the current profile text and a threat model.

<!-- VERIFY: confirm the table cells against the current EUDI Wallet architecture and reference framework before publishing. -->

### What decides privacy in practice

Privacy depends on more than the format. Four layers matter:

1. **The format**, which sets what is possible.
2. **The issuer profile**, which decides how credentials are issued. An issuer that signs one long-lived credential creates a stable identifier. An issuer that signs a batch of single-use credentials removes much of it. Batch issuance is a design choice that some profiles support, and it is one way to reduce linkability even with salted hash formats.
3. **The wallet**, which decides what the holder can see and choose. A wallet that shows clearly which claims a verifier asks for supports informed consent. A wallet that hides this does not.
4. **The verifier**, which decides what to ask for and how long to keep it. A verifier that asks for more than it needs, or stores what it receives, weakens every other layer.

**Protocols, in short.** OpenID4VC names a family of protocols for issuing and presenting credentials over the web. ISO/IEC 18013-5 describes proximity presentation for mdoc. A format can often travel over more than one protocol. When you read a specification, first ask whether it describes the credential or the way it moves.

**Worked example: The university chooses a format for graduation credentials**

A university registry, led by Dr Lindqvist, plans to issue digital degree credentials to graduates. Graduates will show them to employers, to other universities and to professional bodies.

Dr Lindqvist's team lists the likely verifiers and what each needs:

- An employer needs the degree title, the awarding institution and the award year.
- A second university needs the degree title and the grade band.
- A professional body needs the degree title and a confirmation of name.

All three formats from this module allow selective disclosure, so each verifier can receive its own subset. The team then asks the next question: do the graduates need protection from being tracked across these verifiers? The team notes that a graduate may show the credential to many employers over several years. With a reusable credential in a salted hash format, the same issuer signature would repeat each time.

The team decides to ask the issuer profile working group whether batch issuance of single-use credentials is supported, and to record the open question in the privacy impact assessment. It does not pick a format yet. It sets out its criteria first.

**Practice activity: Build a comparison for your own context**

Take your own organisation and list three likely verifiers of a credential you issue or receive. For each verifier, write down:

1. The claims it needs.
2. Whether the holder would mind if two verifiers could tell the credential was the same.
3. Which of the properties in the comparison table matters most to you, and why.

Then write one sentence for each of the four layers (format, issuer profile, wallet, verifier) that describes what you would want to check.

<details><summary>Facilitator notes</summary>

Run a short group exercise: split the group into issuers, holders and verifiers. Each group writes the two privacy properties it cares most about. Compare the lists. Typical results: issuers care about maturity and tooling, holders care about unlinkability and clear consent screens, verifiers care about simplicity and legal clarity.

Remind participants that the table is a simplification and that profiles change. Direct them to the primary sources in the final section.

Time: 15 minutes.

</details>

### Check your understanding

**Question 1.** Which description of the relationship between a format and a protocol is correct?

[( )] A format moves credentials between parties and a protocol describes what a credential contains.
[(X)] A format describes what a credential contains and how it is signed, and a protocol describes how it is issued or presented.
[( )] Formats and protocols are two names for the same thing.
[( )] A protocol decides which claims are hashed and a format decides who the verifier is.
[[?]] One answers "what is it?" and the other answers "how does it travel?".
****
A format, such as SD-JWT VC or ISO mdoc, describes the credential itself. A protocol, such as those in the OpenID4VC family or the proximity protocol in ISO/IEC 18013-5, describes how credentials are issued and presented.
****

**Question 2.** Which statement about SD-JWT VC and ISO mdoc is supported by the module?

[( )] Neither supports selective disclosure.
[( )] Only one of them can hide claims from a verifier.
[(X)] Both support selective disclosure through hashed data signed by the issuer, and a reused credential can still be recognised through the repeated signature.
[( )] Both guarantee that two verifiers can never tell that the same credential was shown.
[[?]] Remember what stays the same each time the credential is shown.
****
Both formats let the holder reveal chosen claims or elements. The issuer signature and key repeat when the same credential is reused, so verifiers who compare notes can recognise it.
****

**Question 3.** A registry issues one long-lived credential per graduate in a salted hash format. What is the main privacy concern the module raises?

[( )] Graduates cannot hide any claims.
[( )] The credential cannot be checked offline.
[(X)] The repeated issuer signature can act as a stable identifier across verifiers.
[( )] The credential reveals the salts of hidden claims.
[[?]] Think about what repeats at each presentation.
****
Selective disclosure still works, but the signature and issuer data repeat at each presentation. Batch issuance of single-use credentials is one way to reduce this, if the profile supports it.
****

**Question 4.** Why does the module call the comparison table "a starting point for questions, not a procurement answer"?

[( )] Because formats cannot be compared at all.
[( )] Because the table contains invented data.
[(X)] Because actual privacy depends on the profile, the issuer, the wallet and the verifier, and profiles change over time.
[( )] Because only one format is allowed in any Member State.
[[?]] Count the layers the module lists.
****
Privacy depends on four layers: format, issuer profile, wallet and verifier. A table of typical designs cannot capture all of them. Current profile text and a threat model are needed for real decisions.
****

## Unlinkability

### What linking means

Selective disclosure limits what a verifier sees in one presentation. Unlinkability asks a different question: can anyone connect two presentations to the same holder or the same credential?

Linking can happen in several ways:

- **Between verifiers.** Verifier A and verifier B compare what they received. If a value, such as a signature or a key, is the same in both, they know the same credential was used. If they also hold a name or an identifier, they learn that the holder visited both.
- **Between visits to the same verifier.** A verifier can recognise a returning holder through repeated values and build a history.
- **Between issuer and verifier.** An issuer that sees where its credentials are shown, or a verifier that shares data with the issuer, can learn about the holder's activity. This is sometimes called the "phone home" problem. It arises when a verifier must contact the issuer to check a credential. Designs in which the verifier checks the signature locally, without contacting the issuer, avoid this.
- **Through the data itself.** A few disclosed claims can be unique enough to identify a person. A birth date, a postcode and a job title together can single someone out, even without a name. This is a re-identification risk, and no cryptography removes it.

It helps to separate three terms:

- **Selective disclosure:** revealing only some claims.
- **Unlinkability:** preventing presentations from being tied together.
- **Anonymity:** not being identifiable at all. A presentation with a name is not anonymous, even if it is unlinkable to other presentations.

A credential system can offer one without the others. A presentation that shows only the course title may still be linkable if the issuer signature repeats.

### Techniques that reduce linking

Several techniques reduce linking. Each has costs.

**Batch issuance of single-use credentials.** The issuer gives the wallet many copies of the same credential, each signed separately and each with its own key material. The wallet uses each copy once. Verifiers cannot tell that two copies belong to the same holder from the signature alone. The cost is operational: the issuer has to produce, store and replace many credentials, and the wallet has to manage them. When the batch runs out, the holder must obtain more, and rules must decide how often.

**Short-lived credentials.** A credential with a short validity period limits how long a stable value can be tracked. The holder must renew often, which depends on a good issuer connection.

**Signature schemes with unlinkable proofs.** Some schemes let the holder derive a fresh proof from the same credential for each presentation. The proofs cannot be linked by their signature values. This is the approach that supports unlinkability without batch issuance. It depends on newer cryptography that is less settled in wallet profiles.

**Local verification.** The verifier checks the signature and the status data without telling the issuer. Where a credential needs a status check, such as revocation, the design of the status mechanism matters. A status check that queries one credential at a time can reveal which credential is being checked. Designs that publish status data in a way that does not identify one holder reduce this.

**Pairwise or per-verifier identifiers.** Where a verifier needs to recognise a returning holder, a wallet can provide an identifier that differs for each verifier. Two verifiers then cannot join their records by that identifier.

![Linking between verifiers](data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" role="img"><title>Two verifiers compare a repeated signature</title><desc>On the left, a holder presents the same credential to verifier A and verifier B. Both receive the same signature value. They compare notes and learn that one holder visited both. On the right, the holder presents two single-use credentials with different signature values. The verifiers cannot connect them by signature.</desc><rect x="0" y="0" width="800" height="450" fill="%23FFFFFF"/><text x="30" y="40" font-family="Open Sans, Arial, sans-serif" font-size="16" font-weight="bold" fill="%2302375B">Reused credential</text><text x="440" y="40" font-family="Open Sans, Arial, sans-serif" font-size="16" font-weight="bold" fill="%2302375B">Single-use credentials</text><line x1="400" y1="20" x2="400" y2="430" stroke="%23D8E2E9" stroke-width="2"/><circle cx="90" cy="215" r="40" fill="%2302375B"/><text x="90" y="220" text-anchor="middle" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%23FFFFFF">Holder</text><rect x="240" y="80" width="140" height="70" rx="6" fill="%23F78222" stroke="%2302375B" stroke-width="2"/><text x="310" y="110" text-anchor="middle" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Verifier A</text><text x="310" y="132" text-anchor="middle" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">sees value X7</text><rect x="240" y="280" width="140" height="70" rx="6" fill="%23F78222" stroke="%2302375B" stroke-width="2"/><text x="310" y="310" text-anchor="middle" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Verifier B</text><text x="310" y="332" text-anchor="middle" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">sees value X7</text><path d="M128 200 L240 125" stroke="%2302375B" stroke-width="2" fill="none"/><path d="M128 230 L240 305" stroke="%2302375B" stroke-width="2" fill="none"/><text x="250" y="225" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Same value: linked</text><circle cx="490" cy="215" r="40" fill="%2302375B"/><text x="490" y="220" text-anchor="middle" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%23FFFFFF">Holder</text><rect x="640" y="80" width="140" height="70" rx="6" fill="%23F78222" stroke="%2302375B" stroke-width="2"/><text x="710" y="110" text-anchor="middle" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Verifier A</text><text x="710" y="132" text-anchor="middle" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">sees value K2</text><rect x="640" y="280" width="140" height="70" rx="6" fill="%23F78222" stroke="%2302375B" stroke-width="2"/><text x="710" y="310" text-anchor="middle" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Verifier B</text><text x="710" y="332" text-anchor="middle" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">sees value M9</text><path d="M528 200 L640 125" stroke="%2302375B" stroke-width="2" fill="none"/><path d="M528 230 L640 305" stroke="%2302375B" stroke-width="2" fill="none"/><text x="590" y="225" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Different values</text><text x="30" y="410" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%234F6576">Values X7, K2 and M9 stand for signature data. They are illustrative.</text></svg>)

**What no technique fixes alone.** If the disclosed claims identify a person, unlinkable signatures do not help. If the verifier asks for a national identifier that is the same everywhere, verifiers can link by that value. The best result comes from combining a careful request (Module 1), a suitable issuing profile (Module 2), and a technique from this module.

**Worked example: The HR department designs a contractor check**

An HR operations lead, Mr Brandt, runs onboarding for external trainers. Each trainer shows a teaching qualification credential at three points: on first registration, when a course is assigned, and when a training room is booked. These checks are run by three different services.

Mr Brandt's team notices that if the credential is reusable, all three services receive the same signature and could join their logs. They look at what each service really needs. The room booking needs only to know that the trainer is registered, which the registration service already knows.

The team makes three changes:

1. The registration service verifies the qualification once and issues an internal, short-lived access token to the trainer.
2. The course assignment service asks for the qualification title only.
3. The room booking service never sees the qualification credential at all.

This design needs no new cryptography. It reduces linking by reducing how many parties see the credential. Mr Brandt adds a note that for trainers who also work at other organisations, a wallet profile with batch issuance would reduce linking across employers, and he asks the education provider that issues the qualification whether it supports it.

**Practice activity: Trace the links**

Draw, on paper, one credential journey from your own context: the issuer, the wallet and up to three verifiers. Mark every value that stays the same across presentations, such as a signature, a key or an identifier. Then mark any claim that could single a person out when combined with another. Circle the three links that would worry you most and write one possible change for each.

<details><summary>Facilitator notes</summary>

This module fits the live workshop. Give each group an A3 sheet. Ask them to draw one journey and mark repeating values with an orange pen. Collect the circled links on a wall and sort them: "fix by design", "fix by technique", "fix by policy". Many links fall into the first or third group, which supports the message that cryptography is one tool among several.

Time: 20 minutes.

</details>

### Check your understanding

**Question 1.** Which situation is an example of linking between verifiers?

[(X)] Two verifiers compare a repeated signature value and learn that one holder visited both.
[( )] A holder shows only one claim to one verifier.
[( )] An issuer signs a list of hashes.
[( )] A wallet shows a consent screen before a presentation.
[[?]] Linking connects separate presentations.
****
When two verifiers see the same signature or key, they can tell that the same credential was used, and can join their records if they share data. Showing one claim or signing hashes does not by itself connect separate presentations.
****

**Question 2.** What is the difference between unlinkability and anonymity?

[( )] They mean the same thing.
[( )] Unlinkability means no claims are shown; anonymity means all claims are shown.
[(X)] Unlinkability prevents presentations from being tied together; anonymity means the person cannot be identified at all.
[( )] Anonymity is a property of the issuer; unlinkability is a property of the verifier.
[[?]] A presentation can include a name and still be unlinkable to other presentations.
****
A presentation with a name is not anonymous, but it can still be unlinkable to other presentations if the cryptographic values differ each time.
****

**Question 3.** Which measure reduces linking by using many separately signed copies of the same credential?

[( )] Short validity periods only.
[(X)] Batch issuance of single-use credentials.
[( )] Hashing every claim with the same salt.
[( )] Asking the verifier to contact the issuer on every check.
[[?]] Each copy is used once.
****
In batch issuance the issuer signs many copies, each with its own key material, and the wallet uses each once. Verifiers cannot connect them by signature. The cost is operational effort for the issuer and the wallet.
****

**Question 4.** In the HR example, why does the room booking service never see the qualification credential?

[( )] Because credentials cannot be shown to more than one service.
[( )] Because the service has no network access.
[(X)] Because it does not need the qualification to make its decision, and fewer parties seeing the credential means fewer places for linking.
[( )] Because the credential is encrypted for the registration service only.
[[?]] Go back to the principle from Module 1: start from the decision.
****
The booking decision needs only the fact that the trainer is registered. Removing the credential from that step reduces linking by reducing how many parties see it.
****

## Zero-knowledge proofs

### What a zero-knowledge proof is

A zero-knowledge proof lets one party, the prover, convince another, the verifier, that a statement is true without revealing why it is true. The verifier learns that the statement holds and learns nothing else.

A classic way to picture this: a prover wants to show that two objects are different without saying which is which. The prover can do this through a repeated game in which a verifier cannot guess the answer unless the prover really can tell the objects apart. After enough rounds, the verifier is convinced, and has learned nothing about the details.

In credential systems, the statement is something like "I hold a credential signed by this issuer, and the birth date in it is before a given day." The proof convinces the verifier of this. The verifier does not see the birth date, the signature or any other claim.

Zero-knowledge proofs have three properties:

- **Completeness:** an honest prover with a true statement can convince the verifier.
- **Soundness:** a prover with a false statement cannot convince the verifier, except with a very small chance.
- **Zero knowledge:** the verifier learns nothing beyond the fact that the statement is true.

You do not need the mathematics for this course. You need to recognise what the technique promises and to ask good questions about it.

### What they could add

Compared with the salted hash approach from Module 1, zero-knowledge proofs could add several things.

**Predicate proofs.** A holder can prove "over 18", "resident in a given country" or "grade at least a pass" from the underlying value, without the issuer having to issue each derived claim in advance.

**Stronger unlinkability.** A holder can create a new proof for each presentation from the same credential. Each proof looks different, so verifiers cannot connect them by signature values.

**Proofs about several credentials.** A holder can prove a statement that combines claims from more than one credential, such as "the person in this degree credential is the person in this identity credential", without revealing the underlying data. This is an area of active research and specification work.

**Proof of holding a key without revealing it,** which supports binding a credential to a wallet.

**Less dependence on single-use batches.** A zero-knowledge approach can offer unlinkability from one credential, which reduces the operational load of batch issuance.

![What zero-knowledge proofs could add](data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" role="img"><title>Disclosure compared with a zero-knowledge predicate proof</title><desc>Two rows. In the first row, the holder discloses a birth date and the verifier sees the date. In the second row, the holder sends a zero-knowledge proof and the verifier sees only the result: over 18, yes. The birth date stays with the holder.</desc><rect x="0" y="0" width="800" height="450" fill="%23FFFFFF"/><text x="30" y="40" font-family="Open Sans, Arial, sans-serif" font-size="16" font-weight="bold" fill="%2302375B">Disclosure of a claim</text><circle cx="80" cy="110" r="36" fill="%2302375B"/><text x="80" y="115" text-anchor="middle" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%23FFFFFF">Holder</text><path d="M120 110 L400 110" stroke="%2302375B" stroke-width="2" fill="none"/><path d="M390 102 L400 110 L390 118" stroke="%2302375B" stroke-width="2" fill="none"/><rect x="190" y="85" width="140" height="50" rx="6" fill="%23FFFFFF" stroke="%2302375B" stroke-width="2"/><text x="260" y="115" text-anchor="middle" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Birth date: shown</text><rect x="410" y="75" width="360" height="70" rx="6" fill="%235DCAE7" stroke="%2302375B" stroke-width="2"/><text x="430" y="105" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Verifier sees the birth date</text><text x="430" y="127" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">and works out the age itself</text><line x1="30" y1="200" x2="770" y2="200" stroke="%23D8E2E9" stroke-width="2"/><text x="30" y="240" font-family="Open Sans, Arial, sans-serif" font-size="16" font-weight="bold" fill="%2302375B">Zero-knowledge predicate proof</text><circle cx="80" cy="310" r="36" fill="%2302375B"/><text x="80" y="315" text-anchor="middle" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%23FFFFFF">Holder</text><path d="M120 310 L400 310" stroke="%2302375B" stroke-width="2" fill="none"/><path d="M390 302 L400 310 L390 318" stroke="%2302375B" stroke-width="2" fill="none"/><rect x="170" y="285" width="180" height="50" rx="6" fill="%23FFFFFF" stroke="%2302375B" stroke-width="2"/><text x="260" y="315" text-anchor="middle" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Proof: over 18</text><rect x="410" y="275" width="360" height="70" rx="6" fill="%235DCAE7" stroke="%2302375B" stroke-width="2"/><text x="430" y="305" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">Verifier learns only: over 18, yes</text><text x="430" y="327" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%2302375B">The birth date stays with the holder</text><text x="30" y="400" font-family="Open Sans, Arial, sans-serif" font-size="14" fill="%234F6576">Cyan marks the verifier, here an education provider or any other party that checks.</text></svg>)

### How mature are they

The honest answer is: it depends on what you mean. Zero-knowledge techniques are well studied in research. Use in wallet credentials is still developing. Look at four dimensions of maturity.

**Cryptographic maturity.** Several zero-knowledge constructions are well analysed. Others are newer and have had less public scrutiny. A decision to rely on one needs review by qualified cryptographers.

**Standardisation.** Standards bodies work on signature schemes and proof formats that support unlinkable proofs and predicate proofs. Whether a particular scheme is final, widely implemented and accepted in the EUDI Wallet profiles is a matter to check against current texts. Do not assume it.

<!-- VERIFY: confirm the current standardisation status of zero-knowledge and unlinkable signature schemes in the EUDI Wallet architecture and reference framework before publishing. -->

**Implementation maturity.** Libraries, wallets and verifier tooling need to support the scheme. Production-quality support, security audits and interoperability tests take time.

**Operational maturity.** Proof generation can cost computing power, which matters on a phone. Proof size and speed affect user experience. Status checks, key rotation and revocation need designs that fit with the proof scheme. Long-term validity is a concern: some schemes rely on assumptions that future computers could weaken, and an organisation that must keep proofs valid for many years should ask about this.

In the context of this course, the topic status is **Emerging**. The formats named for the EUDI Wallet are specified. Tooling and education profiles are still maturing. A cautious message for decision makers: plan for zero-knowledge proofs as a direction, use selective disclosure and careful issuing practice today, and avoid claims that a product delivers "full privacy" because it mentions zero knowledge.

Questions to ask when a vendor or a proposal mentions zero-knowledge proofs:

1. Which statements can be proved, and which cannot?
2. Which scheme is used, and where is it standardised?
3. Has it been independently reviewed?
4. What does it cost in time, battery and data size on a typical phone?
5. What happens to a proof or credential if the underlying assumptions weaken?
6. What does the verifier still see, and what can it store?

**Worked example: The training provider considers age and eligibility proofs**

A vocational training provider, led by operations manager Ms Rahman, runs courses with an age limit and with eligibility rules based on employment status. Learners show credentials from their wallets at enrolment.

Today the provider asks learners to show a date of birth and an employer confirmation. Ms Rahman's team would like to ask only for "age at least 18" and "currently employed in the sector".

The team looks at two routes:

- **Route A:** ask the issuers to add an "age over 18" claim and an "employed in sector" claim to the credentials. Selective disclosure then reveals only those. This works with salted hash formats and needs issuer cooperation.
- **Route B:** wait for wallets and verifiers that support zero-knowledge predicate proofs, then prove the statements from the underlying values.

The team chooses Route A for the next intake because it can be done with current tooling, and records Route B as a watch item. They list the six questions from this module and decide to ask them when a supplier proposes a proof-based solution. They also note that, in either route, the provider must decide how long to keep enrolment records and must say so to learners.

**Practice activity: Question a zero-knowledge claim**

Imagine a supplier states: "Our wallet uses zero-knowledge proofs, so verifiers learn nothing about holders." Write a short reply, no more than six sentences, that:

1. Names what zero-knowledge proofs could add.
2. Names at least two things the statement leaves open.
3. Lists three of the six questions from this module that you would ask first.

<details><summary>Facilitator notes</summary>

Ask participants to read their replies aloud in pairs. The partner plays the supplier and answers briefly. This shows how easily a general promise hides open questions. Remind the group that the aim is informed questions and not rejection of the technique.

If time allows, invite someone from the standards and wallet community (audience P3) to describe from experience which proof types are being discussed in their groups, without naming products.

Time: 15 minutes.

</details>

### Check your understanding

**Question 1.** What does a zero-knowledge proof allow a holder to do?

[( )] Show all claims in a credential at once.
[(X)] Convince a verifier that a statement is true without revealing why it is true.
[( )] Remove the issuer's signature from a credential.
[( )] Change the content of a credential after issue.
[[?]] Think of "over 18" shown without the birth date.
****
A zero-knowledge proof convinces the verifier that a statement holds, such as "over 18", and reveals nothing beyond that fact.
****

**Question 2.** Which of the following could zero-knowledge proofs add compared with salted hash selective disclosure alone?

[( )] The ability to avoid any form of verifier checking.
[(X)] Predicate proofs about a value, and unlinkable proofs created freshly for each presentation.
[( )] A guarantee that verifiers will delete data.
[( )] Removal of the need for issuers.
[[?]] Look back at the list in "What they could add".
****
Zero-knowledge techniques can support predicate proofs and fresh, unlinkable proofs from one credential. They do not control what verifiers do with the data and they do not remove the need for issuers.
****

**Question 3.** How should a decision maker describe the maturity of zero-knowledge proofs in wallet credentials?

[( )] Fully settled and ready for every wallet profile.
[( )] Not studied and not worth watching.
[(X)] Well studied in research, with standardisation, tooling and operations still developing, so a direction to plan for and to check against current texts.
[( )] Banned by the EUDI Wallet rules.
[[?]] The topic status in this course is Emerging.
****
Research on zero-knowledge proofs is advanced, but standards, tools and operational experience in wallet credentials are still developing. Decision makers should plan for the direction, rely on selective disclosure and careful issuing today, and verify current status.
****

**Question 4.** Which question belongs on the list to ask when a supplier mentions zero-knowledge proofs?

[( )] What colour is the wallet icon?
[( )] How many staff does the supplier employ?
[(X)] Which scheme is used, where is it standardised, and has it been independently reviewed?
[( )] Can the proof be printed on paper?
[[?]] Think about the four dimensions of maturity.
****
Asking which scheme is used, where it is standardised and whether it has been independently reviewed addresses cryptographic and standardisation maturity, which are the foundation for any further decision.
****

## Assessment and badge

This is the final knowledge check for the badge "Selective Disclosure and Privacy-Preserving Proofs (Knowledge, L4)", alignment code ICSF-SECP-L4-K.

**Task:** answer all 10 questions. Each question has four options and one correct answer. Read the explanation after each question, whether you answer correctly or not.

**Evidence submitted for the badge:** passed knowledge check.

**Pass rule:** 8 of 10 questions correct (80 per cent). You can retake the check. Passing shows that you understand the concepts in this course. It does not prove competency in a job.

**Rubric**

| Criterion | Questions | Evidence of understanding | Not yet |
|---|---|---|---|
| Explains selective disclosure techniques (Outcome 1) | 1 to 3 | Describes how salted hashes keep a signature valid, what the salt does and what the technique does not control | Treats selective disclosure as deletion of data or as control over what verifiers do later |
| Compares formats by privacy properties (Outcome 2) | 4 to 8 | Separates format from protocol, names what repeats across presentations, distinguishes linkability from anonymity and names measures that reduce linking | Treats all formats as equal or assumes a format alone guarantees privacy |
| Describes what zero-knowledge proofs add and how mature they are (Outcome 3) | 9 and 10 | Names predicate proofs and fresh unlinkable proofs, and gives a cautious statement of maturity | Treats zero-knowledge proofs as settled and complete, or as irrelevant |

**Question 1.** What does the issuer sign in a salted hash selective disclosure credential?

[( )] The claims in readable form, so the verifier can read them without the holder.
[(X)] A list of hashes of the salted claims.
[( )] The holder's choices for each verifier.
[( )] Only the salts.
[[?]] The signature must stay valid when claims are hidden.
****
The issuer signs the list of hashes. The holder later reveals chosen claims with their salts, and the verifier matches them against the signed list.
****

**Question 2.** Why does each claim get its own random salt?

[( )] To shorten the credential.
[( )] To allow the verifier to read hidden claims later.
[(X)] To stop a verifier from guessing hidden values by hashing likely candidates.
[( )] To prove which wallet created the credential.
[[?]] Consider a claim such as a grade, which has few possible values.
****
Without a salt, a verifier could hash each likely value and compare it with the fingerprint. A random salt makes this guessing impractical.
****

**Question 3.** Which statement about selective disclosure is correct?

[( )] It guarantees that a verifier deletes the data it receives.
[( )] It makes every presentation anonymous.
[(X)] It limits what is sent, but not what the verifier stores or does with it afterwards.
[( )] It makes the issuer signature different at each presentation.
[[?]] Think about the point at which the technique stops working.
****
Selective disclosure reduces what is revealed in a presentation. Storage, reuse and deletion by the verifier need legal, policy and audit controls.
****

**Question 4.** What is the difference between a credential format and a protocol?

[( )] A format moves credentials and a protocol describes their content.
[( )] They are the same.
[(X)] A format describes what a credential contains and how it is signed, and a protocol describes how it is issued or presented.
[( )] A protocol is used only for paper credentials.
[[?]] One answers "what is it?" and the other "how does it travel?".
****
SD-JWT VC and ISO mdoc are formats. The OpenID4VC family and the proximity presentation protocol in ISO/IEC 18013-5 describe how credentials are issued and presented.
****

**Question 5.** Which pair of formats both support selective disclosure through hashed data signed by the issuer?

[( )] Paper certificates and scanned images.
[( )] Plain PDF files and plain text files.
[(X)] SD-JWT VC and ISO mdoc.
[( )] Neither of them.
[[?]] Both are named for the EUDI Wallet.
****
SD-JWT VC hashes salted claims, and ISO mdoc hashes data elements. In both cases the issuer signs the hashes and the holder releases chosen items.
****

**Question 6.** A university issues one reusable credential per graduate in a salted hash format. What is the main remaining privacy concern?

[( )] Graduates cannot hide any claim.
[( )] The credential reveals all salts.
[(X)] The repeated issuer signature can act as a stable identifier across verifiers.
[( )] The credential cannot be verified.
[[?]] What stays the same at every presentation?
****
Even with selective disclosure, the signature and issuer data repeat when a credential is reused. Verifiers who compare notes can recognise it.
****

**Question 7.** Which statement correctly separates unlinkability from anonymity?

[( )] Unlinkability means hiding the holder's name; anonymity means hiding the issuer's name.
[(X)] Unlinkability prevents presentations from being tied together; anonymity means the person cannot be identified at all.
[( )] They both mean that the verifier receives no claims.
[( )] Anonymity is guaranteed by every wallet.
[[?]] A presentation can include a name and still be unlinkable to others.
****
A presentation that shows a name is not anonymous, yet it can be unlinkable to other presentations if the cryptographic values differ.
****

**Question 8.** Which measure reduces linking by giving the wallet many separately signed copies of the same credential, each used once?

[( )] Longer validity periods.
[( )] A single shared salt for all claims.
[(X)] Batch issuance of single-use credentials.
[( )] Asking the verifier to contact the issuer at every check.
[[?]] Each copy is used only once.
****
Batch issuance lets verifiers see different signature values, so they cannot connect presentations by signature. It adds operational effort for the issuer and the wallet.
****

**Question 9.** What could a zero-knowledge predicate proof add to a credential system?

[( )] The ability to change claims after issue.
[(X)] Proof of a statement such as "over 18" without revealing the birth date.
[( )] Automatic deletion of data at the verifier.
[( )] Removal of the issuer's signature.
[[?]] The verifier learns only that the statement is true.
****
A predicate proof convinces the verifier that a statement about a value holds, without showing the value itself.
****

**Question 10.** Which description of the maturity of zero-knowledge proofs in wallet credentials is the most careful?

[( )] They are fully settled in every wallet profile.
[( )] They have no place in credential systems.
[(X)] They are well studied in research, while standardisation, tooling and operations are still developing, so they should be checked against current texts and treated as a direction to plan for.
[( )] They have replaced selective disclosure everywhere.
[[?]] The status of the topic in this course is Emerging.
****
Research is advanced, but standards, implementations and operational experience in wallet credentials are still developing. A careful decision maker plans for the direction and uses selective disclosure and careful issuing practice today.
****

<details><summary>Facilitator notes</summary>

**Delivery:** if the course runs inside a cohort, set a date for the knowledge check and offer a 30-minute question session beforehand. Collect unanswered questions from the module sticky notes and use them in this session.

**After the check:** ask participants to name one change they will make in their own organisation. Avoid framing the badge as proof of job competency. It records that the person passed a knowledge check at ICSF stage K.

</details>

## Sources and further reading

Status as of November 2026; check before publishing.

The sources below are official texts, standards bodies and framework owners. Search for them by title on the owner's website, and check that you are reading the current version.

- **Regulation (EU) 2024/1183** of the European Parliament and of the Council, amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework (known as eIDAS 2.0). Published in the Official Journal of the European Union. Available through EUR-Lex.
- **The European Digital Identity Wallet Architecture and Reference Framework (ARF).** Published by the European Commission and the eIDAS expert group. The framework changes between versions, so use the current one.
- **Regulation (EU) 2016/679** of the European Parliament and of the Council (General Data Protection Regulation). Available through EUR-Lex. Read the principle of data minimisation and the rules on purpose limitation.
- **ISO/IEC 18013-5**, Personal identification, ISO-compliant driving licence, Part 5: Mobile driving licence (mDL) application. Published by the International Organization for Standardization. This is the source for the mdoc format and proximity presentation.
- **SD-JWT and SD-JWT VC specifications.** Developed in the Internet Engineering Task Force (IETF) OAuth working group. Check the current status of the documents on the IETF website.
- **OpenID4VC specifications** (OpenID for Verifiable Credential Issuance and OpenID for Verifiable Presentations). Published by the OpenID Foundation. Check the current versions on the OpenID Foundation website.
- **Verifiable Credentials Data Model and Data Integrity specifications.** Published by the World Wide Web Consortium (W3C). Check which versions are current and which have reached Recommendation status.
- **ICoBC Credentialing Skills Framework (ICSF).** Published by the International Council on Badges and Credentials. Skill SECP "Security, privacy and data protection", level L4 "Assure", stage K "Knowledge".
- **ICB-F06 Digital Identity and the EUDI Wallet: Essentials.** The prerequisite course in the ICoBC Kursbibliothek.

**Time-sensitive facts used in this course**

- Member States must offer at least one wallet by 24 December 2026.
- Germany plans its state wallet ('d-you') for 2 January 2027, with basic functions first.
- Regulated private sectors must accept the wallet about one year after issuance starts.
- Readiness varies widely between Member States.

Status as of November 2026; check before publishing.

<!-- VERIFY: confirm all dates and the German plan against current official announcements before publishing. -->
