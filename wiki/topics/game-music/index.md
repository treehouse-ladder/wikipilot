---
title: Game composers and audio
kind: topic
sources: ["[[chrono-trigger-original-soundtrack-vinyl-box-to-release-in-april-2026-f0889eea]]", "[[wwise-vs-fmod-vs-metasounds-choosing-audio-middleware-for-your-ue5-game-in-2026-9afdff3e]]", "[[the-best-video-game-soundtracks-of-2026-so-far-11501826]]", "[[mick-gordon-in-conversation-sonic-state-jan-2026-53ed29e8]]", "[[pragmata-soundtrack-and-vinyl-release-review-2026-31dc604e]]", "[[elden-ring-nightreign-soundtrack-is-coming-to-vinyl-30e2c324]]", "[[seamless-haptics-for-sound-designers-meta-haptics-studio-meets-fmod-and-wwise-891ab31d]]", "[[david-wise-on-creating-gaming-soundtracks-40-years-later-dc37403c]]", "[[final-fantasy-distant-worlds-concerts-set-to-sail-through-the-u-s-in-2026-bd12486f]]", "[[aether-iron-soundtrack-music-review-5b0c61bb]]", "[[octopath-traveler-0-original-soundtrack-music-review-81d13f2c]]", "[[prescription-for-sleep-ocarina-of-time-music-review-f69d5aa2]]", "[[blue-prince-original-soundtrack-music-review-13877127]]", "[[interview-world-of-warcraft-lead-composer-on-making-of-midnight-s-human-made-music-013afc37]]", "[[lies-of-p-original-soundtrack-music-review-94ceba96]]", "[[citizen-sleeper-original-soundtrack-music-review-25f6b6c7]]"]
last_updated: 2026-05-23
last_verified: 2026-05-23
freshness_window_days: 60
---

# Game composers and audio

See [purpose](purpose.md) for the topic charter (in-scope / out-of-scope) and
`CLAUDE.md` "Cross-cutting relevance criteria" for the meta-bar.

## Summary

The first daily research pass surfaces a 2026 dominated by retrospective vinyl releases [[chrono-trigger-original-soundtrack-vinyl-box-to-release-in-april-2026-f0889eea]] and the maturation of adaptive-audio middleware choices for Unreal Engine 5 [[wwise-vs-fmod-vs-metasounds-choosing-audio-middleware-for-your-ue5-game-in-2026-9afdff3e]].

**Vinyl releases.** Square Enix is shipping a 30th-anniversary 4xLP box set of Yasunori Mitsuda's Chrono Trigger Original Soundtrack on March 25, 2026 in Japan and April 2026 in North America, with 64 tracks, Akira Toriyama jacket art, and a commemorative message from Mitsuda inscribed on the box lid [[chrono-trigger-original-soundtrack-vinyl-box-to-release-in-april-2026-f0889eea]]. Bandai Namco is shipping a 7LP Elden Ring: Nightreign vinyl collection in summer 2026, capturing 57 tracks across the Limveld map and the Forsaken Hollows DLC in a limited run of 4,999 copies [[elden-ring-nightreign-soundtrack-is-coming-to-vinyl-30e2c324]]. Capcom's Pragmata arrived in April 2026 with a 46-track score by Yasumasa Kitagawa blending orchestral emotion, ambient piano, and synth-driven tension, with YU-KA performing the ending theme "Memories Are You" [[pragmata-soundtrack-and-vinyl-release-review-2026-31dc604e]].

> To commemorate the 30th anniversary of Chrono Trigger, Square Enix will release a vinyl box set of the game's original soundtrack on March 25, 2026 in Japan and April 2026 for North America. The box includes a total of 64 tracks across 4 LPs from the original soundtrack.

> The epic, orchestral soundtrack to Elden Ring: Nightreign is coming to vinyl for the first time as a 7LP set ... limited to 4999 copies.

> Yasumasa Kitagawa delivered a cinematic sci-fi score blending orchestral emotion with futuristic electronic sound design, with the full 46-track OST released in April 2026.

**Original scores of note.** GameSpot's 2026 best-soundtracks roundup highlights Ridiculon's (Matthias Bossi & Jon Evans) folksy Mewgenics score, Anamanaguchi's 71-song Scott Pilgrim soundtrack, the meditative Cairn score, and the genre-shifting Esoteric Ebb score [[the-best-video-game-soundtracks-of-2026-so-far-11501826]]. Sonic State published a January 2026 long-form interview with Mick Gordon covering his process, the DOOM/DOOM Eternal/Wolfenstein/Prey/Killer Instinct catalog, and reflections on creativity [[mick-gordon-in-conversation-sonic-state-jan-2026-53ed29e8]].

