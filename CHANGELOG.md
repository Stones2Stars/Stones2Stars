# CHANGELOG

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

