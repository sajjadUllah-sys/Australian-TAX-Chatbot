"""
Pre-processed knowledge base from the Australian R&D Tax Incentive Handbook.
All content chunked and ready for RAG retrieval.
"""

HANDBOOK_CHUNKS = [
    {
        "id": "intro_overview",
        "title": "Overview of the R&D Tax Incentive",
        "content": """The Australian R&D Tax Incentive (RDTI) is the Commonwealth Government's primary mechanism for stimulating private-sector innovation. Introduced in 2011, the program replaced the former R&D Tax Concession with a more targeted and accessible offset system.

Its policy objectives are to:
- Encourage companies to undertake research that leads to new knowledge or improved technologies.
- Reduce financial barriers for high-risk experiments.
- Support a globally competitive, innovation-driven economy.

The RDTI rewards companies that invest in new knowledge. Beyond tax savings, registration demonstrates technical credibility to investors, helps embed structured innovation practices, and signals a capacity for measurable experimentation.

Companies that consistently claim R&D offsets tend to: build better internal documentation systems, foster iterative development and testing, and secure funding earlier due to improved audit readiness."""
    },
    {
        "id": "legislation",
        "title": "Key Legislation",
        "content": """The R&D Tax Incentive framework is governed by two principal Acts:

1. Industry Research and Development Act 1986 — empowers AusIndustry (on behalf of the Department of Industry, Science and Resources) to register and assess eligible R&D activities.

2. Income Tax Assessment Act 1997 (Division 355) — administered by the Australian Taxation Office (ATO), which determines allowable expenditure and calculates the tax offset.

Together, these Acts bridge scientific eligibility and taxation compliance. AusIndustry verifies that a company is conducting eligible activities, while the ATO verifies that eligible expenditure relates directly to those activities.

Additional references:
- R&D Tax Incentive Rules 2011 — further detail on registration deadlines and administrative procedures.
- AusIndustry Program Guidelines (latest release) — practical interpretation of R&D tests.
- ATO R&D Tax Incentive Instructions (NAT 73794) — covers the R&D schedule included with the company tax return.
- Public Rulings / Taxation Determinations (e.g., TD 2019/12) — specify treatment of feedstock, apportionment, and connected-entity scenarios."""
    },
    {
        "id": "misunderstandings",
        "title": "Common Misunderstandings About R&D",
        "content": """Many businesses mistake product development or process improvement for R&D automatically. The distinguishing factor is technical uncertainty — whether you could know the results in advance based on publicly available knowledge. If not, it may qualify as R&D under Australian law.

Common misunderstandings:
- Routine software development is NOT R&D just because it is complex or difficult.
- Product development is not automatically R&D — there must be technical uncertainty.
- Process improvements are only R&D if outcomes could not be known in advance.
- R&D requires technical uncertainty, not mere project risk or difficulty.
- Every project must have a defined hypothesis and systematic experimentation."""
    },
    {
        "id": "core_supporting_activities",
        "title": "Core and Supporting R&D Activities",
        "content": """A project may include two categories of activity:

CORE R&D ACTIVITIES: Systematic experiments to generate new knowledge — e.g., formulating hypotheses, testing unknown outcomes, evaluating data.

SUPPORTING R&D ACTIVITIES: Tasks directly connected to and necessary for the core R&D — e.g., design of test rigs, data analysis, or prototype fabrication for experimentation (but not for sale).

Every project should clearly show how each supporting activity leads back to its corresponding core activity. Failing to demonstrate this link is a common source of ineligibility.

A supporting R&D activity is eligible if it is directly related to a core activity or produces goods or services solely for the core R&D ("dominant purpose test").

Examples of supporting activities:
- Calibrating equipment used only in an experiment
- Preparing specialised software to run a scientific model
- Collecting data required for analysis of a core hypothesis"""
    },
    {
        "id": "three_limb_test",
        "title": "The Three-Limb Test for Core R&D Activities",
        "content": """To classify an activity as core R&D, confirm all three limbs below are satisfied:

1. NEW KNOWLEDGE OBJECTIVE – The activity aims to generate new knowledge (products, processes, materials, devices, or services).

2. SYSTEMATIC EXPERIMENTATION – The work follows a scientific method-like process: form a hypothesis, design and conduct experiments, observe results, reach conclusions, and adjust.

3. TECHNICAL UNCERTAINTY – The result could not reasonably be known or determined in advance based on current knowledge or publicly available information.

Key definitions:
- Hypothesis: The predictive statement tested through experimentation.
- Experimentation: Controlled actions designed to test one or more variables under observation.
- Technical Uncertainty: The inability to know outcomes in advance using existing knowledge or experience.
- Supporting Activity Linkage: Clear dependency where a task could not occur independently of the experiment."""
    },
    {
        "id": "excluded_activities",
        "title": "Excluded Activities",
        "content": """Certain activities are legislatively excluded regardless of novelty or effort. Common exclusions include:

- Market research, sales promotion, or consumer testing
- Routine data collection or quality assurance
- Mineral exploration and prospecting
- Management, administration, and legal tasks
- Cosmetic or stylistic design improvements only
- Cost of product certification, ISO or FDA type approvals
- Ordinary coding, debugging, or code review (software)
- User-interface or aesthetic design (software)
- System migration or version upgrades (software)
- Implementing known techniques using standard tools (software)
- Scaling up a proven process with no further uncertainty (manufacturing)
- Routine quality checks (manufacturing)
- Adjusting specifications merely for customer preference (manufacturing)
- Re-tooling production lines for cost efficiency only (manufacturing)
- Phase III or post-marketing trials aimed purely at regulatory approval (health)
- Manufacturing scale-up beyond research quantities (health)
- Routine stability or compliance testing (health)
- Commercial field demonstrations or marketing trials (agriculture)
- Comparative tastings or packaging tests (agriculture)
- Routine quality or chemical analysis (agriculture)

Keeping these exclusions in mind early prevents significant compliance risk."""
    },
    {
        "id": "eligible_entities",
        "title": "Eligible Entities",
        "content": """Only Australian incorporated companies and certain public research bodies may claim the R&D Tax Incentive benefit.

ELIGIBLE entities include:
- Proprietary limited (Pty Ltd) companies
- Public companies limited by shares or guarantee
- Corporate trustees acting for a trust that incurs R&D expenditure

INELIGIBLE entities (cannot claim directly):
- Partnerships
- Sole traders
- Unincorporated joint ventures
- Trusts

Note: Ineligible entities can contribute to a corporate entity's project, but cannot claim directly.

Regulatory Bodies:
- AusIndustry: Assess activity eligibility. Documents needed: Registration form, technical project descriptions, supporting evidence.
- ATO: Assess expenditure and issue tax determinations. Documents needed: R&D Tax Incentive Schedule, corporate tax return, financial records."""
    },
    {
        "id": "benefits_offset",
        "title": "Overview of Benefits and Offset Structure",
        "content": """The R&D Tax Incentive program provides a tax offset, not a deduction.

For FY 2024 (onward):
- Companies with turnover UNDER $20 million: Refundable offset — approximately 18.5 percentage points above corporate tax rate → potential cash refund
- Companies with turnover $20 MILLION OR MORE: Non-refundable offset — approximately 8.5 percentage points above corporate tax rate → tax liability reduction

CASH FLOW ADVANTAGES:
For startups and pre-revenue companies, the refundable portion means the ATO may pay a cash refund even if no taxable income exists. This funding stream is often reinvested to extend product development cycles without diluting equity.

STRATEGIC BENEFIT FOR ESTABLISHED FIRMS:
Claimants gain by reducing overall tax liability, improving innovation ROI and non-diluted funding without security. Large organizations also use R&D registration as an internal governance tool to track experimentation across teams.

WORKED EXAMPLE:
A software firm spending $500,000 on developing a novel encryption algorithm records a net R&D expenditure of $450,000 after adjustments. At a 43.5% refundable offset, it may receive a cash refund of approximately $195,750. Without RDTI, the same firm would receive no tax benefit if pre-revenue.

VALUE BEYOND TAX:
- Promotes investor confidence through validated innovation
- Provides benchmarking data for continuous improvement
- Facilitates collaborations with research institutions
- Non-diluted funding without any security"""
    },
    {
        "id": "interaction_other_programs",
        "title": "Interaction with Other Programs",
        "content": """While firms can leverage complementary grants (e.g., Cooperative Research Centres, Accelerating Commercialisation), double-dipping on the same expenditure is prohibited. Careful reconciliation ensures compliance.

Record-Keeping Requirements:
Companies must account for the nexus between expenditure and activity. The ATO may request documentation proving:
- How costs were incurred wholly or mainly for R&D purposes.
- Evidence such as timesheets, invoices, lab notes, or experiment designs.
- Ensure that expenditure claimed reconciles to the company's Profit & Loss."""
    },
    {
        "id": "eligible_expenditure",
        "title": "Eligible Expenditure Categories",
        "content": """Expenditure can only be claimed if it is incurred on R&D activities and the nexus is clear between cost and experiment. The ATO requires claimants to substantiate cost origin, amount, and direct connection to registered activities.

COMMONLY ELIGIBLE CATEGORIES:

1. Employee Expenditure
   - Examples: Salary, wages, superannuation for staff conducting R&D tasks.
   - Key Documentation: Contemporaneous timesheets, HR contracts, activity logs.

2. Contractor Costs
   - Examples: Payments to consultants, engineers, or labs performing experiments.
   - Key Documentation: Invoices, statements of work, engagement letters.

3. Materials
   - Examples: Items consumed or transformed during experimentation.
   - Key Documentation: Purchase orders, lab consumption records.

4. Overheads/Utilities
   - Examples: Reasonably apportioned electricity, rent, etc., relevant to R&D space.
   - Key Documentation: Cost allocation schedule.

5. Depreciation
   - Examples: Decline in value of experimental equipment.
   - Key Documentation: Asset register, usage records."""
    },
    {
        "id": "cost_apportionment",
        "title": "Apportionment, Cost Allocation and Feedstock Rule",
        "content": """APPORTIONMENT AND COST ALLOCATION:
When staff or facilities are partly used for commercial tasks, apply a reasonable apportionment method:
- Time-based approach: Allocate labour by R&D vs non-R&D hours.
- Usage-based approach: Allocate power, rent, or machinery depreciation based on R&D usage ratio.
Consistent apportionment methodology across all projects supports audit credibility.

FEEDSTOCK RULE:
If materials used in R&D also create outputs sold commercially, only the net cost (input minus sales proceeds) is claimable. This prevents double benefit from cost and income recognition.

NON-ELIGIBLE COSTS:
- Patents, trademarks, and intellectual property registration
- Capital construction (buildings, large plant)
- Interest, lease, or finance expenses
- Marketing, distribution, or after-sales activities

DOCUMENTATION STANDARDS:
Support every cost with:
1. Invoice/evidence of expenditure
2. Proof of payment
3. Demonstration of R&D nexus

The ATO often denies claims where costs are lump-sum or not clearly tied to experiment-specific activities. Invoices must show a direct nexus to the R&D activity/project — terms like "Provision of Professional services" would not be accepted.

ILLUSTRATIVE EXAMPLE:
A biotech firm purchases laboratory chemicals for assays. Half are consumed in controlled assays (R&D); half used in product stability tests (commercial QA). Only the R&D portion — supported by lab logs and consumption sheets — can be included."""
    },
    {
        "id": "group_structures",
        "title": "Group Structures and R&D",
        "content": """Modern businesses often undertake R&D through multi-entity groups or collaborative partnerships. In these structures, eligibility hinges on which entity bears the financial risk and owns or controls the experimental results.

KEY TESTS FOR GROUP ELIGIBILITY:
1. Incurrence Test: The entity claiming must actually incur the expenditure (i.e., have a legal obligation to pay).
2. R&D Ownership: The entity must own, control, or have rights to results arising from the R&D.
3. Onshore Requirement: Activities must occur in Australia unless an AusIndustry overseas finding is obtained (rare and tightly limited).

ASSOCIATED ENTITY SCENARIOS:
- Parent company funds R&D conducted by a subsidiary → Subsidiary is the claiming entity (if it performs experiments, bears cost and owns IP). Audit focus: Intercompany funding agreements.
- Australian company outsources to foreign lab → Australian company claims if overseas finding approved. Audit focus: Documentation of necessity and approval.
- Joint venture partners collaborate on R&D → Each partner claims for its own expenditure. Audit focus: Evidence of shared-risk arrangements.

CONNECTED AND AFFILIATE RELATIONSHIPS:
The ATO applies "connected entity" and "affiliate" definitions to determine aggregated turnover and offset rate eligibility. Consolidated accounts may alter whether a firm qualifies for refundable status (< $20 million turnover). Transparency in group reporting avoids later clawbacks.

INTRA-GROUP DOCUMENTATION ESSENTIALS:
- Intercompany agreements outlining project ownership, deliverables, and cost recovery.
- Clear accounting entries showing which entity incurred expenditure.
- Evidence of cash flows matching contractual obligations.
- Evidence of payment and/or mutual obligations over loan accounts.

SPECIAL CASE - CORPORATE TRUSTEES:
Where a corporate trustee incurs R&D expenditure on behalf of a trust, the trust beneficiary company is not automatically eligible. The trustee company itself must satisfy the incurrence and control tests. Professional tax advice is vital here."""
    },
    {
        "id": "pre_registration_planning",
        "title": "Pre-Registration Planning",
        "content": """Most errors in R&D Tax Incentive claims occur not during submission — but during the planning and documentation stage. The most successful claimants treat compliance as part of project management, not as an after-the-fact exercise.

DEFINE R&D AT PROJECT COMMENCEMENT:
Embed eligibility analysis into the innovation process:
- At project initiation, identify the technical uncertainties being investigated.
- Assign whether each activity is "core," "supporting," or excluded.
- Schedule documentation tasks alongside technical milestones.

CHECKLIST:
✅ Defined hypothesis and measurable objective
✅ Project plan includes time and budget for experimentation
✅ Responsible technical lead named
✅ Record-keeping tool selected

R&D GOVERNANCE FRAMEWORK:
Create internal R&D policies detailing how new projects are assessed and approved:
- Criteria for determining eligibility
- Required approvals before registration
- Procedures for updating project status and closing experiments
- Responsibility matrix linking technical, accounting, and compliance staff

STAKEHOLDER ROLES:
- Technical Team: Design and conduct experiments, maintain logs.
- Finance Team: Track and apportion costs, ensure invoices are coded correctly.
- R&D Manager / Compliance Officer: Coordinate eligibility assessment, ensure timely registration.

TECHNOLOGY READINESS VS RESEARCH STAGE:
Carefully separate experimental R&D (unknown outcomes) from commercial productization. Many claims fail because routine engineering enhancements are included. Use the Technology Readiness Level (TRL) approach to determine whether you are still investigating or simply scaling up.

ENGAGING ADVISORS EARLY:
Grants specialists can review project technology/structure and ensure expenditure tracking systems align with RDTI requirements before costs are incurred. Pre-year-end diagnostic reviews save time compared to retroactive reconstructions."""
    },
    {
        "id": "record_keeping",
        "title": "Record Keeping Best Practices",
        "content": """AusIndustry and ATO assessments rely heavily on contemporaneous evidence. Without it, projects may technically qualify but still be denied. Documents must show that experimentation occurred and what was learned.

DOCUMENTATION FRAMEWORK — FOUR EVIDENCE CATEGORIES:
1. Experimental: Test plans, design sketches, lab notebooks, annotated code repositories.
2. Analytical: Data sets, testing results, comparison tables, statistical outputs.
3. Financial: Invoices, payroll records, timesheets, cost allocation summaries.
4. Management: Project proposals, minutes of R&D meetings, progress reports.

CONTEMPORANEOUS VS RETROSPECTIVE:
Regulators value documents created during experimentation. Retrospective write-ups are acceptable only if they can be supported by dated underlying records. A timestamped digital trail (emails, commits, lab instrument logs) strengthens credibility.

DIGITAL TOOLS:
- Project tracking: Jira, Trello, Monday.com
- Version control: Git, Bitbucket
- Data storage: cloud folders with access control and date logging

COMMON DOCUMENTATION GAPS:
- Missing or generic hypotheses ("to improve performance")
- No evidence of failed tests (must show attempts and outcomes, not just success)
- Timesheets not linked to experiment phases
- Financial coding inconsistent with technical project names
- Invoices without sufficient description to show nexus to R&D project and activities

RETENTION RULES:
Maintain all supporting documents for at least five years after lodging the claim. Archived data should remain retrievable even if staff leave the company.

AUDIT-READY FILE STRUCTURE:
R&D_Projects/
  Project_A_Composite Materials/
    01_Planning/
    02_Experimental_Designs/
    03_Results/
    04_Finance_Records/
    05_Reports/"""
    },
    {
        "id": "registration_process",
        "title": "The Registration Process (AusIndustry)",
        "content": """TIMING:
Registration must occur within 10 months after the company's financial year-end. For a 30 June balance date, the deadline is 30 April of the following year.

ACCESSING THE PORTAL:
Registration is completed online via the R&D Tax Incentive Customer Portal on business.gov.au through myGovID and Relationship Authorisation Manager (RAM).

INFORMATION REQUIRED:
1. Company and project details
2. Project period (start & end dates)
3. Description of activities — core and supporting, written to meet eligibility tests
4. Expenditure summary
5. Declaration and authorisation

WRITING EFFECTIVE TECHNICAL DESCRIPTIONS:
The most challenging part is articulating core activity summaries (up to 2000 characters each). Follow this four-part structure:
- Objective: What was the technical aim or hypothesis?
- Knowledge Gaps: Why wasn't the solution known in advance? Cite prior art, research, or literature gaps.
- Experimental Activities: Describe tests, trials, or prototypes systematically.
- Outcomes and Learnings: Summarize what knowledge was gained, irrespective of success or failure.

Avoid: marketing slogans, commercial justifications, or business impact commentary — focus on the technical problem and experimentation.

SINGLE VS MULTIPLE PROJECTS:
If activities differ fundamentally (e.g., distinct hypotheses or technologies), register separate projects. Bundling unrelated work risks rejection for "project inappropriately defined."

REVIEW AND CONFIRMATION:
After submission, AusIndustry issues a reference number confirming registration. Maintain internal acknowledgement and linked documents in your R&D audit file."""
    },
    {
        "id": "ato_claim",
        "title": "The Claim Process (ATO)",
        "content": """FROM REGISTRATION TO TAX RETURN:
AusIndustry registration is prerequisite but not the claim itself. You claim the offset by lodging the R&D Tax Incentive Schedule alongside the company income tax return.

KEY COMPONENTS OF THE ATO SCHEDULE:
- Expenditure Items: salaries, contractors, materials, depreciation, overheads, etc.
- Feedstock Adjustments: if applicable.
- Aggregated Turnover: determines offset type (refundable vs non-refundable).
- Registration Number: must match the Project IDs from AusIndustry.

ALIGNING WITH ACCOUNTING RECORDS:
Ensure the claim matches the company's ledger and statutory accounts. The ATO will examine:
- Whether total R&D expenses reconcile with profit and loss.
- Consistency between narrative descriptions and financial allocations.
- Evidence of payment (cash-basis recognition required).

CALCULATION EXAMPLE:
- Payroll R&D staff: $220,000
- Contractors: $80,000
- Consumables: $20,000
- Overheads (apportioned): $10,000
- Total Eligible: $330,000
- Refundable Offset @ 43.5%: $143,550

JOINT AUSINDUSTRY-ATO COMPLIANCE:
The two agencies exchange data electronically. If AusIndustry finds activities ineligible, the ATO will automatically adjust or disallow the corresponding expenditure. A coherent and accurate description in both submissions is vital.

CLAIM REVIEW PERIODS:
The ATO may issue reviews up to four years after lodgement. Having all project documentation archived together makes responding straightforward and inexpensive.

IMPORTANT TIMEFRAMES:
- R&D Year: Financial year of the company.
- Registration Deadline: 10 months after year end (e.g., 30 April for a 30 June balance date).
- Record Retention: Minimum of 5 years.
- Potential review: Up to 4 years after lodgement."""
    },
    {
        "id": "compliance_pitfalls",
        "title": "Top 10 Compliance Pitfalls",
        "content": """Even technically excellent R&D projects can fail under audit when documentation, wording, or cost treatment breaches legislative requirements. Most compliance failures are preventable with early planning and disciplined reporting.

TOP TEN R&D COMPLIANCE PITFALLS:

1. No clear hypothesis or experiment plan
   - Typical Cause: Activities described in commercial terms (e.g., "to improve user satisfaction")
   - Prevention: Re-frame objectives into technical uncertainties and test plans.

2. Inadequate documentation
   - Typical Cause: Record-keeping commenced after year end
   - Prevention: Document experiments contemporaneously; timestamp data.

3. Unlinked supporting activities
   - Typical Cause: Work (e.g., market analysis) claimed without direct experimental connection
   - Prevention: Provide narrative linking each supporting activity to its core experiment.

4. Expenditure overclaim
   - Typical Cause: Including non-R&D time or full overheads
   - Prevention: Use time sheets, usage logs, and fair apportionment calculations.

5. Duplicated claim across entities
   - Typical Cause: Parent & subsidiary both claim same cost
   - Prevention: Define one incurring entity and intercompany funding agreement.

6. Inconsistent descriptions
   - Typical Cause: AusIndustry vs ATO forms not aligned
   - Prevention: Cross-check project wording and expenditure totals before lodgement.

7. Staff turnover
   - Typical Cause: Loss of technical knowledge and evidence
   - Prevention: Capture data centrally, not on personal devices.

8. Missed deadlines
   - Typical Cause: Registration filed after 10-month limit
   - Prevention: Set compliance calendar reminders.

9. Overseas activities without ruling
   - Typical Cause: Testing performed offshore without advance approval
   - Prevention: Apply for Overseas Finding before year-end if essential.

10. Feedstock misinterpretation
    - Typical Cause: Claiming costs for goods later sold
    - Prevention: Deduct feedstock revenue before lodging.

ROOT CAUSES OF FAILURE:
- Treating the R&D claim as purely a tax exercise rather than a technical one.
- Delegating full responsibility to accounting teams without technical oversight.
- Poor internal communication between engineering and finance functions.

CONSEQUENCES OF NON-COMPLIANCE:
- Adjustment or claw-back of disallowed credits
- Penalties and interest for false or misleading claims
- Negative precedent affecting subsequent year registrations"""
    },
    {
        "id": "audit_process",
        "title": "Review and Audit Process",
        "content": """TYPES OF REGULATOR REVIEWS:
1. AusIndustry Activity Review: Ensures activities meet definitions of "core" or "supporting" R&D.
2. ATO Expenditure Review: Verifies financial accuracy and nexus to activities.
3. Joint Review: Conducted collaboratively where issues overlap.

TRIGGERS FOR REVIEW:
- Random selection (routine sampling)
- Discrepancies between financial data and registered activities
- Unusually large claims relative to turnover
- Industry-specific risk factors (e.g., software and agriculture historically high audit rates)

AUDIT WORKFLOW OVERVIEW:
- Week 0: Notification Letter from AusIndustry/ATO — inform applicant of review scope.
- Weeks 1-4: Information Request — provide technical and financial evidence.
- Weeks 4-8: Interviews / Q&A — clarify experimental process and expenditure linkages.
- Weeks 8-12: Preliminary Findings — draft review report issued.
- Weeks 12-14: Response Period — submit explanations / additional data.
- 6 months: Final Finding — Eligible / Ineligible decision.
- 2 months: Objection or Review — Independent Review.

PREPARING FOR A REVIEW:
- Keep a master file for each project including technical logs, expenditure workpapers, and correspondence.
- Nominate an internal R&D officer as audit liaison.
- Maintain a timeline of key events (experiment start/end, prototypes).

RESPONDING TO REGULATOR QUERIES:
- Answer factually and concisely.
- Supply requested evidence in organised folders.
- Never reconstruct or embellish experiments; provide what actually exists.
- Ask for clarification if a query appears ambiguous before replying.

POSSIBLE OUTCOMES:
1. All eligible → claim stands.
2. Partially eligible → offset adjusted, refund recalculated.
3. Ineligible → expenditure disallowed; may trigger penalty.

LESSONS FROM PAST AUDITS:
- Clear hypotheses and documented failures impress reviewers more than broad success claims.
- The presence of a designated R&D manager demonstrates maturity and lowers risk scores.
- Cumulative evidence (emails, progress reports, photos) outweighs polished end-of-year summaries."""
    },
    {
        "id": "case_studies",
        "title": "Case Studies: Audit Outcomes",
        "content": """CASE STUDY 1 – SOFTWARE START-UP: DOCUMENTATION PITFALLS
Scenario: A tech company developed a machine-learning algorithm and claimed $1.2 million in R&D.
Issues Identified:
- "Core R&D activity" description lacked clear experiment detail.
- Only Jira sprint summaries existed — no explicit hypothesis or test results.
Regulator Outcome: AusIndustry disallowed the project for failing the systematic experimentation test.
Lessons:
- Convert agile sprint goals to scientific experiments ("Does model X improve accuracy > Y% under condition Z?").
- Export version-control metrics and results logs contemporaneously.

CASE STUDY 2 – MANUFACTURING COMPANY: CLEAR BOUNDARIES PAY OFF
Scenario: A metals manufacturer trialled new heat-treatment parameters for lightweight alloy components. Separate pilot-run data were maintained.
Evidence Provided: Experiment plans, temperature cycle logs, tensile strength results, cost codes dedicated to test batches.
Outcome: AusIndustry accepted all activities; ATO validated overhead apportionment at 80% accuracy.
Lessons:
- Install distinct cost codes for pilot experiments.
- Maintain engineering reports showing uncertainties addressed.

CASE STUDY 3 – AGRICULTURAL BUSINESS: PARTIAL ELIGIBILITY
Scenario: An agribusiness conducted commercial crop trials while also testing new irrigation algorithms.
Findings: Core R&D verified for algorithm trials only; general crop trials deemed normal production. Claim reduced by 40%.
Lessons:
- Separate R&D plots or test groups from production acreage.
- Record the decision matrix proving uncertainty existed in the R&D subset only.

CROSS-CASE INSIGHTS:
1. Strong, dated evidence always outweighs narrative alone.
2. Every audit hinges on proving uncertainty → experiment → knowledge gained.
3. Avoid over-aggregation: register distinct projects rather than bundling many activities under one title.
4. Staff education delivers exponential compliance improvement — frontline engineers who understand what "R&D eligibility" means produce better evidence naturally."""
    },
    {
        "id": "software_ict",
        "title": "Software and ICT Industry-Specific Guidance",
        "content": """The software sector is one of the most active — and closely scrutinised — R&D Tax Incentive categories. Rapid iteration, agile processes, and intangible results make documentation and eligibility framing critical.

TYPICAL ELIGIBLE R&D ACTIVITIES (SOFTWARE):
- Development of new algorithms or data-processing techniques.
- Research into artificial-intelligence models requiring experimental tuning.
- Creation of novel software architectures or integration methods where outcomes were uncertain.
- Security or cryptography innovations.

COMMONLY EXCLUDED ACTIVITIES (SOFTWARE):
- Ordinary coding, debugging, or code review.
- User-interface or aesthetic design.
- System migration or version upgrades.
- Implementing known techniques using standard tools.

RULE OF THUMB: R&D requires technical uncertainty, not mere project risk or "difficulty."

DOCUMENTATION BEST PRACTICES (SOFTWARE):
- Use development tickets to capture hypotheses ("Can model X reduce latency below Yms?").
- Save benchmark scripts, test data, and results from each iteration.
- Link developer timesheets to sprint numbers tied to R&D projects.
- Join version-control commits with the AusIndustry project name.

EXAMPLE - ALGORITHMIC OPTIMIZATION:
A fintech firm investigates if an adaptive caching algorithm can improve transaction authorization speed by 30%.
- Core activity: controlled simulations adjusting cache-size parameters.
- Supporting activity: building test environment and monitoring tools.
- Outcome: new algorithmic method validated — eligible R&D.

AUDIT INSIGHT:
Claims will likely be disallowed where firms describe activities commercially ("enhancing customer experience") instead of technically ("determining if algorithm A outperforms B under constraint C"). Language precision = eligibility confidence."""
    },
    {
        "id": "manufacturing",
        "title": "Manufacturing and Engineering Industry-Specific Guidance",
        "content": """Manufacturing involves continuous innovation but not every modification qualifies. Distinction between experimental processes and routine production is central.

ELIGIBLE EXAMPLES (MANUFACTURING):
- Designing and trialling new materials or composites.
- Prototype fabrication for testing mechanical or chemical properties.
- Process-parameter optimisation where behaviour is scientifically uncertain.
- Integration of automated control systems requiring experimental calibration.

EXCLUDED OR PARTIALLY ELIGIBLE (MANUFACTURING):
- Scaling up a proven process with no further uncertainty.
- Routine quality checks.
- Adjusting specifications merely for customer preference.
- Re-tooling production lines for cost efficiency only.

EVIDENCE CHECKLIST (MANUFACTURING):
✅ Design drawings and technical specifications of prototypes
✅ Test-run logs and sensor data
✅ Failed trials — showing genuine experimentation
✅ Materials traceability records distinguish R&D batches from commercial output

EXAMPLE - ADVANCED MATERIALS TESTING:
A metal-fabrication company explores a new titanium alloy to achieve higher fatigue resistance.
- Test coupons of varying thickness are statistically tested.
- Each batch logged and analysed to verify mechanical properties.
- Commercial production not commenced until successful prototype proven.
- Result: Core R&D accepted; production setup costs excluded.

AUDIT EXPERIENCE:
Companies that segregate R&D trial runs with separate lot numbers or cost centres demonstrate compliance decisively. Clear separation between "experiments" and "production" protects entire claims."""
    },
    {
        "id": "agriculture",
        "title": "Agriculture and Food Processing Industry-Specific Guidance",
        "content": """Agricultural development often contains experimental design — but routine agronomic trials generally fail the R&D test unless scientifically structured and addressing unknown mechanics.

TYPICAL ELIGIBLE ACTIVITIES (AGRICULTURE):
- Controlled crop-trials comparing novel variables (e.g., fertiliser composition, irrigation pattern).
- Development of new genetic strains or bio-control methods.
- Engineering of precision-agriculture systems or software algorithms.
- Development of new food-processing techniques (e.g., enzyme-based extraction, low-temperature drying).

COMMON EXCLUSION EXAMPLES (AGRICULTURE):
- Commercial field demonstrations or marketing trials.
- Comparative tastings or packaging tests.
- Routine quality or chemical analysis.

DOCUMENTATION ESSENTIALS (AGRICULTURE):
- Experimental design protocols (randomised trial layouts, sample sizes).
- Environmental data (weather logs, sensor readings).
- Analytical reports from labs.
- Photographic evidence of field layouts and measurement devices.

EXAMPLE - IRRIGATION ALGORITHM TRIAL:
An agriculture business tests AI controlled irrigation system to achieve optimal soil moisture.
- Core activity: experimental algorithm development and field validation.
- Supporting: sensor calibration, data capture, statistical analysis.
- Outcome: data supports predictive model, confirming eligibility.

COMPLIANCE CONSIDERATIONS:
- Keep R&D plots physically separate from commercial acreage.
- Retain maps and data tagging each test block.
- Document "unknowns" – e.g., weather effect on soil conductivity – to demonstrate technical uncertainty."""
    },
    {
        "id": "health_biotech",
        "title": "Health, Biotechnology, and Pharmaceuticals Industry-Specific Guidance",
        "content": """Health-related R&D is typically robustly eligible because it naturally relies on experimental science. However, heavy regulatory layers create nuance between scientific experimentation and routine verification.

COMMON ELIGIBLE ACTIVITIES (HEALTH/BIOTECH):
- Laboratory experiments on biological or chemical entities.
- Creation and screening of new drug compounds or medical devices.
- Pre-clinical animal testing and in vitro research.
- Clinical Phase I and early Phase II trials (testing safety and efficacy).

TYPICALLY NON-ELIGIBLE (HEALTH/BIOTECH):
- Phase III or post-marketing trials aimed purely at regulatory approval.
- Manufacturing scale-up beyond research quantities.
- Routine stability or compliance testing.

DOCUMENTATION FOCUS (HEALTH/BIOTECH):
- Experimental plans (protocols, control groups, data sets).
- Ethics and Human Research Committee approvals.
- Laboratory notebooks / electronic lab journals (ELNs).
- Detailed statistical and analytical method records.

EXAMPLE - NEW DRUG FORMULATION:
A biotech firm develops a nanoparticle-based drug-delivery system to target specific cells.
- Core R&D: design and characterisation of compound nano-carriers.
- Supporting: synthesis of test batches, microscopy, comparative efficacy tests.
- Excluded: scaling up for commercial manufacture post Phase II.
- Outcome: Regulators validated eligibility for pharma R&D stages 1 & 2; later compliance / manufacturing excluded.

PARTNERING AND IP OWNERSHIP:
Where companies collaborate with universities or hospitals, confirm contractual rights to results (IP ownership or licence). Only the entity bearing risk and owning results may claim the offset.

AUDIT OBSERVATIONS:
- Regulators expect precise scientific language and structured data (including negative results).
- Companies with electronic lab notebooks prepared for audit can respond within days.
- Clear demarcation between research and regulatory testing avoids claw-backs."""
    },
    {
        "id": "strategy_integration",
        "title": "Integrating R&D with Business Strategy",
        "content": """The R&D Tax Incentive is most powerful when treated as part of an organisation's innovation strategy, not merely a financial credit. By aligning business goals with structured experimentation, companies accelerate both compliance and innovation outcomes.

BUILDING AN INNOVATION CULTURE:
- Leadership Commitment: Senior management must champion evidence-based experimentation and allocate dedicated budgets.
- Incentive Alignment: Reward teams for rigorous testing, not just launch speed.
- Education: Periodic workshops on what qualifies as R&D help engineers and accountants speak the same language.

EMBEDDING PROCESS DISCIPLINE:
Integrate R&D criteria in governance tools such as:
- Stage-gate or agile project templates with an "eligibility checkpoint."
- Internal sign-off matrices confirming technical uncertainty.
- Standard R&D hypothesis and results forms.

KEY BENEFIT: When every project automatically captures technical data, compliance documentation nearly writes itself at year-end.

TRACKING ACROSS FINANCIAL YEARS:
Projects commonly extend beyond a single tax year. Maintain a continuity log recording:
- Year-by-year progress summaries
- Changes in hypotheses or experimental design
- Cost carry-forwards

CONTINUOUS IMPROVEMENT:
Use previous reviews or audit feedback as learning opportunities. Create an internal "R&D lessons database" noting successes and gaps. Annual benchmarking helps sustain compliance excellence.

STRATEGIC OUTCOMES for organisations that embed RDTI-aligned innovation frameworks:
- Faster claim preparation.
- Higher eligibility certainty.
- Greater board-level visibility of technical achievement."""
    },
    {
        "id": "working_with_advisors",
        "title": "Working with Advisors and Specialists",
        "content": """The R&D Tax Incentive straddles two disciplines – science and tax law. Experienced Grants Specialists and some Advisors can bridge this gap, structuring claims accurately while freeing internal resources.

WHEN TO ENGAGE:
Engage early – ideally before the project starts or by mid-year – to align tracking system and confirm eligibility tests. Late engagement often forces reconstruction of records and increases risk.

TYPES OF SUPPORT PARTNERS:
- Grants Specialist: Prepare fully compliant R&D claim covering both technical and financial aspects and liaise with AusIndustry and ATO in all related matters.
- R&D Tax Consultant: Interpret legislation, only review technical narratives, prepare basic financial calculations.
- Accountant or Tax Agent: Prepare basic financial aspects of R&D claim, integrate into tax return.
- Technical Expert / Engineer: Validate scientific uncertainty language and design experiments.

MANAGING CONSULTANT ENGAGEMENTS:
- Obtain clear scope and fee agreement.
- Maintain ownership of all your source documents.
- Ensure technical staff review narratives for accuracy before submission.

COLLABORATION WORKFLOW:
1. Internal team collects evidence.
2. Consultant reviews eligibility and drafts descriptions.
3. Finance team validates costing.
4. All parties sign off jointly before lodgement.

ETHICAL AND GOVERNANCE CONSIDERATIONS:
Ensure conflicts of interest and confidentiality are addressed in contracts. R&D records often contain trade secrets; use NDAs and secure file transfer protocols.

POST-ENGAGEMENT REVIEW:
Conduct an annual evaluation of advisor performance and update standing contracts as legislation evolves."""
    },
    {
        "id": "post_claim",
        "title": "Post-Claim Obligations and Forward Planning",
        "content": """RETENTION OF RECORDS:
Both AusIndustry and ATO require records to be retained for five years from the date of lodgement. Maintain digital backups with date stamps and access logs.

INTERNAL AUDIT AND SELF-ASSESSMENT:
Annual self-audits should test samples of activities and ensure:
- Experimentation evidence remains accessible.
- Financial apportionments still reasonable.
- Project ownership and entitlements documented.
A simple internal rubric – scoring projects on documentation and traceability – helps prioritise remediation before external review.

RESPONDING TO POLICY CHANGE:
The R&D Tax Incentive is subject to regular legislative review. Stay current by monitoring official sources:
- business.gov.au/rdtaxincentive
- ATO R&D Tax Incentive web guidance
- Professional bodies (CA ANZ, CPA Australia, AusIndustry bulletins)

CONTINUOUS READINESS FOR REVIEW:
Adopt a "no-surprises" policy by keeping an up-to-date R&D master register listing projects, participants, and evidence locations.

LEVERAGING R&D DATA BEYOND TAX:
R&D records hold strategic insight. Use them to:
- Support grant applications or investor presentations.
- Benchmark innovation productivity.
- Inform future product portfolio decisions.

GOVERNANCE REPORTING:
Include R&D metrics in board dashboards: number of active projects, eligible expenditure ratio, and audit status.

END-TO-END LIFECYCLE:
1. Idea Generation — Identify technical uncertainty → Hypothesis statement.
2. Experimentation — Generate new knowledge → Data and results logs.
3. Registration — Comply with AusIndustry rules → Project narrative submission.
4. Claim Lodgement — Monetise eligible costs → ATO R&D schedule.
5. Post-Claim — Continuous audit readiness → Evidence archives + self-review."""
    },
    {
        "id": "defining_rd_project",
        "title": "Defining an R&D Project",
        "content": """For registration, activities are grouped into "projects" — a series of related experiments pursuing a common aim.

EACH PROJECT:
- Must include at least one core activity.
- May include connected supporting activities.
- Runs within a defined timeframe within the R&D year.

TIP: Construct projects at the level of experiment clusters, not entire product lines, to maintain technical precision and clear audit boundaries.

RISK ZONE INDICATORS — an activity may appear eligible yet fail audit due to:
- Lack of a defined hypothesis.
- Unclear link between experiments and claimed costs.
- Descriptions written in commercial rather than technical language.

WORKED EXAMPLE — COMPOSITE MATERIALS:
A manufacturer tests new composite materials for high-temperature resistance:
- Hypothesis: A specific carbon-silica blend can increase heat tolerance by 15%.
- Experiments: Small-scale oven tests varying mix ratios.
- Core Activity: Conducting the controlled experiments.
- Supporting Activities: Data recording, software modelling, and fabrication of small test batches for analysis only.
- Sales or large-scale manufacturing would be excluded.

COMPLIANCE HEALTH CHECK — before each lodging cycle confirm:
✅ Current-year hypotheses identified
✅ Documented evidence of experimentation
✅ Financial ledger reconciliation completed
✅ Cross-matching between AusIndustry projects and ATO schedules
✅ Submission < 10 months post year-end"""
    },
    {
        "id": "glossary",
        "title": "Glossary of Key Terms",
        "content": """KEY TERMS AND DEFINITIONS:

Activity: Work undertaken by a company as part of an R&D project.

Aggregated Turnover: Total revenue of connected and affiliated entities used to determine offset type.

AusIndustry: Commonwealth agency that administers eligibility assessment for the R&D Tax Incentive.

Core R&D Activity: An experimental activity whose outcome cannot be known in advance and is conducted to generate new knowledge.

Supporting R&D Activity: An activity directly related to, and necessary for a core activity.

Feedstock Adjustment: Requirement to subtract income from sale of goods produced during R&D activities.

Systematic Experimentation: Structured approach of hypothesis, testing, observation and evaluation.

Technical Uncertainty: Aspect of a project that cannot be resolved by existing knowledge or standard practice.

Refundable / Non-Refundable Offset: Type of tax benefit depending on aggregated turnover thresholds.

RDTI: R&D Tax Incentive — the main program name.

ATO: Australian Taxation Office — administers the tax aspects of the program.

Division 355: The section of the Income Tax Assessment Act 1997 that governs the R&D Tax Incentive.

TRL: Technology Readiness Level — a scale used to determine whether work is in the research phase or moving to commercialisation.

RAM: Relationship Authorisation Manager — used to access the AusIndustry portal.

ELN: Electronic Lab Notebook — digital record of laboratory experiments.

NDA: Non-Disclosure Agreement — used to protect trade secrets when working with advisors."""
    },
    {
        "id": "documentation_templates",
        "title": "Documentation Templates and Checklists",
        "content": """R&D PROJECT SUMMARY SHEET TEMPLATE:
- Project Title
- Objective / Hypothesis
- Technical Uncertainty
- Experimental Method
- Results / Observations
- Knowledge Gained
- Supporting Documents

R&D TIMESHEET SAMPLE FIELDS:
- Employee Name
- Week Ending
- Total Hours
- R&D Hours
- Description of Work (e.g., prototype testing)
- Authorised By

EXPENDITURE TRACKING SHEET FIELDS:
- Date
- Supplier
- Cost Type
- Amount
- R&D %
- Documentation Evidence

AUDIT EVIDENCE INDEX FIELDS:
- Evidence Type
- File Reference
- Location
- Linked Project
- Retention Period

COMPLIANCE SELF-REVIEW CHECKLIST (Key Questions):
1. Is the claimant an Australian incorporated company that incurred the eligible R&D expenditure?
2. Have all projects been assessed to ensure at least one qualifying "core R&D activity" exists?
3. Do activity descriptions clearly demonstrate systematic experimentation to resolve technical uncertainty?
4. Is each supporting activity directly related to a core activity?
5. Have excluded activities been removed from the claim?
6. Is a clear hypothesis stated and supported by evidence?
7. Are experiment plans, results and conclusions documented within the financial year?
8. Are records contemporaneous and date-stamped?
9. Has an AusIndustry registration been lodged before the 10-month deadline?
10. Do project names and descriptions match between AusIndustry form and ATO R&D schedule?
11. Have claimed costs been verified as directly linking to eligible R&D Activities?
12. Are employee and contractor hours recorded with timesheets?
13. Is any overhead apportionment method reasonable and documented?
14. Have feedstock rules been applied where R&D output was sold commercially?
15. Are all R&D files retained for at least 5 years post-lodgement?
16. Could the company produce complete support within 5 days of an ATO/AusIndustry request?
17. Has management formally approved the R&D claim and internal compliance policy?
18. Have technical and finance teams received annual training on R&D compliance requirements?"""
    }
]

def get_all_chunks():
    return HANDBOOK_CHUNKS

def get_chunk_by_id(chunk_id):
    for chunk in HANDBOOK_CHUNKS:
        if chunk["id"] == chunk_id:
            return chunk
    return None
