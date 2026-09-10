---
name: foreign-legal-ppt
description: Research and create presentation decks on foreign laws, regulations, enforcement and cross-border legal risk for Chinese management audiences. Use when a PPT requires strict source traceability, current-law verification, bilingual legal terminology, executive-level explanation, visual quality control, or a reusable personal deck profile.
---

# Foreign Legal PPT

Produce a decision-useful management presentation without weakening the underlying legal research. Treat the deck as two linked deliverables: a traceable research record and a concise visual explanation.

## Select the operating mode

- **Set up my PPT profile:** Read [references/profile-setup.md](references/profile-setup.md). Interview the user, analyze any reference deck or screenshots, produce sample pages when useful, and create a reusable local workspace outside the skill directory.
- **Create or revise a deck:** Locate and read `ppt-config.md`, then the profile, relevant calibrations, and known counterexamples it points to. If no config exists, offer to initialize one without blocking the current task.
- **Research or outline only:** Complete the research and narrative stages without generating a PPTX.

Ask only for missing facts that would materially change the legal scope, audience, confidentiality treatment, or deliverable. Infer reversible design details from the saved profile and supplied references.

## Work in phases

Split each deck into five phases and keep owners explicit. Do not let the model substitute its own judgment for the briefing answers, the structure lock, or the calibration rulings that belong to the user:

- **P0 前置约束**：使用者确认受众、决策目的、不能遗漏的问题，以及任务是一般介绍还是真实项目。AI 为页数、语言、版式、引用和交付形态提供默认建议。按 [references/upfront-briefing.md](references/upfront-briefing.md) 保存为 `brief.md`。
- **P1 检索与规则还原草稿（AI）**：按 briefing 检索，形成议题地图与来源台账；凡涉及管辖/门槛/例外归类的页面，另产"规则结构还原"草稿（对照规则定义树：全集与子集、例外、术语），供使用者裁决。
- **P2 结构梳理与确认（使用者裁决）**：首次模式下，AI 给出一套推荐叙事骨架及一套有实质差异的备选；核对模式复用既有结构，只呈现变化。确认后锁定，锁定前不做正文制作。
- **P3 制作与质检（AI）**：在锁定结构内生成、渲染、逐页检查。
- **P4 裁决点与沉淀（共同）**：交付 `review-checklist.md`（AI 已作但需律师裁决的口径/结论/建议点，未裁决项默认标注"未复核，不作决策依据"）；结论获使用者确认后，按 [references/accumulation.md](references/accumulation.md) 沉淀使用习惯与口径库。

## Establish the assignment (P0)

Complete the minimum upfront briefing before research. The user confirms the audience, decision purpose, must-not-miss issues, and whether a real matter is involved. For the remaining fields, propose defaults and record any unconfirmed assumption visibly:

- target audience and the decision or action the deck should support, including who may ask follow-up questions at the presentation;
- governing jurisdictions, the user's own business/deal connection to the subject, and relevant dates;
- the user's "must-not-miss" questions and any previously criticized coverage gaps;
- whether an existing confirmed calibration (口径库) exists for this subject, which switches the task into verify-incrementally mode;
- whether the deck is an internal working draft, training material, or external advice;
- language, page range, deadline, source cutoff, and required template;
- confidentiality, privilege, client-data, and permitted research boundaries.

Never upload confidential, privileged, personal, export-controlled, or client material to an external service unless the user has authorized that destination. Use public, fictional, de-identified, or locally accessible material by default.

Read [references/runtime-adaptation.md](references/runtime-adaptation.md) before substantive work. Confirm which capabilities are actually available in the current Agent. Do not assume that installing this Skill provides web search, access to legal databases, vision, PowerPoint generation, or slide rendering.

## Research before designing

Read and apply [references/legal-research.md](references/legal-research.md). Build an issue map and source ledger before writing substantive slides. Verify material propositions against primary sources and distinguish binding law, proposed rules, guidance, enforcement actions, allegations, decisions, and commentary.

Do not treat a search result, AI summary, law-firm alert, unofficial translation, or press report as the final authority when a controlling primary source is reasonably available. Preserve disagreements and uncertainty that could change the audience's decision.

Before approving the outline, map every material issue to a proposed slide, appendix, or explicit exclusion. A page is not complete merely because every sentence has a citation. It must address the material sides of the issue at the depth required by the assignment.