> The Mewgenics score combines a punchy, folksy sound with the inner workings of a cat's mind, crafted by Ridiculon's Matthias Bossi and Jon Evans.

> Mick Gordon participated in a 2026 conversation with Bonfire Conversations, discussing his life, fame, process, creativity and his childhood, as well as his career, creative process, and approach to music.

**Adaptive-audio middleware.** A 2026 UE5-focused comparison argues developers now have three serious options: Wwise as the AAA industry standard with the most sophisticated hierarchical interactive-music system (segments, playlists, switches), FMOD as the indie-friendly powerhouse, and Epic's built-in MetaSounds — workable for simple adaptive music but lacking dedicated music authoring tools, while offering zero licensing cost versus Wwise's per-platform commercial fees [[wwise-vs-fmod-vs-metasounds-choosing-audio-middleware-for-your-ue5-game-in-2026-9afdff3e]]. This feeds directly into the pre-declared `adaptive-music-tech-comparison` page.

> In 2026, Unreal Engine 5 developers have three serious options: Wwise (the AAA industry standard), FMOD (the indie-friendly powerhouse), and MetaSounds (Epic's built-in procedural audio system) ... MetaSounds is workable for simple adaptive music but lacks dedicated music authoring tools.

**Audio middleware — haptics convergence.** A May 2026 Meta developer post details Meta Haptics Studio's integration with both major audio-middleware packages, folding controller-haptic authoring into the sound designer's existing toolchain: FMOD supports the `.haptic` format today via the Haptics Instrument in FMOD 2.03.11, and Wwise gains native `.haptic` support in early 2026 [[seamless-haptics-for-sound-designers-meta-haptics-studio-meets-fmod-and-wwise-891ab31d]]. The post frames `.haptic` as a candidate de-facto interchange standard for controller haptics, analogous to `.wav` for audio, covering essentially every commercial VR title in production through the two middleware integrations [[seamless-haptics-for-sound-designers-meta-haptics-studio-meets-fmod-and-wwise-891ab31d]]. This extends the existing Wwise/FMOD/MetaSounds comparison from purely musical/SFX authoring into unified audio-plus-haptic feedback.

> FMOD support is available today through the Haptics Instrument in FMOD 2.03.11, while Wwise will natively support .haptic in early 2026.

> the .haptic format is on track to become the de facto interchange spec for controller haptics across platforms, the same way .wav became the universal audio interchange format.

**Composer interviews.** Screen Rant interviewed Donkey Kong Country composer David Wise at Gamescom LATAM 2026, where he performed on the main stage on May 1–2; the conversation covers his 40-year career from Rare (1985–2009) through ongoing NDA projects, with Wise stressing continuous tool-learning as central to his evolving process [[david-wise-on-creating-gaming-soundtracks-40-years-later-dc37403c]].

> With a career spanning over 40 years, the musician has created soundtracks for some of the most popular games ever. Wise began his career in games at Rare in 1985 and remained there until 2009. His best-known work is for the fantastic Donkey Kong Country, which was released by Rare in 1994 for the SNES.

**Live performance.** Distant Worlds: Music from FINAL FANTASY returns to the U.S. through 2026, including a two-night Carnegie Hall event on June 12–13, 2026, "Celebrating Nobuo Uematsu!", with a program chosen by Uematsu (in attendance) and vocalists RIKKI and Amanda Achen [[final-fantasy-distant-worlds-concerts-set-to-sail-through-the-u-s-in-2026-bd12486f]].

> On June 12 and 13, 2026, Distant Worlds returns to the famed Carnegie Hall in New York City for "Celebrating Nobuo Uematsu!," a special concert event featuring beloved Final Fantasy music compositions chosen by Nobuo Uematsu himself.

## Recent updates

**Original scores of note (cont.).** The second daily pass on 2026-05-21 surfaces RPGFan's mid-May review run. The standout new original score is *Aether & Iron*, co-composed by two-time Grammy winner Christopher Tin and Grammy-nominee Alex Williamson — a noir-leaning orchestral score (strings, horns, light percussion) recorded with a live orchestra, with RPGFan calling its "Nations Crusade Adagio" a choir-and-orchestra piece sitting "somewhere between the romantic era of classical composition and a good Hans Zimmer film score," and flagging the album as a plausible Grammy shortlist contender for next year [[aether-iron-soundtrack-music-review-5b0c61bb]]. On the JRPG side, Yasunori Nishiki's *Octopath Traveler 0 Original Soundtrack* (Square Enix, SQEX-11181~2, released 2025-12-10) spreads across 2 CDs, with the first disc built around the main theme and four elaborated variants ("Fury," "Sorrow," "Compassion," "Requiem") plus a full "Wishvale" town suite, while roughly 40 percent of the set is carried over from Champions of the Continent [[octopath-traveler-0-original-soundtrack-music-review-81d13f2c]].

> The Aether & Iron Soundtrack was co-composed by Christopher Tin and Alex Williamson. Tin is a two-time Grammy-winning composer, while Williamson is a Grammy-nominee.

> About 40 percent of the OST is music lifted from Champions of the Continent, all found on the second of the soundtrack's two CDs. The first disc features the main theme and four elaborated versions (Fury, Sorrow, Compassion, and Requiem).

**Arrangement releases.** Scarlet Moon Records' jazz duo GENTLE LOVE — saxophonist Norihiko Hibino (a Metal Gear Solid series composer) and pianist AYAKI — released their first all-Zelda album, *Prescription for Sleep: Ocarina of Time*, marking The Legend of Zelda's 40th anniversary; RPGFan characterizes it as roughly "25% Zelda, 75% GENTLE LOVE" with four-to-seven-minute tracks given over to soloing and calm sonic exploration [[prescription-for-sleep-ocarina-of-time-music-review-f69d5aa2]].

> Scarlet Moon Records' prolific jazz duo GENTLE LOVE released their first-ever all-Zelda album, Prescription for Sleep: Ocarina of Time, with saxophonist Norihiko Hibino (composer on the Metal Gear Solid series) and pianist AYAKI celebrating the 40th anniversary of The Legend of Zelda.

**Original scores of note (cont.).** The 2026-05-22 daily pass surfaces RPGFan's review of the *Blue Prince Original Soundtrack* by the Dutch duo Trigg & Gusset — lead composer Bart Knol with Erik van Geer co-composing on bass clarinet, their first game score [[blue-prince-original-soundtrack-music-review-13877127]]. The defining compositional choice is the total absence of drums or percussion, which RPGFan credits with enabling "excellent rubato" and a gentle, swaying ambient-jazz character; the closest the album comes to a pulse is the brisk 3/4 ostinato synth pattern of standout track "Under the Black Bridge" [[blue-prince-original-soundtrack-music-review-13877127]].

> One notable aspect of the Blue Prince OST is that it has no drums and no percussion of any kind. This allows for some excellent rubato and lets the listener get lost in the gentle, swaying tones without feeling that pulsing, bouncing energy.

> A standout track is Under the Black Bridge, a brisk 3/4 piece with an ostinato synth pattern that comes as close to percussion as the OST gets.

## Composer interviews (cont.) — 2026-05-23

The 2026-05-23 daily pass surfaces Game Informer's February 2026 interview with World of Warcraft lead composer Leo Kaliski on the score for the *Midnight* expansion. Kaliski frames Blizzard's music team as deliberately human-made amid the generative-AI wave, saying "We here at Blizzard feel very lucky and happy that we're not using generative AI. We're just writing what we think is cool" [[interview-world-of-warcraft-lead-composer-on-making-of-midnight-s-human-made-music-013afc37]]. He argues AI music still lags human work on perceptibility: "Music is not there yet. Usually, you hear it, and you instantly know something is not right about it, or the fidelity isn't there" [[interview-world-of-warcraft-lead-composer-on-making-of-midnight-s-human-made-music-013afc37]]. On craft, Kaliski describes WoW's deliberately broad musical identity as functional rather than foregrounded — the score sits in the background to support gameplay and story "without overstepping boundaries, unless it's a big cinematic moment" [[interview-world-of-warcraft-lead-composer-on-making-of-midnight-s-human-made-music-013afc37]].

> We here at Blizzard feel very lucky and happy that we're not using generative AI. We're just writing what we think is cool, and are happy to do that.

> Music is not there yet. Usually, you hear it, and you instantly know something is not right about it, or the fidelity isn't there.

**Original scores of note (cont.).** RPGFan's catalog adds two atmospheric OST reviews. The *Lies of P Original Soundtrack* spans 70 total tracks, the first 16 being collectible in-game records carrying lyrical ballads plus remixed "Golden" versions; RPGFan tags opener "Feel" as "rain-soaked smooth jazz" that sets the album apart from peer action-RPG scores, and notes the 2025 free addition of 51 Overture-DLC tracks to digital copies [[lies-of-p-original-soundtrack-music-review-94ceba96]]. Amos Roddy's *Citizen Sleeper Original Soundtrack* is a mellow 23-track slice-of-life score for a lived-in sci-fi setting, blending industrial, electro, and ambient textures RPGFan compares to Vangelis' *Blade Runner*, Kenji Kawai's *Ghost in the Shell*, and Kenji Yamamoto's *Metroid Prime* [[citizen-sleeper-original-soundtrack-music-review-25f6b6c7]].

> The soundtrack comprises 70 total tracks, with the first 16 being collectible records featuring lyrical ballads plus remixed Golden versions.

> The soundtrack is a mix of industrial, electro, and ambient sounds reminiscent of quieter moments from film and game soundtracks like Vangelis' Blade Runner (1982), Kenji Kawai's Ghost in the Shell (1995), and Kenji Yamamoto's Metroid Prime (2002).


## Comparisons

Pre-declared comparison pages for this topic. Listed in prose backticks
until the underlying entity pages exist:

- `2026-notable-soundtracks` — rolling list of notable score releases.
- `adaptive-music-tech-comparison` — Wwise vs FMOD vs proprietary.

## Disputes

- [[wwise-vs-fmod-vs-metasounds-choosing-audio-middleware-for-your-ue5-game-in-2026-9afdff3e]] claims MetaSounds is workable for simple adaptive music but lacks dedicated music authoring tools, positioning Wwise as the AAA standard for interactive-music hierarchy; field reports from composers shipping UE5 titles on MetaSounds are more bullish about MetaSounds for non-trivial procedural music. Status: unresolved

- [[interview-world-of-warcraft-lead-composer-on-making-of-midnight-s-human-made-music-013afc37]] claims AI-generated music is still instantly perceptible as artificial ("the fidelity isn't there"); recent generative-audio model releases tracked under frontier-models/ai-in-game-dev claim near-indistinguishable output for short cues. Status: unresolved
## Open questions

- [ ] What is the breakdown of AAA vs indie adoption of Wwise, FMOD, and MetaSounds as of mid-2026? The comparison source asserts industry standing but does not provide adoption numbers.
- [ ] Is there a confirmed Pragmata OST vinyl release planned, or only the streaming OST? The review notes Capcom often does limited vinyl runs for major new IPs but no Pragmata vinyl was announced as of the review date.
- [ ] Did Mick Gordon discuss the still-unresolved DOOM Eternal soundtrack credit dispute in the January 2026 Sonic State conversation?
- [ ] Which 2026-shipping AAA titles are using MetaSounds in production for music — not just sound effects? Adoption data for music specifically would close the middleware comparison.
- [ ] Does the `.haptic` interchange-standard claim hold beyond VR titles? The Meta source frames adoption around "essentially every commercial VR title," but flat-panel/console controller-haptic adoption of `.haptic` via FMOD/Wwise is not quantified.
- [ ] What are the licensing terms for shipping `.haptic`-authored content through FMOD vs Wwise on PSVR2/PC VR, and do they differ from each middleware's existing audio licensing?
- [ ] Which (if any) of David Wise's NDA projects are game scores, and for what platform/studio?
- [ ] Is there a physical (vinyl/CD) release planned for the Aether & Iron soundtrack [[aether-iron-soundtrack-music-review-5b0c61bb]], or streaming-only? RPGFan's review covers the music but does not note a physical edition.
- [ ] Does the Octopath Traveler 0 OST overlap with Champions of the Continent constitute padding, or is the carried-over 40 percent re-recorded/re-arranged [[octopath-traveler-0-original-soundtrack-music-review-81d13f2c]]?
- [ ] Is there a physical (vinyl/CD) release planned for the Blue Prince Original Soundtrack [[blue-prince-original-soundtrack-music-review-13877127]], or is it Bandcamp/streaming-only? RPGFan notes Trigg & Gusset's Bandcamp catalog but does not mention a Blue Prince physical edition.

- [ ] Is there a physical (vinyl/CD) release planned for the WoW: Midnight soundtrack, or streaming/in-game only? The interview covers process but no physical edition.
- [ ] Does the WoW: Midnight score use any adaptive-music middleware (Wwise/FMOD/proprietary), or is it linear-cue based? The interview discusses instrumentation and creative process but not the interactive-music implementation.
- [ ] Is the Lies of P OST's 70-track count inclusive of the 51 free Overture-DLC tracks, or are those additional [[lies-of-p-original-soundtrack-music-review-94ceba96]]? The review is ambiguous on whether the count predates or includes the DLC additions.
## See also

- [purpose](purpose.md)
- [[2026-05-21-wwise-fmod-metasounds-ue5-comparison]]
