# CHANGELOG

## v1.BETA.277 - 2026-06-12
### Ai
- breakdown chance is not bombard - stop the siege-line self-sabotage ([#410](https://github.com/stones2stars/S2S/issues/410))(flabbert)
- pack courage marches at field enemies, not just adjacent ones ([#409](https://github.com/stones2stars/S2S/issues/409))(flabbert)
- horde courage marches the wave and packs engage in the field ([#409](https://github.com/stones2stars/S2S/issues/409))(flabbert)
- barb horde courage - hordes force city attacks at an odds floor ([#409](https://github.com/stones2stars/S2S/issues/409))(flabbert)
- workers respect escorts and standing defense in danger reactions ([#406](https://github.com/stones2stars/S2S/issues/406))(flabbert)
- retire EVAL_MERGE_FACTOR; healer demand scales with stack HP-mass ([#395](https://github.com/stones2stars/S2S/issues/395))(flabbert)
- siege stacks merge to beat the defender ([#395](https://github.com/stones2stars/S2S/issues/395))(flabbert)
- garrison consolidation pass + overwhelmed-split retune ([#395](https://github.com/stones2stars/S2S/issues/395))(flabbert)
- demand gates read strength-weighted counts under Size Matters ([#395](https://github.com/stones2stars/S2S/issues/395))(flabbert)
- strength-weighted force ledgers - SM-aware unit accounting ([#395](https://github.com/stones2stars/S2S/issues/395))(flabbert)
- NPCs may not field invisible units until every civ can counter them(flabbert)
### Balance
- master hunter line +2 strength across the board(flabbert)
### Bug Fixes
- event publish stays one bool check while the server is off ([#407](https://github.com/stones2stars/S2S/issues/407))(flabbert)
- human missions only break when danger overwhelms the plot defense (Fixes [#406](https://github.com/stones2stars/S2S/issues/406))(flabbert)
    **Fixes [#406](https://github.com/stones2stars/S2S/issues/406)**
- C2C_World_Remixed Peaks option scaled hills instead of peaks(flabbert)
### Docs
- a verdict worthy of the gold medal(flabbert)
- the Clandestine Battering Ram takes gold at 113 cb - first over the cap(flabbert)
- owner ruling - docs-only commits go straight to main(flabbert)
- styled REALISM_INDEX.html twin (+ sibling links between the indexes)(flabbert)
- the historical ram footnote - capital equipment, not crackers(flabbert)
- ground the Battering Ram entry in what is certain(flabbert)
- the Clandestine Battering Ram - the oral-tradition siege mechanic(flabbert)
- Realism Index entry 3 - the Clandestine Battering Ram(flabbert)
- Realism Index entries 4+5 - the Grid Before the Generator, the 326 supply chains(flabbert)
- the Realism Index - sibling of the Despair Index for designed absurdities(flabbert)
- pseudo-progress terminals audit rule (owner ruling, [#410](https://github.com/stones2stars/S2S/issues/410))(flabbert)
- barb-pressure-concentrates-on-small-civs balance finding ([#408](https://github.com/stones2stars/S2S/issues/408))(flabbert)
- Size Matters AI literacy plan - owner rulings + phased scope ([#395](https://github.com/stones2stars/S2S/issues/395))(flabbert)
### Features
- human turn-phase events on the /events stream ([#407](https://github.com/stones2stars/S2S/issues/407))(flabbert)
- /events SSE turn-boundary stream on the dev HTTP server (Fixes [#407](https://github.com/stones2stars/S2S/issues/407))(flabbert)
    **Fixes [#407](https://github.com/stones2stars/S2S/issues/407)**
- AI-vs-human benchmarking scheme - collector, Benchmarks/, merge/split logging ([#387](https://github.com/stones2stars/S2S/issues/387))(flabbert)
- /players + /cities telemetry endpoints; gameId playtest identity ([#387](https://github.com/stones2stars/S2S/issues/387))(flabbert)

### All Changes
- ai: breakdown chance is not bombard - stop the siege-line self-sabotage ([#410](https://github.com/stones2stars/S2S/issues/410)) (flabbert)
- docs: a verdict worthy of the gold medal (flabbert)
- docs: the Clandestine Battering Ram takes gold at 113 cb - first over the cap (flabbert)
- docs: owner ruling - docs-only commits go straight to main (flabbert)
- docs: styled REALISM_INDEX.html twin (+ sibling links between the indexes) (flabbert)
- docs: the historical ram footnote - capital equipment, not crackers (flabbert)
- docs: ground the Battering Ram entry in what is certain (flabbert)
- ai: pack courage marches at field enemies, not just adjacent ones ([#409](https://github.com/stones2stars/S2S/issues/409)) (flabbert)
- docs: the Clandestine Battering Ram - the oral-tradition siege mechanic (flabbert)
- docs: Realism Index entry 3 - the Clandestine Battering Ram (flabbert)
- ai: horde courage marches the wave and packs engage in the field ([#409](https://github.com/stones2stars/S2S/issues/409)) (flabbert)
- docs: Realism Index entries 4+5 - the Grid Before the Generator, the 326 supply chains (flabbert)
- docs: the Realism Index - sibling of the Despair Index for designed absurdities (flabbert)
- docs: pseudo-progress terminals audit rule (owner ruling, [#410](https://github.com/stones2stars/S2S/issues/410)) (flabbert)
- balance: master hunter line +2 strength across the board (flabbert)
- ai: barb horde courage - hordes force city attacks at an odds floor ([#409](https://github.com/stones2stars/S2S/issues/409)) (flabbert)
- docs: barb-pressure-concentrates-on-small-civs balance finding ([#408](https://github.com/stones2stars/S2S/issues/408)) (flabbert)
- fix: event publish stays one bool check while the server is off ([#407](https://github.com/stones2stars/S2S/issues/407)) (flabbert)
- feat: human turn-phase events on the /events stream ([#407](https://github.com/stones2stars/S2S/issues/407)) (flabbert)
- feat: /events SSE turn-boundary stream on the dev HTTP server (Fixes [#407](https://github.com/stones2stars/S2S/issues/407)) (flabbert)
    **Fixes [#407](https://github.com/stones2stars/S2S/issues/407)**
- ai: workers respect escorts and standing defense in danger reactions ([#406](https://github.com/stones2stars/S2S/issues/406)) (flabbert)
- fix: human missions only break when danger overwhelms the plot defense (Fixes [#406](https://github.com/stones2stars/S2S/issues/406)) (flabbert)
    **Fixes [#406](https://github.com/stones2stars/S2S/issues/406)**
- ai: retire EVAL_MERGE_FACTOR; healer demand scales with stack HP-mass ([#395](https://github.com/stones2stars/S2S/issues/395)) (flabbert)
- ai: siege stacks merge to beat the defender ([#395](https://github.com/stones2stars/S2S/issues/395)) (flabbert)
- ai: garrison consolidation pass + overwhelmed-split retune ([#395](https://github.com/stones2stars/S2S/issues/395)) (flabbert)
- ai: demand gates read strength-weighted counts under Size Matters ([#395](https://github.com/stones2stars/S2S/issues/395)) (flabbert)
- ai: strength-weighted force ledgers - SM-aware unit accounting ([#395](https://github.com/stones2stars/S2S/issues/395)) (flabbert)
- docs: Size Matters AI literacy plan - owner rulings + phased scope ([#395](https://github.com/stones2stars/S2S/issues/395)) (flabbert)
- fix: C2C_World_Remixed Peaks option scaled hills instead of peaks (flabbert)
- feat: AI-vs-human benchmarking scheme - collector, Benchmarks/, merge/split logging ([#387](https://github.com/stones2stars/S2S/issues/387)) (flabbert)
- ai: NPCs may not field invisible units until every civ can counter them (flabbert)
- feat: /players + /cities telemetry endpoints; gameId playtest identity ([#387](https://github.com/stones2stars/S2S/issues/387)) (flabbert)

## v1.BETA.276 - 2026-06-11
### Ai
- wildlife sorties are harvests - odds floor instead of a ban ([#400](https://github.com/stones2stars/S2S/issues/400))(flabbert)
- garrisons stop sortieing against wildlife; chokeDefend loses the inflated anyAttack (Fixes [#400](https://github.com/stones2stars/S2S/issues/400))(flabbert)
    **Fixes [#400](https://github.com/stones2stars/S2S/issues/400)**
- property-control units commit their journeys and pool at home (Fixes [#396](https://github.com/stones2stars/S2S/issues/396))(flabbert)
    **Fixes [#396](https://github.com/stones2stars/S2S/issues/396)**
- stop hunter fallbacks stranding units in rival territory (Fixes [#392](https://github.com/stones2stars/S2S/issues/392))(flabbert)
    **Fixes [#392](https://github.com/stones2stars/S2S/issues/392)**
- city "vicinity" guarding is radius 2, not 21 tiles; recall garrison members ([#384](https://github.com/stones2stars/S2S/issues/384))(flabbert)
- demote categorically mis-typed CITY_DEFENSE units to their XML default role ([#384](https://github.com/stones2stars/S2S/issues/384))(flabbert)
- two-tier city garrison - no retype on garrisoning, retention hysteresis ([#384](https://github.com/stones2stars/S2S/issues/384))(flabbert)
- subdued/tamed animal economy -- spread the herd, disband the zoo ([#381](https://github.com/stones2stars/S2S/issues/381))(flabbert)
    **Fixes [#381](https://github.com/stones2stars/S2S/issues/381)**
- garrison sortie uses AI_leaveAttack, not the range-inflated anyAttack ([#382](https://github.com/stones2stars/S2S/issues/382))(flabbert)
    **Fixes [#382](https://github.com/stones2stars/S2S/issues/382)**
- border patrol walks only its OWN border ([#24](https://github.com/stones2stars/S2S/issues/24))(flabbert)
- ONE birthmark->direction helper; patrol fans 8 ways; mid-land heads to border ([#24](https://github.com/stones2stars/S2S/issues/24))(flabbert)
- use birthmark parity for the patrol stream split, not getID(flabbert)
- border patrol intercepts before it wanders, and patrollers split streams ([#24](https://github.com/stones2stars/S2S/issues/24))(flabbert)
    **Fixes [#24](https://github.com/stones2stars/S2S/issues/24)**
### Bug Fixes
- register AUTOMATE_SPREAD in GlobalTypes.xml ([#381](https://github.com/stones2stars/S2S/issues/381))(flabbert)
- two always-false guards -- isGameStart never true; rev NPC guard dead ([#105](https://github.com/stones2stars/S2S/issues/105), [#139](https://github.com/stones2stars/S2S/issues/139))(flabbert)
    **Fixes [#105](https://github.com/stones2stars/S2S/issues/105)**
    **Fixes [#139](https://github.com/stones2stars/S2S/issues/139)**
### Chore
- purge the FLB logger experiment (owner ruling)(flabbert)
### Docs
- explain how to get releases (GitHub dist repo or SVN)(flabbert)
- link the S2S Discord from the Despair Index(flabbert)
- despair is now measured in centiphants (cp)(flabbert)
- despair index - the owner identifies the real bug(flabbert)
- despair index entry 2 - The Library of Alexandria, Burned Nightly (95 cE)(flabbert)
- despair index HTML page + standing contribution policy(flabbert)
- The S2S Despair Index (TM)(flabbert)
- record the deferred interior-coverage limitation of border patrol(flabbert)
- release is a strict follower of main (owner ruling)(flabbert)
### Features
- /units live game-state endpoint on the dev HTTP server ([#387](https://github.com/stones2stars/S2S/issues/387))(flabbert)
- GET-only hello-world HTTP server PoC behind a logging BUG option ([#387](https://github.com/stones2stars/S2S/issues/387))(flabbert)

### All Changes
- docs: explain how to get releases (GitHub dist repo or SVN) (flabbert)
- docs: link the S2S Discord from the Despair Index (flabbert)
- Merge pull request [#401](https://github.com/stones2stars/S2S/issues/401) from Stones2Stars/feature/400-garrison-wildlife-sorties (flabbert)
    **Fixes [#400](https://github.com/stones2stars/S2S/issues/400)**
- ai: wildlife sorties are harvests - odds floor instead of a ban ([#400](https://github.com/stones2stars/S2S/issues/400)) (flabbert)
- ai: garrisons stop sortieing against wildlife; chokeDefend loses the inflated anyAttack (Fixes [#400](https://github.com/stones2stars/S2S/issues/400)) (flabbert)
    **Fixes [#400](https://github.com/stones2stars/S2S/issues/400)**
- Merge pull request [#398](https://github.com/stones2stars/S2S/issues/398) from Stones2Stars/docs/centiphants (flabbert)
- docs: despair is now measured in centiphants (cp) (flabbert)
- Merge pull request [#397](https://github.com/stones2stars/S2S/issues/397) from Stones2Stars/feature/396-property-control-stranding (flabbert)
    **Fixes [#396](https://github.com/stones2stars/S2S/issues/396)**
- docs: despair index - the owner identifies the real bug (flabbert)
- ai: property-control units commit their journeys and pool at home (Fixes [#396](https://github.com/stones2stars/S2S/issues/396)) (flabbert)
    **Fixes [#396](https://github.com/stones2stars/S2S/issues/396)**
- Merge pull request [#393](https://github.com/stones2stars/S2S/issues/393) from Stones2Stars/feature/392-hunter-stranding (flabbert)
    **Fixes [#392](https://github.com/stones2stars/S2S/issues/392)**
- Merge pull request [#394](https://github.com/stones2stars/S2S/issues/394) from Stones2Stars/docs/despair-cabv (flabbert)
- docs: despair index entry 2 - The Library of Alexandria, Burned Nightly (95 cE) (flabbert)
- ai: stop hunter fallbacks stranding units in rival territory (Fixes [#392](https://github.com/stones2stars/S2S/issues/392)) (flabbert)
    **Fixes [#392](https://github.com/stones2stars/S2S/issues/392)**
- Merge pull request [#391](https://github.com/stones2stars/S2S/issues/391) from Stones2Stars/feature/384-garrison-tiers (flabbert)
    **Fixes [#384](https://github.com/stones2stars/S2S/issues/384)**
- docs: despair index HTML page + standing contribution policy (flabbert)
- docs: The S2S Despair Index (TM) (flabbert)
- ai: city "vicinity" guarding is radius 2, not 21 tiles; recall garrison members ([#384](https://github.com/stones2stars/S2S/issues/384)) (flabbert)
- ai: demote categorically mis-typed CITY_DEFENSE units to their XML default role ([#384](https://github.com/stones2stars/S2S/issues/384)) (flabbert)
- ai: two-tier city garrison - no retype on garrisoning, retention hysteresis ([#384](https://github.com/stones2stars/S2S/issues/384)) (flabbert)
- Merge pull request [#390](https://github.com/stones2stars/S2S/issues/390) from Stones2Stars/feature/387-units-endpoint (flabbert)
- feat: /units live game-state endpoint on the dev HTTP server ([#387](https://github.com/stones2stars/S2S/issues/387)) (flabbert)
- Merge pull request [#389](https://github.com/stones2stars/S2S/issues/389) from Stones2Stars/feature/387-http-server-poc (flabbert)
- Merge pull request [#388](https://github.com/stones2stars/S2S/issues/388) from Stones2Stars/chore/purge-flb-logger (flabbert)
- feat: GET-only hello-world HTTP server PoC behind a logging BUG option ([#387](https://github.com/stones2stars/S2S/issues/387)) (flabbert)
- chore: purge the FLB logger experiment (owner ruling) (flabbert)
- Merge pull request [#385](https://github.com/stones2stars/S2S/issues/385) from Stones2Stars/fix/381-subdued-animal-economy (flabbert)
    **Fixes [#381](https://github.com/stones2stars/S2S/issues/381)**
- fix: register AUTOMATE_SPREAD in GlobalTypes.xml ([#381](https://github.com/stones2stars/S2S/issues/381)) (flabbert)
- ai: subdued/tamed animal economy -- spread the herd, disband the zoo ([#381](https://github.com/stones2stars/S2S/issues/381)) (flabbert)
    **Fixes [#381](https://github.com/stones2stars/S2S/issues/381)**
- Merge pull request [#383](https://github.com/stones2stars/S2S/issues/383) from Stones2Stars/fix/382-garrison-sortie (flabbert)
    **Fixes [#382](https://github.com/stones2stars/S2S/issues/382)**
- Merge pull request [#375](https://github.com/stones2stars/S2S/issues/375) from Stones2Stars/fix/24-border-patrol (flabbert)
    **Fixes [#24](https://github.com/stones2stars/S2S/issues/24)**
- ai: garrison sortie uses AI_leaveAttack, not the range-inflated anyAttack ([#382](https://github.com/stones2stars/S2S/issues/382)) (flabbert)
    **Fixes [#382](https://github.com/stones2stars/S2S/issues/382)**
- ai: border patrol walks only its OWN border ([#24](https://github.com/stones2stars/S2S/issues/24)) (flabbert)
- docs: record the deferred interior-coverage limitation of border patrol (flabbert)
- Merge branch 'main' into fix/24-border-patrol (flabbert)
- Merge pull request [#374](https://github.com/stones2stars/S2S/issues/374) from Stones2Stars/fix/105-139-dead-guards (flabbert)
    **Fixes [#105](https://github.com/stones2stars/S2S/issues/105)**
- ai: ONE birthmark->direction helper; patrol fans 8 ways; mid-land heads to border ([#24](https://github.com/stones2stars/S2S/issues/24)) (flabbert)
- ai: use birthmark parity for the patrol stream split, not getID (flabbert)
- ai: border patrol intercepts before it wanders, and patrollers split streams ([#24](https://github.com/stones2stars/S2S/issues/24)) (flabbert)
    **Fixes [#24](https://github.com/stones2stars/S2S/issues/24)**
- fix: two always-false guards -- isGameStart never true; rev NPC guard dead ([#105](https://github.com/stones2stars/S2S/issues/105), [#139](https://github.com/stones2stars/S2S/issues/139)) (flabbert)
    **Fixes [#105](https://github.com/stones2stars/S2S/issues/105)**
    **Fixes [#139](https://github.com/stones2stars/S2S/issues/139)**
- Merge pull request [#373](https://github.com/stones2stars/S2S/issues/373) from Stones2Stars/docs/release-branch-convention (flabbert)
- docs: release is a strict follower of main (owner ruling) (flabbert)

## v1.BETA.275 - 2026-06-11
### Ai
- **cityAI:** fix inverted human commerce-emphasis weighting ([#68](https://github.com/stones2stars/S2S/issues/68))(flabbert)
    **Fixes [#68](https://github.com/stones2stars/S2S/issues/68)**
- **cityAI:** fix three valuation bugs in AI_getBuildingYieldValue ([#66](https://github.com/stones2stars/S2S/issues/66))(flabbert)
    **Fixes [#66](https://github.com/stones2stars/S2S/issues/66)**
### Bug Fixes
- drop the per-plot assert in CvPlot::disableGraphicsPaging(flabbert)
- art tag must merge before the base copy (Improvement)(flabbert)
- art tag must merge before the base copy (Bonus/Feature/Terrain)(flabbert)
- **loader:** unset load-order stamp means NOT loaded -- delayed resolution required(flabbert)
### Ci
- temporarily build only the release branch in AppVeyor(flabbert)
### City
- specialist yields receive the city yield modifier like worked tiles ([#317](https://github.com/stones2stars/S2S/issues/317))(flabbert)
### Docs
- record the parity ruling -- excluding specialists from modifiers was a mistake(flabbert)
- record the emphasis-as-city-need-signal ruling ([#367](https://github.com/stones2stars/S2S/issues/367))(flabbert)
- dead-code pass -- 2026-06-11 candidate-generation results(flabbert)
- frame-span findings + the garrison-churn investigation log(flabbert)
- record the 2026-06-10 turn-time cycle and re-rank the levers(flabbert)
- new git rule - verify the current branch immediately before every commit(flabbert)
- AGENTS.md is the single home for rules; CLAUDE.md stays a bootstrap shim(flabbert)
- PR-state git rule + CLAUDE.md bootstrap so repo docs load every session(flabbert)
### Performance Improvements
- frame-span instrumentation -- the doTurn tree missed ~70s/turn of unit AI(flabbert)
- gate + loop-invert resource consumption (its only consumer is optional depletion)(flabbert)

### All Changes
- Merge pull request [#371](https://github.com/stones2stars/S2S/issues/371) from Stones2Stars/docs/emphasis-city-needs-ruling (flabbert)
- Merge pull request [#372](https://github.com/stones2stars/S2S/issues/372) from Stones2Stars/fix/317-specialist-yield-parity (flabbert)
- docs: record the parity ruling -- excluding specialists from modifiers was a mistake (flabbert)
- city: specialist yields receive the city yield modifier like worked tiles ([#317](https://github.com/stones2stars/S2S/issues/317)) (flabbert)
- docs: record the emphasis-as-city-need-signal ruling ([#367](https://github.com/stones2stars/S2S/issues/367)) (flabbert)
- Merge pull request [#366](https://github.com/stones2stars/S2S/issues/366) from Stones2Stars/fix/68-commerce-emphasis-weighting (flabbert)
    **Fixes [#68](https://github.com/stones2stars/S2S/issues/68)**
- **cityAI:** fix inverted human commerce-emphasis weighting ([#68](https://github.com/stones2stars/S2S/issues/68)) (flabbert)
    **Fixes [#68](https://github.com/stones2stars/S2S/issues/68)**
- Merge pull request [#361](https://github.com/stones2stars/S2S/issues/361) from Stones2Stars/fix/66-building-yield-value (flabbert)
    **Fixes [#66](https://github.com/stones2stars/S2S/issues/66)**
- Merge branch 'main' into fix/66-building-yield-value (flabbert)
- Merge pull request [#365](https://github.com/stones2stars/S2S/issues/365) from Stones2Stars/fix/plot-paging-assert-spam (flabbert)
- Merge pull request [#351](https://github.com/stones2stars/S2S/issues/351) from Stones2Stars/data/196-partial-adopters (flabbert)
- Merge pull request [#350](https://github.com/stones2stars/S2S/issues/350) from Stones2Stars/data/196-big-standalone (flabbert)
- Merge pull request [#349](https://github.com/stones2stars/S2S/issues/349) from Stones2Stars/data/196-events (flabbert)
- Merge pull request [#348](https://github.com/stones2stars/S2S/issues/348) from Stones2Stars/data/196-society-systems (flabbert)
- Merge pull request [#347](https://github.com/stones2stars/S2S/issues/347) from Stones2Stars/data/196-world-setup (flabbert)
- Merge pull request [#346](https://github.com/stones2stars/S2S/issues/346) from Stones2Stars/data/196-gameplay-small (flabbert)
- Merge pull request [#345](https://github.com/stones2stars/S2S/issues/345) from Stones2Stars/data/196-graphics-ui (flabbert)
- Merge pull request [#344](https://github.com/stones2stars/S2S/issues/344) from Stones2Stars/data/196-art-family (flabbert)
- fix: drop the per-plot assert in CvPlot::disableGraphicsPaging (flabbert)
- fix: art tag must merge before the base copy (Improvement) (flabbert)
- fix: art tag must merge before the base copy (Bonus/Feature/Terrain) (flabbert)
- **loader:** unset load-order stamp means NOT loaded -- delayed resolution required (flabbert)
- **cityAI:** fix three valuation bugs in AI_getBuildingYieldValue ([#66](https://github.com/stones2stars/S2S/issues/66)) (flabbert)
    **Fixes [#66](https://github.com/stones2stars/S2S/issues/66)**
- Merge pull request [#360](https://github.com/stones2stars/S2S/issues/360) from Stones2Stars/docs/dead-code-pass-findings (flabbert)
- docs: dead-code pass -- 2026-06-11 candidate-generation results (flabbert)
- [#196](https://github.com/stones2stars/S2S/issues/196): complete the five partial adopters (Building/Unit/Promotion/Trait/Improvement) (flabbert)
- [#196](https://github.com/stones2stars/S2S/issues/196): migrate LeaderHead, Civic, UnitCombat to declarative loading (flabbert)
- [#196](https://github.com/stones2stars/S2S/issues/196): migrate CvEventInfo + CvEventTriggerInfo to declarative loading (flabbert)
- [#196](https://github.com/stones2stars/S2S/issues/196): migrate society/system info classes to declarative loading (flabbert)
- [#196](https://github.com/stones2stars/S2S/issues/196): migrate world/setup info classes to declarative loading (flabbert)
- [#196](https://github.com/stones2stars/S2S/issues/196): migrate small gameplay/options info classes to declarative loading (flabbert)
- [#196](https://github.com/stones2stars/S2S/issues/196): migrate graphics/UI info classes to declarative getDataMembers loading (flabbert)
- [#196](https://github.com/stones2stars/S2S/issues/196): migrate the art-info family to declarative getDataMembers loading (flabbert)
- Merge pull request [#343](https://github.com/stones2stars/S2S/issues/343) from Stones2Stars/ci/appveyor-release-only (flabbert)
- ci: temporarily build only the release branch in AppVeyor (flabbert)
- Merge pull request [#342](https://github.com/stones2stars/S2S/issues/342) from Stones2Stars/perf/frame-span-unit-ai-churn (flabbert)
- docs: frame-span findings + the garrison-churn investigation log (flabbert)
- perf+ai: fix the garrison re-decide churn (and two gameplay bugs it concealed) (flabbert)
- perf: frame-span instrumentation -- the doTurn tree missed ~70s/turn of unit AI (flabbert)
- perf: gate + loop-invert resource consumption (its only consumer is optional depletion) (flabbert)
- Merge pull request [#340](https://github.com/stones2stars/S2S/issues/340) from Stones2Stars/perf/turn-time-repository-pilot (flabbert)
- docs: record the 2026-06-10 turn-time cycle and re-rank the levers (flabbert)
- perf+arch: repository skeleton v2, spin guard, choose instrumentation, value retention, scoring index fix (flabbert)
- Merge pull request [#338](https://github.com/stones2stars/S2S/issues/338) from Stones2Stars/chore/196-gamespeed-simplification (flabbert)
- docs: new git rule - verify the current branch immediately before every commit (flabbert)
- [#248](https://github.com/stones2stars/S2S/issues/248): derive turn counts & calendar from era data; delete GameTurnInfos tables (flabbert)
- [#248](https://github.com/stones2stars/S2S/issues/248): GameSpeed/Handicap Percents maps -> named fields; tag-dispatched Adapt grammar (flabbert)
- Merge pull request [#335](https://github.com/stones2stars/S2S/issues/335) from Stones2Stars/chore/310-worldinfo-citylimits-percent (flabbert)
- [#310](https://github.com/stones2stars/S2S/issues/310): migrate CvWorldInfo to declarative loading; Percents map -> iCityLimitsScalePercent (flabbert)
- Merge pull request [#334](https://github.com/stones2stars/S2S/issues/334) from Stones2Stars/feature/infoutil-char-array-and-enum-as-int (flabbert)
- docs: AGENTS.md is the single home for rules; CLAUDE.md stays a bootstrap shim (flabbert)
- docs: PR-state git rule + CLAUDE.md bootstrap so repo docs load every session (flabbert)
- Merge pull request [#332](https://github.com/stones2stars/S2S/issues/332) from Stones2Stars/chore/196-declarative-info-loading-tier2 (flabbert)
- demote CvPlot::changeVisibilityCount negative-cap assert to gated [ENG/viscap] log (flabbert)
- [#196](https://github.com/stones2stars/S2S/issues/196): document declarative info loading in Sources/docs/reference (flabbert)
- [#196](https://github.com/stones2stars/S2S/issues/196): migrate CvMapInfo and CvGoodyInfo (Tier-2) (flabbert)
    **Closes [#249](https://github.com/stones2stars/S2S/issues/249)**
    **Closes [#265](https://github.com/stones2stars/S2S/issues/265)**
- [#196](https://github.com/stones2stars/S2S/issues/196): migrate 7 Tier-2 info classes using the new wrappers (flabbert)
    **Closes [#258](https://github.com/stones2stars/S2S/issues/258)**
    **Closes [#259](https://github.com/stones2stars/S2S/issues/259)**
    **Closes [#272](https://github.com/stones2stars/S2S/issues/272)**
    **Closes [#280](https://github.com/stones2stars/S2S/issues/280)**
    **Closes [#282](https://github.com/stones2stars/S2S/issues/282)**
    **Closes [#290](https://github.com/stones2stars/S2S/issues/290)**
    **Closes [#306](https://github.com/stones2stars/S2S/issues/306)**

## v1.BETA.261 - 2026-06-10
### Map
- mark zone-rework plan paused after A-soft (resume point = A-hard)(flabbert)
- soft-disable inherited multimap + add zone-rework plan(flabbert)
- proactive graphics-paging eviction (PAGING_RESIDENT_SOFT_CAP)(flabbert)
- guard null/dummy entity in CvDLLEntity remove/destroy (fixes map-switch CTD)(flabbert)

### All Changes
- Merge pull request [#331](https://github.com/stones2stars/S2S/issues/331) from Stones2Stars/feature/infoutil-char-array-and-enum-as-int (flabbert)
- Merge pull request [#330](https://github.com/stones2stars/S2S/issues/330) from Stones2Stars/chore/196-declarative-info-loading-tier1 (flabbert)
- [#196](https://github.com/stones2stars/S2S/issues/196): add char-array and enum-as-int wrappers to CvInfoUtil (flabbert)
- [#196](https://github.com/stones2stars/S2S/issues/196): migrate 10 more Tier-1 info classes to declarative getDataMembers (flabbert)
    **Closes [#224](https://github.com/stones2stars/S2S/issues/224)**
    **Closes [#234](https://github.com/stones2stars/S2S/issues/234)**
    **Closes [#239](https://github.com/stones2stars/S2S/issues/239)**
    **Closes [#256](https://github.com/stones2stars/S2S/issues/256)**
    **Closes [#267](https://github.com/stones2stars/S2S/issues/267)**
    **Closes [#274](https://github.com/stones2stars/S2S/issues/274)**
    **Closes [#285](https://github.com/stones2stars/S2S/issues/285)**
    **Closes [#286](https://github.com/stones2stars/S2S/issues/286)**
    **Closes [#299](https://github.com/stones2stars/S2S/issues/299)**
    **Closes [#305](https://github.com/stones2stars/S2S/issues/305)**
- [#196](https://github.com/stones2stars/S2S/issues/196): migrate 8 simple info classes to declarative getDataMembers (flabbert)
    **Closes [#216](https://github.com/stones2stars/S2S/issues/216)**
    **Closes [#226](https://github.com/stones2stars/S2S/issues/226)**
    **Closes [#229](https://github.com/stones2stars/S2S/issues/229)**
    **Closes [#246](https://github.com/stones2stars/S2S/issues/246)**
    **Closes [#250](https://github.com/stones2stars/S2S/issues/250)**
    **Closes [#254](https://github.com/stones2stars/S2S/issues/254)**
    **Closes [#262](https://github.com/stones2stars/S2S/issues/262)**
    **Closes [#283](https://github.com/stones2stars/S2S/issues/283)**
- Merge pull request [#329](https://github.com/stones2stars/S2S/issues/329) from Stones2Stars/fix/325-building-requires-build-vs-operate (flabbert)
    **Fix [#325](https://github.com/stones2stars/S2S/issues/325)**
- Fix [#325](https://github.com/stones2stars/S2S/issues/325): distinguish build vs operate requirements in building help (flabbert)
    **Fix [#325](https://github.com/stones2stars/S2S/issues/325)**
- Merge pull request [#327](https://github.com/stones2stars/S2S/issues/327) from Stones2Stars/map/multimap-soft-disable (flabbert)
- Merge pull request [#328](https://github.com/stones2stars/S2S/issues/328) from Stones2Stars/core/324-minidump-month (flabbert)
    **Fix [#324](https://github.com/stones2stars/S2S/issues/324)**
- Fix [#324](https://github.com/stones2stars/S2S/issues/324): minidump filename month off-by-one (tm_mon + 1) (flabbert)
    **Fix [#324](https://github.com/stones2stars/S2S/issues/324)**
- Map: mark zone-rework plan paused after A-soft (resume point = A-hard) (flabbert)
- Map: soft-disable inherited multimap + add zone-rework plan (flabbert)
- Map: proactive graphics-paging eviction (PAGING_RESIDENT_SOFT_CAP) (flabbert)
- Map: guard null/dummy entity in CvDLLEntity remove/destroy (fixes map-switch CTD) (flabbert)

## v1.BETA.249 - 2026-06-09

### All Changes
- Merge pull request [#323](https://github.com/stones2stars/S2S/issues/323) from Stones2Stars/map/40-space-map-latitude (flabbert)
- Map [#40](https://github.com/stones2stars/S2S/issues/40): derive latitude from the Earth band on space maps (flabbert)

## v1.BETA.246 - 2026-06-09
### Docs
- link Phase 3b followup issues ([#319](https://github.com/stones2stars/S2S/issues/319) stack, [#320](https://github.com/stones2stars/S2S/issues/320) tooltip); note calibration is ongoing(flabbert)
- Phase 3b foundation FinalRelease-playtested; balance is followup scope(flabbert)
- **AGENTS:** nothing here is ever a one-liner — read core docs + trace consumers first(flabbert)

### All Changes
- Merge pull request [#322](https://github.com/stones2stars/S2S/issues/322) from Stones2Stars/combat/320-modifier-breakdown (flabbert)
- **AGENTS:** nothing here is ever a one-liner — read core docs + trace consumers first (flabbert)
- Combat [#320](https://github.com/stones2stars/S2S/issues/320): re-add itemised strength-modifier breakdown via CombatPreview.detailLines (flabbert)
- Merge pull request [#321](https://github.com/stones2stars/S2S/issues/321) from Stones2Stars/combat/319-attackodds-winpct-gate (flabbert)
- docs([#319](https://github.com/stones2stars/S2S/issues/319)): frame aggression tuning as ongoing calibration folded into per-leader work, not a tracked task (flabbert)
- Combat [#319](https://github.com/stones2stars/S2S/issues/319): gate stack attack go/no-go on lead-attacker win%, not goodness (flabbert)
- Merge pull request [#318](https://github.com/stones2stars/S2S/issues/318) from Stones2Stars/combat/phase3b-and-aco-cleanup (flabbert)
- docs: link Phase 3b followup issues ([#319](https://github.com/stones2stars/S2S/issues/319) stack, [#320](https://github.com/stones2stars/S2S/issues/320) tooltip); note calibration is ongoing (flabbert)
- docs: Phase 3b foundation FinalRelease-playtested; balance is followup scope (flabbert)
- Remove dead Advanced Combat Odds (ACO) BUG-options surface (flabbert)
- Phase 3b: route AI attack odds through the binomial engine (flabbert)

## v1.BETA.235 - 2026-06-08
### Docs
- reference note for constructibility/prereq system + [PERF/reqmodel] tag + FASSERT/FinalRelease fact ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2)(flabbert)
- **plans:** record help-text clusters 3 + documented exceptions ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2)(flabbert)
- **plans:** record status-aware renderer + cluster 2 ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2)(flabbert)
- **plans:** record help-text migration cluster 1 ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2)(flabbert)
### Refactor
- **prereq:** model-driven InCity-buildings + civic requirement help ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2)(flabbert)
- **prereq:** status-aware model requirement renderer + building/bonus clusters ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2)(flabbert)
- **prereq:** FinalRelease-visible model-fidelity logging, not asserts ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2)(flabbert)
- **prereq:** model-driven vicinity requirement help text ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2)(flabbert)
- **prereq:** complete building requirement-model GOM coverage ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2)(flabbert)
- **prereq:** unit train-requirement model + index migration ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2)(flabbert)
- **prereq:** unified construction-requirement model ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2)(flabbert)

### All Changes
- Merge pull request [#315](https://github.com/stones2stars/S2S/issues/315) from Stones2Stars/refactor/195-phase2-unified-prereq-model (flabbert)
- docs: reference note for constructibility/prereq system + [PERF/reqmodel] tag + FASSERT/FinalRelease fact ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2) (flabbert)
- **plans:** record help-text clusters 3 + documented exceptions ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2) (flabbert)
- **prereq:** model-driven InCity-buildings + civic requirement help ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2) (flabbert)
- **plans:** record status-aware renderer + cluster 2 ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2) (flabbert)
- **prereq:** status-aware model requirement renderer + building/bonus clusters ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2) (flabbert)
- **prereq:** FinalRelease-visible model-fidelity logging, not asserts ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2) (flabbert)
- **plans:** record help-text migration cluster 1 ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2) (flabbert)
- **prereq:** model-driven vicinity requirement help text ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2) (flabbert)
- **prereq:** complete building requirement-model GOM coverage ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2) (flabbert)
- **prereq:** unit train-requirement model + index migration ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2) (flabbert)
- **prereq:** unified construction-requirement model ([#195](https://github.com/stones2stars/S2S/issues/195) Phase 2) (flabbert)

## v1.BETA.222 - 2026-06-08
### Docs
- mirror sea-AI + bug-hunt knowledge into the repo; mandate in-repo docs(flabbert)
- **agents:** hard rule — never read .vcxproj for build facts (they're dead)(flabbert)
- **plans:** AI architecture north-star — unifying frame for the AI/data rework(flabbert)
- **sea-ai:** link the AI_refreshExploreRange spin root cause to issue [#189](https://github.com/stones2stars/S2S/issues/189)(flabbert)
### Features
- building->improvement yield bonuses + AI worker stranded-city fixes(flabbert)
### Performance Improvements
- **cabv:** static enabler reverse-index for constructibility ([#195](https://github.com/stones2stars/S2S/issues/195))(flabbert)
- **cityAI:** memoize building constructible-set + derived-data repository foundation(flabbert)
- **instrumentation:** CvGame::doTurn phase scopes + cabvset diag + creep tool(flabbert)
### Refactor
- **xml-loading:** declarative loading foundation, bool-list flattening, dead-code removal(flabbert)
    **Fixes [#194](https://github.com/stones2stars/S2S/issues/194)**

### All Changes
- Merge pull request [#314](https://github.com/stones2stars/S2S/issues/314) from Stones2Stars/perf/195-constructibility-enabler-index (flabbert)
- **cabv:** static enabler reverse-index for constructibility ([#195](https://github.com/stones2stars/S2S/issues/195)) (flabbert)
- Merge pull request [#313](https://github.com/stones2stars/S2S/issues/313) from Stones2Stars/refactor/declarative-xml-loading (flabbert)
- **xml-loading:** declarative loading foundation, bool-list flattening, dead-code removal (flabbert)
    **Fixes [#194](https://github.com/stones2stars/S2S/issues/194)**
- **plans:** AI architecture north-star — unifying frame for the AI/data rework (flabbert)
- Merge pull request [#193](https://github.com/stones2stars/S2S/issues/193) from Stones2Stars/perf/turn-instrumentation-and-creep-tool (flabbert)
- **agents:** hard rule — never read .vcxproj for build facts (they're dead) (flabbert)
- **instrumentation:** CvGame::doTurn phase scopes + cabvset diag + creep tool (flabbert)
- Merge pull request [#192](https://github.com/stones2stars/S2S/issues/192) from Stones2Stars/perf/cabv-memoization-and-repo-foundation (flabbert)
- **cityAI:** memoize building constructible-set + derived-data repository foundation (flabbert)
- Merge pull request [#190](https://github.com/stones2stars/S2S/issues/190) from Stones2Stars/feat/building-improvement-yields-and-worker-stranded-fixes (flabbert)
- feat: building->improvement yield bonuses + AI worker stranded-city fixes (flabbert)
- Merge pull request [#188](https://github.com/stones2stars/S2S/issues/188) from Stones2Stars/fix/auto-hunt-sea-leaves-borders (flabbert)
- **sea-ai:** link the AI_refreshExploreRange spin root cause to issue [#189](https://github.com/stones2stars/S2S/issues/189) (flabbert)
- seaExplore hysteresis + docs; detectSpin; [HAI] taxonomy; git-workflow rule ([#187](https://github.com/stones2stars/S2S/issues/187)) (flabbert)
    **Fixes [#187](https://github.com/stones2stars/S2S/issues/187)**
- edits to auto sea hunt (flabbert)
- Auto-hunt sea units leave borders to engage and explore (autoHuntMove) (flabbert)
- Merge pull request [#183](https://github.com/stones2stars/S2S/issues/183) from Stones2Stars/docs/mirror-knowledge-and-sea-ai (flabbert)
- docs: mirror sea-AI + bug-hunt knowledge into the repo; mandate in-repo docs (flabbert)
- Merge pull request [#182](https://github.com/stones2stars/S2S/issues/182) from Stones2Stars/feature/sea-attack-relax-and-logging (flabbert)
- Merge pull request [#181](https://github.com/stones2stars/S2S/issues/181) from Stones2Stars/fix/lowprio-engine-guards (flabbert)
- Merge pull request [#180](https://github.com/stones2stars/S2S/issues/180) from Stones2Stars/fix/lowprio-88-attackodds-bwin (flabbert)
- Merge pull request [#179](https://github.com/stones2stars/S2S/issues/179) from Stones2Stars/fix/lowprio-cvgame (flabbert)
- Merge pull request [#178](https://github.com/stones2stars/S2S/issues/178) from Stones2Stars/fix/lowprio-cvcity (flabbert)
- Sea AI: let attack-sea pursue enemies beyond own waters + log the sea cascade (flabbert)
- Low-priority engine guards: UAF, independent wrap, vassal arg, project cost, null capital ([#78](https://github.com/stones2stars/S2S/issues/78), [#95](https://github.com/stones2stars/S2S/issues/95), [#92](https://github.com/stones2stars/S2S/issues/92), [#108](https://github.com/stones2stars/S2S/issues/108), [#133](https://github.com/stones2stars/S2S/issues/133)) (flabbert)
    **Fixes [#78](https://github.com/stones2stars/S2S/issues/78)**
    **Fixes [#92](https://github.com/stones2stars/S2S/issues/92)**
    **Fixes [#95](https://github.com/stones2stars/S2S/issues/95)**
    **Fixes [#108](https://github.com/stones2stars/S2S/issues/108)**
    **Fixes [#133](https://github.com/stones2stars/S2S/issues/133)**
- Write *bWin in the no-attacker branch of AI_attackOdds; init caller ([#88](https://github.com/stones2stars/S2S/issues/88)) (flabbert)
    **Fixes [#88](https://github.com/stones2stars/S2S/issues/88)**
- Guard divide-by-zero / NaN in flexible difficulty and win-for-losing ([#102](https://github.com/stones2stars/S2S/issues/102), [#103](https://github.com/stones2stars/S2S/issues/103)) (flabbert)
    **Fixes [#102](https://github.com/stones2stars/S2S/issues/102)**
    **Fixes [#103](https://github.com/stones2stars/S2S/issues/103)**
- Low-priority CvCity fixes: health diff out-params, culture-timer assert, dead loop ([#59](https://github.com/stones2stars/S2S/issues/59), [#60](https://github.com/stones2stars/S2S/issues/60), [#64](https://github.com/stones2stars/S2S/issues/64)) (flabbert)
    **Fixes [#59](https://github.com/stones2stars/S2S/issues/59)**
    **Fixes [#60](https://github.com/stones2stars/S2S/issues/60)**
    **Fixes [#64](https://github.com/stones2stars/S2S/issues/64)**

## v1.BETA.192 - 2026-06-05

### All Changes
- Merge pull request [#176](https://github.com/stones2stars/S2S/issues/176) from Stones2Stars/fix/153-conquest-occupation-anarchy (flabbert)
- Merge pull request [#174](https://github.com/stones2stars/S2S/issues/174) from Stones2Stars/fix/agent-89-chooseelection (flabbert)
- Merge pull request [#173](https://github.com/stones2stars/S2S/issues/173) from Stones2Stars/fix/agent-tier3-cvplayerai (flabbert)
- Merge pull request [#172](https://github.com/stones2stars/S2S/issues/172) from Stones2Stars/fix/agent-tier3-cvplayer (flabbert)
- Merge pull request [#171](https://github.com/stones2stars/S2S/issues/171) from Stones2Stars/fix/agent-tier3-selgroup (flabbert)
- Merge pull request [#170](https://github.com/stones2stars/S2S/issues/170) from Stones2Stars/fix/agent-tier3-cvplot (flabbert)
- Cut conquest occupation anarchy to ~1/5 ([#153](https://github.com/stones2stars/S2S/issues/153)) (flabbert)
- Merge pull request [#169](https://github.com/stones2stars/S2S/issues/169) from Stones2Stars/fix/agent-97-research-cost (flabbert)
- Merge pull request [#175](https://github.com/stones2stars/S2S/issues/175) from Stones2Stars/docs/dead-code-xml-pass-plan (flabbert)
- Add plan for the dead-code / dead-XML removal pass (flabbert)
- Merge pull request [#167](https://github.com/stones2stars/S2S/issues/167) from Stones2Stars/fix/agent-tier2-cvplayer (flabbert)
- Merge pull request [#168](https://github.com/stones2stars/S2S/issues/168) from Stones2Stars/fix/agent-99-corp-hq (flabbert)
- Fix shadowed vote and wrong vote-outcome index in AI_chooseElection ([#89](https://github.com/stones2stars/S2S/issues/89)) (flabbert)
    **Fixes [#89](https://github.com/stones2stars/S2S/issues/89)**
- Tier-3 AI decision fixes in CvPlayerAI ([#121](https://github.com/stones2stars/S2S/issues/121), [#124](https://github.com/stones2stars/S2S/issues/124), [#128](https://github.com/stones2stars/S2S/issues/128), [#129](https://github.com/stones2stars/S2S/issues/129), [#132](https://github.com/stones2stars/S2S/issues/132)) (flabbert)
    **Fixes [#121](https://github.com/stones2stars/S2S/issues/121)**
    **Fixes [#124](https://github.com/stones2stars/S2S/issues/124)**
    **Fixes [#128](https://github.com/stones2stars/S2S/issues/128)**
    **Fixes [#129](https://github.com/stones2stars/S2S/issues/129)**
    **Fixes [#132](https://github.com/stones2stars/S2S/issues/132)**
- Tier-3 fixes in CvPlayer: corp trigger validity and resolution master skip ([#113](https://github.com/stones2stars/S2S/issues/113), [#120](https://github.com/stones2stars/S2S/issues/120)) (flabbert)
    **Fixes [#113](https://github.com/stones2stars/S2S/issues/113)**
    **Fixes [#120](https://github.com/stones2stars/S2S/issues/120)**
- Tier-3 fixes in CvSelectionGroup: shadow-unit pairing and pillage tiering ([#86](https://github.com/stones2stars/S2S/issues/86), [#87](https://github.com/stones2stars/S2S/issues/87)) (flabbert)
    **Fixes [#86](https://github.com/stones2stars/S2S/issues/86)**
    **Fixes [#87](https://github.com/stones2stars/S2S/issues/87)**
- Tier-3 correctness fixes in CvPlot ([#77](https://github.com/stones2stars/S2S/issues/77), [#79](https://github.com/stones2stars/S2S/issues/79), [#81](https://github.com/stones2stars/S2S/issues/81)) (flabbert)
    **Fixes [#77](https://github.com/stones2stars/S2S/issues/77)**
    **Fixes [#79](https://github.com/stones2stars/S2S/issues/79)**
    **Fixes [#81](https://github.com/stones2stars/S2S/issues/81)**
- Add cutting-edge discount instead of overwriting it for AI in getResearchCost ([#97](https://github.com/stones2stars/S2S/issues/97)) (flabbert)
    **Fixes [#97](https://github.com/stones2stars/S2S/issues/97)**
- Fix wrong player index in doHeadquarters team-scoring loop ([#99](https://github.com/stones2stars/S2S/issues/99)) (flabbert)
    **Fixes [#99](https://github.com/stones2stars/S2S/issues/99)**
- Tier-2 correctness fixes in CvPlayer ([#107](https://github.com/stones2stars/S2S/issues/107), [#109](https://github.com/stones2stars/S2S/issues/109), [#114](https://github.com/stones2stars/S2S/issues/114), [#116](https://github.com/stones2stars/S2S/issues/116), [#117](https://github.com/stones2stars/S2S/issues/117)) (flabbert)
    **Fixes [#107](https://github.com/stones2stars/S2S/issues/107)**
    **Fixes [#109](https://github.com/stones2stars/S2S/issues/109)**
    **Fixes [#114](https://github.com/stones2stars/S2S/issues/114)**
    **Fixes [#116](https://github.com/stones2stars/S2S/issues/116)**
    **Fixes [#117](https://github.com/stones2stars/S2S/issues/117)**
- Merge pull request [#164](https://github.com/stones2stars/S2S/issues/164) from Stones2Stars/fix/agent-158-diplo-equal (flabbert)
- Merge pull request [#163](https://github.com/stones2stars/S2S/issues/163) from Stones2Stars/fix/agent-mapgen-159-160 (flabbert)
- Merge pull request [#165](https://github.com/stones2stars/S2S/issues/165) from Stones2Stars/fix/agent-161-conscript (flabbert)
- Merge pull request [#166](https://github.com/stones2stars/S2S/issues/166) from Stones2Stars/fix/agent-162-assimilate-capital (flabbert)
- Guard rebel capital in assimilateHandler before war-odds ([#162](https://github.com/stones2stars/S2S/issues/162)) (flabbert)
    **Fixes [#162](https://github.com/stones2stars/S2S/issues/162)**
- Guard getConscriptUnit() in calculatePotentialConscriptUnit ([#161](https://github.com/stones2stars/S2S/issues/161)) (flabbert)
    **Fixes [#161](https://github.com/stones2stars/S2S/issues/161)**
- Fix inverted equal-power filter in CvDiplomacy.filterUserResponse ([#158](https://github.com/stones2stars/S2S/issues/158)) (flabbert)
    **Fixes [#158](https://github.com/stones2stars/S2S/issues/158)**
- Fix Y-axis split guards and dead strip clamp in fractal map gen ([#159](https://github.com/stones2stars/S2S/issues/159), [#160](https://github.com/stones2stars/S2S/issues/160)) (flabbert)
    **Fixes [#159](https://github.com/stones2stars/S2S/issues/159)**
    **Fixes [#160](https://github.com/stones2stars/S2S/issues/160)**

## v1.BETA.163 - 2026-06-05
### Ci
- only run AppVeyor commit builds on main and release(flabbert)
### Docs
- clarify old-vs-new unit pathfinder and USE_OLD_PATH_GENERATOR(flabbert)
- add engine FAStar pathfinding reference(flabbert)
- import C2C community modding + player docs for review(flabbert)

### All Changes
- Merge pull request [#157](https://github.com/stones2stars/S2S/issues/157) from Stones2Stars/fix/agent-156-trait-req-fallback (flabbert)
- Persist modder game options so trait threshold ignores low fallback ([#156](https://github.com/stones2stars/S2S/issues/156)) (flabbert)
    **Fixes [#156](https://github.com/stones2stars/S2S/issues/156)**
- Merge pull request [#155](https://github.com/stones2stars/S2S/issues/155) from Stones2Stars/add-issue-template (flabbert)
- Add a simple bug-report issue form for users (flabbert)
- Fix cannotMaintain skipping higher process tiers (agent-found [#140](https://github.com/stones2stars/S2S/issues/140)) (flabbert)
    **Fixes [#140](https://github.com/stones2stars/S2S/issues/140)**
- Merge pull request [#152](https://github.com/stones2stars/S2S/issues/152) from Stones2Stars/fix/agent-found-cvplayerai-scoring (flabbert)
- Merge pull request [#151](https://github.com/stones2stars/S2S/issues/151) from Stones2Stars/fix/agent-found-83-rbombard-range (flabbert)
- Fix 3 CvPlayerAI scoring/crash bugs (agent-found [#125](https://github.com/stones2stars/S2S/issues/125), [#130](https://github.com/stones2stars/S2S/issues/130), [#134](https://github.com/stones2stars/S2S/issues/134)) (flabbert)
    **Fixes [#125](https://github.com/stones2stars/S2S/issues/125)**
    **Fixes [#130](https://github.com/stones2stars/S2S/issues/130)**
    **Fixes [#134](https://github.com/stones2stars/S2S/issues/134)**
- Merge pull request [#148](https://github.com/stones2stars/S2S/issues/148) from Stones2Stars/fix/agent-found-crash-batch2 (flabbert)
- Merge pull request [#149](https://github.com/stones2stars/S2S/issues/149) from Stones2Stars/fix/agent-found-62-corp-maintenance (flabbert)
- Fix getMinimumRBombardRange() mixing damage-limit and range (agent-found [#83](https://github.com/stones2stars/S2S/issues/83)) (flabbert)
    **Fixes [#83](https://github.com/stones2stars/S2S/issues/83)**
- Merge pull request [#147](https://github.com/stones2stars/S2S/issues/147) from Stones2Stars/fix/agent-found-84-continuemission (flabbert)
- Merge pull request [#150](https://github.com/stones2stars/S2S/issues/150) from Stones2Stars/ci/appveyor-build-filter (flabbert)
- ci: only run AppVeyor commit builds on main and release (flabbert)
- Fix calcCorporateMaintenance compounding over-charge (agent-found [#62](https://github.com/stones2stars/S2S/issues/62)) (flabbert)
    **Fixes [#62](https://github.com/stones2stars/S2S/issues/62)**
- Fix 4 more null-deref / OOB crashes (agent-found, crash batch 2) (flabbert)
    **Fixes [#91](https://github.com/stones2stars/S2S/issues/91)**
    **Fixes [#85](https://github.com/stones2stars/S2S/issues/85)**
    **Fixes [#119](https://github.com/stones2stars/S2S/issues/119)**
    **Fixes [#123](https://github.com/stones2stars/S2S/issues/123)**
- Fix continueMission() dangling missionNode (agent-found [#84](https://github.com/stones2stars/S2S/issues/84)) (flabbert)
    **Fixes [#84](https://github.com/stones2stars/S2S/issues/84)**
- Merge pull request [#145](https://github.com/stones2stars/S2S/issues/145) from Stones2Stars/fix/agent-found-python (flabbert)
- Merge pull request [#144](https://github.com/stones2stars/S2S/issues/144) from Stones2Stars/fix/agent-found-city-ai (flabbert)
- Merge pull request [#143](https://github.com/stones2stars/S2S/issues/143) from Stones2Stars/fix/agent-found-unit-ai (flabbert)
- Merge pull request [#146](https://github.com/stones2stars/S2S/issues/146) from Stones2Stars/docs/pathfinding-reference (flabbert)
- Merge pull request [#142](https://github.com/stones2stars/S2S/issues/142) from Stones2Stars/fix/agent-found-crash-batch (flabbert)
- docs: clarify old-vs-new unit pathfinder and USE_OLD_PATH_GENERATOR (flabbert)
- docs: add engine FAStar pathfinding reference (flabbert)
- Fix 3 Python logic bugs (agent-found, batch 2c) (flabbert)
    **Fixes [#136](https://github.com/stones2stars/S2S/issues/136)**
    **Fixes [#137](https://github.com/stones2stars/S2S/issues/137)**
    **Fixes [#138](https://github.com/stones2stars/S2S/issues/138)**
- Fix 5 City-AI logic bugs (agent-found, batch 2b) (flabbert)
    **Fixes [#58](https://github.com/stones2stars/S2S/issues/58)**
    **Fixes [#65](https://github.com/stones2stars/S2S/issues/65)**
    **Fixes [#67](https://github.com/stones2stars/S2S/issues/67)**
    **Fixes [#69](https://github.com/stones2stars/S2S/issues/69)**
    **Fixes [#70](https://github.com/stones2stars/S2S/issues/70)**
- Fix 7 Unit-AI logic bugs (agent-found, batch 2a) (flabbert)
    **Fixes [#49](https://github.com/stones2stars/S2S/issues/49)**
    **Fixes [#51](https://github.com/stones2stars/S2S/issues/51)**
    **Fixes [#52](https://github.com/stones2stars/S2S/issues/52)**
    **Fixes [#53](https://github.com/stones2stars/S2S/issues/53)**
    **Fixes [#54](https://github.com/stones2stars/S2S/issues/54)**
    **Fixes [#55](https://github.com/stones2stars/S2S/issues/55)**
    **Fixes [#56](https://github.com/stones2stars/S2S/issues/56)**
- Fix 10 crash / null-deref / data-corruption bugs (agent-found, multi-line) (flabbert)
    **Fixes [#75](https://github.com/stones2stars/S2S/issues/75)**
    **Fixes [#73](https://github.com/stones2stars/S2S/issues/73)**
    **Fixes [#80](https://github.com/stones2stars/S2S/issues/80)**
    **Fixes [#63](https://github.com/stones2stars/S2S/issues/63)**
    **Fixes [#93](https://github.com/stones2stars/S2S/issues/93)**
    **Fixes [#94](https://github.com/stones2stars/S2S/issues/94)**
    **Fixes [#104](https://github.com/stones2stars/S2S/issues/104)**
    **Fixes [#110](https://github.com/stones2stars/S2S/issues/110)**
    **Fixes [#111](https://github.com/stones2stars/S2S/issues/111)**
    **Fixes [#112](https://github.com/stones2stars/S2S/issues/112)**
- Merge pull request [#141](https://github.com/stones2stars/S2S/issues/141) from Stones2Stars/fix/agent-found-oneliners (flabbert)
- Drop the getExtraFreedomFighters change ([#118](https://github.com/stones2stars/S2S/issues/118)) — ambiguous intent, no callers (flabbert)
- Merge pull request [#96](https://github.com/stones2stars/S2S/issues/96) from Stones2Stars/docs/import-c2c-community-docs (flabbert)
- Fix 15 one-liner correctness bugs from the agent-found review (flabbert)
    **Fixes [#50](https://github.com/stones2stars/S2S/issues/50)**
    **Fixes [#74](https://github.com/stones2stars/S2S/issues/74)**
    **Fixes [#76](https://github.com/stones2stars/S2S/issues/76)**
    **Fixes [#82](https://github.com/stones2stars/S2S/issues/82)**
    **Fixes [#90](https://github.com/stones2stars/S2S/issues/90)**
    **Fixes [#98](https://github.com/stones2stars/S2S/issues/98)**
    **Fixes [#101](https://github.com/stones2stars/S2S/issues/101)**
    **Fixes [#100](https://github.com/stones2stars/S2S/issues/100)**
    **Fixes [#106](https://github.com/stones2stars/S2S/issues/106)**
    **Fixes [#115](https://github.com/stones2stars/S2S/issues/115)**
    **Fixes [#118](https://github.com/stones2stars/S2S/issues/118)**
    **Fixes [#135](https://github.com/stones2stars/S2S/issues/135)**
    **Fixes [#131](https://github.com/stones2stars/S2S/issues/131)**
    **Fixes [#127](https://github.com/stones2stars/S2S/issues/127)**
    **Fixes [#126](https://github.com/stones2stars/S2S/issues/126)**
- docs: import C2C community modding + player docs for review (flabbert)

## v1.BETA.123 - 2026-06-04
### Docs
- finish case rename (banana -> docs) and fix references(flabbert)
- add player-facing game-mechanics documentation(flabbert)
- restructure developer docs into reference/ and plans/(flabbert)
### Temp
- rename Docs -> banana (case-rename step 1/2)(flabbert)

### All Changes
- Merge pull request [#71](https://github.com/stones2stars/S2S/issues/71) from Stones2Stars/fix/unit-city-review-bugs (flabbert)
- Merge pull request [#72](https://github.com/stones2stars/S2S/issues/72) from Stones2Stars/docs/restructure (flabbert)
- docs: finish case rename (banana -> docs) and fix references (flabbert)
- temp: rename Docs -> banana (case-rename step 1/2) (flabbert)
- docs: add player-facing game-mechanics documentation (flabbert)
- docs: restructure developer docs into reference/ and plans/ (flabbert)
- Fix three verified CvUnit/CvCity correctness bugs (flabbert)
    **Fixes [#48](https://github.com/stones2stars/S2S/issues/48)**
    **Fixes [#57](https://github.com/stones2stars/S2S/issues/57)**
    **Fixes [#61](https://github.com/stones2stars/S2S/issues/61)**

## v1.BETA.114 - 2026-06-04

### All Changes
- Merge pull request [#47](https://github.com/stones2stars/S2S/issues/47) from Stones2Stars/ai-property-control-and-diagnostics (flabbert)
- Add AI tagged-logging developer reference (flabbert)
- Fix two mature-game asserts that flooded Asserts.log (flabbert)
- Rework AI property-control assignment and fix the production gate (flabbert)
- Fix never-ending-turn hang from AI unit re-evaluation spin (flabbert)
- Add AI unit/combat/production diagnostic logging (flabbert)
- Fix BetterBTSAI.cpp after union-merge of the ai-logging branches (flabbert)
- Merge remote-tracking branch 'origin/ai-logging/contractbroker' (flabbert)
- Merge remote-tracking branch 'origin/ai-logging/combat' (flabbert)
- Merge remote-tracking branch 'origin/ai-logging/gameinfo' (flabbert)
- Merge remote-tracking branch 'origin/ai-logging/founding' (flabbert)
- Merge remote-tracking branch 'origin/ai-logging/espionage' (flabbert)
- Merge remote-tracking branch 'origin/ai-logging/group' (flabbert)
- Merge remote-tracking branch 'origin/ai-logging/city' (flabbert)
- Merge remote-tracking branch 'origin/ai-logging/unit' (flabbert)
- Make ContractBroker logging heavy and structurally consistent (flabbert)
- Add [CTB] ContractBroker decision logging (flabbert)
- Add [COM] combat decision logging (flabbert)
- Add [GAME] session header log (GameInfo.log) (flabbert)
- Add [FND] city-founding decision logging (flabbert)
- Add [ESP] espionage decision logging (flabbert)
- Add [GRP] group/army coordination logging (flabbert)
- Enrich [UNT] logging with committed mission intent ([UNT/mission]) (flabbert)
- Add [CIT] city production decision logging (verbose at choices) (flabbert)
- Add [UNT] unit AI behaviour logging (flabbert)
- Add [WAR] team war/strategy decision logging (flabbert)
- Merge pull request [#29](https://github.com/stones2stars/S2S/issues/29) from Stones2Stars/ai-decision-logging (flabbert)
- Fix four AI decision-making bugs surfaced by the new logging (flabbert)
- Set per-player AI helper owners on load (CvPlayer::read) (flabbert)
- Log realized trade items in CvDeal::startTrade ([DIP/trade]) (flabbert)
- Add AI logging rollout plan to docs (flabbert)
- Add CvDecisionAI flavour/decision logging; retire legacy BBAI logging (flabbert)

## v1.BETA.85 - 2026-06-04

### All Changes
- Merge pull request [#28](https://github.com/stones2stars/S2S/issues/28) from Stones2Stars/fix-worker-escort-stall-and-network-automation (flabbert)
- Stop workers stalling on WAIT_FOR_ESCORT in foreign territory (flabbert)
- Merge pull request [#27](https://github.com/stones2stars/S2S/issues/27) from Stones2Stars/fix-event-city-ring-targeting (flabbert)
- Fix city events ringing a random tile instead of the city (flabbert)
- Merge pull request [#26](https://github.com/stones2stars/S2S/issues/26) from Stones2Stars/worker-city-commitment (flabbert)
- Stop workers abandoning their city when they stray into another's radius (flabbert)

## v1.BETA.75 - 2026-06-03

### All Changes
- Merge pull request [#22](https://github.com/stones2stars/S2S/issues/22) from Stones2Stars/combat-simplification (flabbert)
- Combat scope doc: record removal phase complete + Phase 3a done (flabbert)
- Show the combat-odds bar in the minimal and assassinate previews too (flabbert)
- Restore the graphical combat-odds bar in the combat tooltip (flabbert)
- Make asserts fire properly: remove the bIgnoreAlways=true suppression hack (flabbert)
- Log asserts in the Assert build instead of popping dialogs (flabbert)
- Restore live element definitions wrongly stripped from the unit schema (flabbert)
- Add Phase 3b plan: route AI win-% through the binomial engine (flabbert)
- Phase 3a: unify resolution + odds onto a shared RoundModel (Layer 1) (flabbert)
- Remove last affliction/equipment vestiges: NoSpread, Afflict params, equipment category (flabbert)
- Clean orphans from removed combat options (afflictions/equipment) (flabbert)
- Combat scope: confirm KEEP for REALISTIC_SIEGE/AMNESTY/HIDE_SEEK/WITHOUT_WARNING (flabbert)
- R4 Phases 2-7: remove inert affliction/critical/fortitude scaffolding (flabbert)
- R4 Phase 1 checkpoint: remove OUTBREAKS_AND_AFFLICTIONS game option (flabbert)
- R5a+R5b: remove dodge/precision + armor/puncture combat stats (flabbert)
- Combat simplification checkpoint: CvCombatModel + CvHunterAI + R1-R4 removals (flabbert)

## v1.BETA.61 - 2026-06-01

### All Changes
- increase strength of hunters in earlygame (flabbert)

## v1.BETA.59 - 2026-06-01

### All Changes
- Merge pull request [#21](https://github.com/stones2stars/S2S/issues/21) from Stones2Stars/feature/size-matters-group-merge (flabbert)
- Size Matters: enable bulk merge across a selection group (flabbert)
- Merge pull request [#20](https://github.com/stones2stars/S2S/issues/20) from Stones2Stars/feature/configurable-production-overflow-cap (flabbert)
- Add add-bug-option project skill (flabbert)
- Make production overflow cap a configurable BUG option (flabbert)
- Updated text for increasing difficulty, cibola peasant 240-160 work rate to better be compared to normal work rate for his age, tiny nerf to set captive free option food reward, nerf to negligent additional -1 happiness, and reduced free city and distance upkeep by 10% should make it worse for free gold city spam printing, amber mine now needs mining camp, fixed scroll maker now with printing press removes its commerce instead of costing gold, subdued wolverine no longer builds enclosure rodent, removed fresh water as prereq for seed camp since it allowed it to be built on ice terain next to a river Ordered all options in xml to be same as in backend so options wont have wrong description aka turning on wrong options Fixed via appia wonder route bug Add 5 gold to capital as temp fix for economy changes Restored tribal guard as auto start unit but still is buildable if dies and can be upgraded as a temp fix until ai can survive fixed some typos neanderthall tribe guardian now promotes corectly unlocking chasing now will give a free chaser like gathering gives gatherer persistence hunting will now give 1 free chaser to all who research it and 1 more to the first one to research it (to speed up and make early game a bit less boring, also i think is good paralele to hunter/gatherer dynamics) (SimoCvijic0)

## v1.BETA.50 - 2026-06-01

### All Changes
- make without warning default on (flabbert)
- reorder the gameoption xml so that it matches with gameoption enum (flabbert)
- Add UNITAI selection & unit-production documentation (flabbert)
- Fix stale LaunchC2C.bat references to LaunchS2S.bat (flabbert)

## v1.BETA.45 - 2026-05-31

### All Changes
- One-time svn delete of C2C.bat (renamed to S2S.bat) (flabbert)

## v1.BETA.43 - 2026-05-31

### All Changes
- Rename deployed launcher C2C.bat to S2S.bat (flabbert)
- Stage README + CHANGELOG into both SVN and Git deploy roots (flabbert)
- Use canonical Stones2Stars/Stones2Stars.git casing for the mirror URL (flabbert)

## v1.BETA.39 - 2026-05-31
### FPKCLEAN
- add GitHub distribution mirror to deploy + sub-100MB FPK cap(flabbert)

### All Changes
- FPKCLEAN: add GitHub distribution mirror to deploy + sub-100MB FPK cap (flabbert)

## v1.BETA.37 - 2026-05-30

### All Changes
- Merge pull request [#19](https://github.com/stones2stars/S2S/issues/19) from Stones2Stars/feature/next-trait-culture-bug-option (flabbert)
- Move NEXT_TRAIT_CULTURE_REQ_PERCENT to a BUG menu option (flabbert)

## v1.BETA.33 - 2026-05-30

### All Changes
- Merge pull request [#18](https://github.com/stones2stars/S2S/issues/18) from Stones2Stars/feature/cityimprovechanges (flabbert)
- rework city and worker improvement (flabbert)
- update agents md (flabbert)
- fix python error in via appia (flabbert)
- add claude skills, update agents.md and update gitignoire (flabbert)
- add 6 base gold to capital (flabbert)

## v1.BETA.28 - 2026-05-29

### All Changes
- Merge pull request [#17](https://github.com/stones2stars/S2S/issues/17) from Stones2Stars/feature/worker-ai-and-plot-snapshot (flabbert)
- Worker AI overhaul + plot snapshot logger (flabbert)
- Merge pull request [#15](https://github.com/stones2stars/S2S/issues/15) from Stones2Stars/feature/addinforepositories (flabbert)
- remove annoying error when loading game after previous game has already been loaded (flabbert)
- Merge pull request [#14](https://github.com/stones2stars/S2S/issues/14) from Stones2Stars/feature/buildingsrepo-coverage (flabbert)
- Merge pull request [#13](https://github.com/stones2stars/S2S/issues/13) from Stones2Stars/feature/buildsrepo-worker-coverage (flabbert)
- Merge pull request [#16](https://github.com/stones2stars/S2S/issues/16) from Stones2Stars/feature/sparsify-civic-perinfo-arrays (flabbert)
- sparsify civic and event per-building dense-loop callers (flabbert)
- expand BuildingsRepo with worldWonders, withFreeStartEra, autoBuildings (flabbert)
- add BuildsRepo::routeBuilds and migrate CvPlot::getBuildTime (flabbert)
- introduce Repos pattern with BuildingsRepo and BuildsRepo (flabbert)
- add claude generated doProduction docs (flabbert)

## v1.BETA.9 - 2026-05-27

### All Changes
- ensure mapscript does not crash with graphics paging off (flabbert)

## v1.BETA.7 - 2026-05-27

### All Changes
- add claude generated docs on how mapscripts work (flabbert)
- remove cache from appveyor (flabbert)
- Merge pull request [#12](https://github.com/stones2stars/S2S/issues/12) from Stones2Stars/splitinfos (flabbert)
- Merge branch 'splitinfos' of https://github.com/stones2stars/s2s into splitinfos (flabbert)
- updat einclude (flabbert)
- split out infos to individual files (flabbert)
- add claude folder to gitignore (flabbert)
- update contractbroker readme (flabbert)
- s2s patch111 (SimoCvijic0)
- Nerf to mahogany woodcutter to be a bit better than a mammoth worker that is unlocked in same tech 240 -> 160 work rate. Increased trained cat and its combat line upkeep by 1 as they are OP. Moved gold vault to be a national wonder from a regular building. Fixed grand marine festival coin from vicinity resources now is added. (SimoCvijic0)
- updat einclude (flabbert)
- split out infos to individual files (flabbert)
- transfer updates from c2c (SimoCvijic0)

## v1.BETA.27 - 2026-05-18

### All Changes
- make units or features not disappear with graphics paging off (flabbert)

## v1.BETA.25 - 2026-05-17

### All Changes
- use correct storage (flabbert)
- make vscode no longer try to set compiler to 2017 (flabbert)
- make intellisense not cry when using foreach_ (flabbert)

## v1.BETA.21 - 2026-05-14

### All Changes
- referenec rename stage 1 (flabbert)

## v1.BETA.18 - 2026-05-13

### All Changes
- rename usersettings folder to Stones2Stars (quickfix) (flabbert)

## v1.BETA.17 - 2026-05-13

### All Changes
- add latest c2c changes (flabbert)

## v1.BETA.14 - 2026-05-13

### All Changes
- use finalrelease (flabbert)

## v1.BETA.13 - 2026-05-13

### All Changes
- use token (flabbert)
- fix tags? maybe? (flabbert)
- do I really need git user when I have fully connected the repo? (flabbert)
- fix missing tag manipulation (flabbert)
- debug release pipe (flabbert)
- update fpkbuilder (flabbert)
- update fpkbuilder (flabbert)
- update secrets (flabbert)
- use fpkbuilder instead of fpklive (flabbert)
- add  svn build to cache (flabbert)
- test appveyor (flabbert)
- remove image from appveyor (flabbert)
- add Ai generated docs, and AGENTS.md (flabbert)
- remove appveyour cache, it does not work (flabbert)
- add new fpk builder (flabbert)

## v1.BETA.2 - 2026-02-07

### All Changes
- backup of old background (flabbert)
- change background (flabbert)
- fix (SimoCvijic0)
- fix (SimoCvijic0)
- fix (SimoCvijic0)
- removed typo removed typo removed typo removed typo added flavour for ancient customs 20. Shattered the abomination of the ancient customs and will do so eventually with all such buildings as they are counter to the     idea of a civ game, giving bonuses for all buildings even ones you can't build.... Now it replaces a few buildings     that all can build in any city and has its own small bonuses to boost its importance. 19. Units that fight disease and units that educate in cities now will get passive xp per turn as they do those activities rest of fixes 18. Animals can no longer fortify sry beavers 17. New vicinity Bonus mechanic update, if tile is not worked, improved, connected the vicinity bonus will not count. Before it only mattered that it exists this now shifts more power to tiles. Also, most buildings now shifted from global to vicinity bonuses only. 14. All auto build behavioral buildings are now immune to destruction by events, such as alpha male, stick gatherer etc. Earthquake event now doesnt kill pop when it should not, and duck cant go on mountain peaks Wembley stadium is now world wonder instead of national Muddy now gives 1 hammer instead of food 13. Last but not least a new economic empire resource sistem that is here to give purpose to stacking resources. Having 1 or 5 oil doesn't matter as long as you have 1. Not any more now empire resource sistem gives global bonuses for every copy of resource your empire has. Oil as an example gives 2 hammers per copy so stacking 5 oils gives 10 hammers. This also provides a local bonus for the city for the remaining raw value. Example grain gives 2 global and 2 local food bonus to a city. 13. Last but not least a new economic empire resource sistem that is here to give purpose to stacking resources. Having 1 or 5 oil doesn't matter as long as you have 1. Not any more now empire resource sistem gives global bonuses for every copy of resource your empire has. Oil as an example gives 2 hammers per copy so stacking 5 oils gives 10 hammers. This also provides a local bonus for the city for the remaining raw value. Example grain gives 2 global and 2 local food bonus to a city. 12. And now finally the balance changes: 12. And now finally the balance changes: Tech commit 11. Reworked the prehistoric, ancient, classical and medieval tech tree to better match historical accuracy - All units buildings that were moved up down left right were rebalanced according to the strength and cost of the   place they are now in the tech three ( balance is not changed cost per tech lvl ). - Most notable changes, cavalry becomes available after chariots in ancient - Elephants become available after military training in classical - Christianity from classical - Many other changes on removing useless prereq teches to enable a smoother flow explore the new tree and new strategies 10. Changed 95% of buildings that gave gold into commerce other than ones that makes sense to give gold: - Exemptions are buildings like tax office, gambling houses, thieves etc... - Makes economy more real by managing tax rates when in need of gold instead of just getting flat gold direct from buildings   sliders have purpose again. - Drastically improves AI by reducing its 2 big weaknesses. First AI stacks useless gold and does nothing with it   now if he has enough gold AI maxes out research and since most buildings are now commerce AI is much more potent in   researching then before without loosing his combat edge. Second AI won't send you 100000 gold for chicken because AI won't have   100000 gold lying around. - Changed all global bonuses to buildings to local ( almost all ) this is also another nerf to building meta and moving to tiles   primacy. Cities that have good local bonuses can have stronger buildings but because you have wheat in africa doesn't mean bakery in   siberia makes more bread instantly when in ancient age. (Note im looking into making stackable vicinity bonuses to make this   even more powerful and flavorful) - Changed all housing in same principle - Adjusted great persons and specialists in same principle 9. Due to previous yield changes and the increase of hunting reward from previous updates base city growth threshold has been increased from 124 -> 130, the per lvl scale will remain the same. 8. In the same idea as with the raw yield all improvements have their yield increased by 1 where appropriate 7. Raw resource yield buff. Every raw resource in the game has had its base yield increased by +1. The goal is simple: -Make resource tiles matter more -Reduce late game building power -Preserve each resource’s intended role Instead of listing 108 individual changes, this was done systematically and consistently across all raw resources. 6. Added building obsidian gatherer 0/1/2 yield works same as rice gatherer etc... 5. Events fixes: - Bugfix for text for event kava - Fixed event found murex gave clam now gives murex - Event pirates of the neutral zones now triggers correctly 4. Implemented scaling per era unit supply costs 1 x Age starting from prehistoric as base 1 then ancient 2 etc... Idea is to have a better simulated gold sink, as 1 gold for stone thrower and 1 gold for panzer makes no sense. 3. Initial free units outside reduced to 5 from 10 and gold cost increased from 0.5 to 0.75 per unit ( a 50% increase). 2.Improved ai build wealth logic to allow for ai to go sometimes into negative forcing his units to disband so he can resume building buildings rather than getting stuck on wealth. (Noticed 2/3x better AI score as game progresses especially on harder difficulties..) 1. Special units reduced upkeep. Healers, Law Enforcement and Entertainers upkeep reduced by 1 for all ages (SimoCvijic0)
- Merge remote-tracking branch 'origin/main' (SimoCvijic0)
- update (SimoCvijic0)
- fix caching? (flabbert)

## v1.BETA.31 - 2025-11-17

### All Changes
- let username be visible (flabbert)
- go back to finalrelease for release build (flabbert)

## v1.BETA.29 - 2025-11-17

### All Changes
- update user and pass (flabbert)
- use flabbert user (flabbert)
- add the git stuff (flabbert)
- take debugging back to square one (flabbert)
- use dummy commit_desc (flabbert)
- use debug build to speed up testing (flabbert)
- go back to cloud until fpklive is rebuilt (flabbert)
- add discord notifications (flabbert)
- we seem to need to copy the info into the yml file? (flabbert)
- clean up unused parts of deploy scripts, define cloud and image in appveyour (flabbert)
- define environment variables in project (flabbert)
- add i-still-use-this to git whatchanged (flabbert)
- latest, and last from c2c (flabbert)
- update gitignore to not have unpackedassets, and remove actions (flabbert)
- Merge remote-tracking branch 'origin/main' (SimoCvijic0)
- test (SimoCvijic0)
- update appveyor script, remove secrets (flabbert)
- update install batfile to use S2S instead (flabbert)
- rename launch file (flabbert)
- rename ini file (flabbert)
- remove bad commit from old times (flabbert)
- First commit fix owls cant fly on mountain peaks (SimoCvijic0)
- remove c2c mentions in readme (flabbert)
- initial move (flabbert)