For pages that categorize scope, thresholds, exceptions, or filing obligations, draft a rule-structure reconstruction: reproduce the rule's own classification tree (full set ∪/∩ relations, each node's regulatory cite, exceptions and carve-outs, defined terms) from the primary text and compare it with the proposed wording. Flag four failure modes — missing categories, wrong axis, example treated as full set, and invented terms replacing regulatory language — and resolve them before the outline is confirmed. Check [references/accumulation.md](references/accumulation.md): if the user has a confirmed calibration entry for this subject, run verification against it instead of generating a fresh taxonomy.

## Design the management narrative

Read and apply [references/management-deck.md](references/management-deck.md). Translate the research into the audience's decision path. A default structure may cover executive conclusion, scope and triggers, process and timing, business consequences, risk scenarios, recommended actions, and sources. Change that structure when the assignment requires a different story.

In first-run mode, propose one recommended narrative skeleton and one materially different alternative, each stating the chapter order and every page's role in the decision path. In verification mode, show only justified changes to the prior structure. The user confirms the structure before it is locked (P2). Keep legal rule, factual application, risk judgment, and recommendation visibly distinct.

Each slide must have a defined job. Prefer a supported takeaway title when the evidence establishes a conclusion; use a direct topic title for definitions, process, scope, or background. When the audience may be asked follow-up questions at the presentation, also draft a short Q&A card (5–10 expected questions with answers whose wording matches the deck and cites the page-level basis).

## Choose the execution path

- **首次模式:** Use when no profile or relevant confirmed calibration exists. Run P0–P4. Ask only the minimum briefing questions, recommend sensible defaults, confirm the research scope and structure, and use a visual sample when the style is new.
- **核对模式:** Use when a relevant profile and confirmed calibration exist. Recheck current primary sources, identify factual and legal changes, reuse the prior structure when it still fits, and ask only about changed or unresolved decision points.
- **快速模式:** Use for a familiar, low-risk internal task with stable inputs, profile, and calibration. Complete the work without routine intermediate approvals, but pause when a material scope change, stale calibration, source conflict, or consequential judgment appears.

The execution path changes the number of interruptions, not the research, source, rendering, or quality standard.

Jurisdiction, threshold, and exception classification is a strong confirmation point by default: even when the user has asked for a fast path, present the classification framework and the structure lock for review, and mark the affected conclusions as "未复核，不作决策依据" in the review-checklist when no qualified reviewer is available. Locked narrative structure may not be changed mid-production without a new user confirmation.

Do not make the user approve routine implementation choices already settled by the profile. A mature workflow should reduce repeated questions over time.

## Produce the deck (P3)

Use the available presentation-generation capability and the user's template or reference deck. Keep required tables, charts, timelines, process diagrams, and source evidence editable when the environment supports it. Do not substitute decorative imagery for evidence. Stay inside the locked structure from P2; do not silently add, drop, or reorder sections.

Role boundary while producing: the model is responsible for research, rule-structure drafts, facts, sources, wording drafts, and visuals. Classification rulings, risk grades, conclusions, and recommendations are presented as drafts with their basis, and carried into the review-checklist for the user/lawyer to decide — not presented as if already decided.

Apply the saved personal profile before defaults. If none exists, use a restrained management style: light background, dark text, one controlled accent color, ample whitespace, legible bilingual typography, and limited decoration. Avoid generic courthouse columns, gavels, flags, handshakes, glowing globes, and ornamental maps unless they convey necessary information.

Put concise source markers on the relevant slide when the audience needs them. Put full citations, URLs, titles, dates, pinpoint references, translation notes, and retrieval dates in speaker notes or a source appendix. Never invent a citation.

## Validate before delivery (P3–P4)

Read and apply [references/quality-gates.md](references/quality-gates.md). Render and inspect every slide. Correct content omissions, unsupported propositions, citation mismatches, text overflow, illegible footnotes, inconsistent terminology, weak visual hierarchy, and cross-slide contradictions. Confirm the delivered deck still matches the locked structure and that any change made along the way went back through a user confirmation.

Deliver the requested PPTX plus the source ledger when legal research was performed, together with a review-checklist based on [assets/review-checklist-template.md](assets/review-checklist-template.md). Unchecked items default to "未复核，不作决策依据". Label material assumptions, unresolved issues, and the source cutoff. State that a qualified lawyer must review the work when it will support legal advice or a consequential business decision.

After the user responds to the draft, apply [references/accumulation.md](references/accumulation.md): offer to record usage habits, confirmed calibrations into the user's 口径库, and anti-pattern entries for any page the reviewer flagged. Never write unconfirmed drafts into the confirmed zone.
