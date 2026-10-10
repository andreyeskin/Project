# Исследование визуального стиля для обучающего ЭКГ-квеста «Nachtdienst»

Дата: 2026-10-10. Собрано шестью поисковыми агентами (пять завершили работу; шестой, «эстетика больниц», успел вернуть результат до остановки, если он есть ниже). Стадии синтеза, жюри и критики остановлены по решению автора: сырых находок оказалось достаточно. Тексты находок на английском, как вернули агенты; ссылки проверялись агентами по первоисточникам, но не перепроверялись вручную.

## Сквозные выводы (повторяются у разных агентов)

1. Два слоя: спокойный низкоконтрастный мир и точный высококонтрастный документ (лента ЭКГ) поверх него. Мир всегда темнее и менее насыщен, чем лента.
2. Ленту не стилизовать: чёрная кривая на розовой миллиметровке для измерений; зелёный на чёрном монитор только как атмосфера.
3. Красно-розовая гамма и чистый чёрный зарезервированы за лентой и тревогами; мир в кремовом, мятном, бирюзовом, дереве и одном тёплом акценте.
4. Печатные эффекты (растр, зерно, дизеринг, несведение) только на мир, никогда на ленту.
5. Постановка кадра: фронтальная камера по центру, симметрия, 1 доминирующий + 1 поддерживающий + 1 акцентный цвет, мало крупных предметов.
6. Обучение: подсказки на ленте как статичные заливки, без мигания; системный алгоритм чтения ЭКГ как постоянная рельса интерфейса; эмоции персонажей через лицо; тест на каждый предмет: «использовал бы его кардиолог для решения?».

## Квесты и игры про чтение улик: стили и приёмы

### Papers, Please (Lucas Pope / 3909)
- Тип: game  
- Ссылка: https://papersplea.se/  
- Стиль: bleak Soviet-bloc pixel art with a hard world/desk split and draggable paper documents  
- Визуальные черты: Fixed single screen split into zones: top third = exterior checkpoint scene (world), bottom two-thirds = inspector's desk where every document is a draggable object (Wikipedia screenshot caption: arrival left-centre, paperwork bottom-right, checkpoint top third); Palette is deliberately coarse and muted (Game Developer: 'coarse, bleak color'; 'bleak, aging Soviet bloc'): approx. desk charcoal #2A2A2A–#3B3B3B, snow/sky grey #B9BAB2, concrete #6E6E66, Arstotzka olive-green #4F6B3A, passport cream #E6DCC3, approve-stamp green #3E8B4C, deny-stamp red #B5362B; Documents are the brightest, cleanest elements on screen; world layer is low-contrast and small, so attention naturally falls on the papers; 'Inspect mode' lets the player click two conflicting fields to highlight a discrepancy; a rulebook lives on the same desk as a document (rules-as-document); Tactile feedback: 'coarse, clacking shutter', 'bright, haphazard stamp aligned over each passport' (Game Developer); chunky bitmap typography, no anti-aliasing; Technical minimalism on purpose: Pope credits the game's 'technical simplicity' and avoiding 'gobs of 3D assets'  
- Почему подходит: It is the canonical 'read documents inside a stylised world' game: the ECG strip can occupy the desk layer exactly as passports do, while the hospital scene stays small and desaturated in the upper band. Its rulebook-on-desk pattern maps 1:1 onto an ECG rule card (intervals, axis criteria) the learner drags next to the strip; inspect-mode highlighting maps onto 'click the abnormal segment'.  
- Риски: Pixel art collides with the team's exact-millimetre SVG strip (grid would alias); the oppressive grey-olive mood is at odds with 'catchy, engaging' for adult learners; a fully 2D fixed-screen layout wastes the Blender pipeline unless the world band is a rendered still.  
- Реализуемость в Blender: Easy for the world band (a single low-contrast orthographic still per location, downsampled with nearest-neighbour filtering to fake pixels); the desk/document layer should remain HTML/SVG, not Blender.

### Return of the Obra Dinn (Lucas Pope / 3909)
- Тип: game  
- Ссылка: https://obradinn.com/  
- Стиль: 1-bit dithered 3D with a cream paper logbook as the deduction interface  
- Визуальные черты: 'An Insurance Adventure with Minimal Colour' (official site): real-time 3D rendered as two-tone dither; Pope cites 1-bit early Macintosh games (Wikipedia); Dither is stable and world-anchored rather than screen-space noise: it 'tends to look like an applied texture', dots 'don't jump around' (Set Side B on Pope's TIGSource devlog); rendering routines were modified to add 'the equivalent of motion blur for this dithering approach' to fight motion sickness (Wikipedia); Selectable monitor palettes in options (ludo.guide / Steam community): Macintosh (default, pure #000000/#FFFFFF-ish), IBM 8503, IBM 5151 green phosphor, Commodore 1084 blue, Zenith ZVM 1240 amber, LCD; Document view: a logbook with crew sketches, roster and ship plan opens as a flat page with line drawings and serif text, totally separate from the dithered 3D world; the Memento Mortem watch freezes a scene so the player can study it; Output 16:9 only, letterboxed (Steam system requirements) – a fixed-aspect, low-resolution frame as a design constraint; Awards: IGF Grand Prize, BAFTA Game Design, The Game Awards Best Art Direction (official site)  
- Почему подходит: Shows that a monochrome world makes a document the only coloured, high-value object; an ECG strip (black trace on pink grid) would be the single chromatic element in a near-1-bit hospital. The 'freeze the moment, then deduce in the book' loop is the ECG loop: freeze a patient event, study the strip, enter rhythm/rate/axis in a logbook. Its monitor-palette menu is a ready-made idea: paper mode vs. IBM-green ICU-monitor mode.  
- Риски: Full 1-bit dither is visually taxing for long study sessions and eerie by nature; the strip's fine 1 mm grid must never pass through the dither (keep it SVG). Motion-sick-prone if animated; fine for stills.  
- Реализуемость в Blender: Easy to medium: render a clean grey-scale pass, then apply an ordered (Bayer) dither in the compositor or in post (Python/PIL); projecting the pattern in world space for stable animation is harder but unnecessary for still scenes.

### The Case of the Golden Idol (Color Gray Games / Playstack)
- Тип: game  
- Ссылка: http://www.thegoldenidol.com/  
- Стиль: frozen-moment 18th-century pixel scenes with a parchment fill-in-the-blanks 'thinking mode'  
- Визуальные черты: Two explicit modes: Exploring (point-and-click to collect keyword tiles from characters, objects, documents) and Thinking (fill blank slots in an account of events; the game reports whether a segment is 'entirely correct') – Wikipedia; Each case is a frozen tableau with looping animations; art drawn in Aseprite, built in Godot then Unity (Redux); references Gustave Doré and William Hogarth; intent to 'elicit a bit of nostalgia' in 1990s adventure players; Deliberately ugly-charming figures with heavy dark outlines; palette approx. muddy ochre #B48A4A, dusty red #8F3B2E, moss green #5B6B3A, parchment #EADBB0, soot #2B2420; The deduction layer is a flat parchment overlay with word tiles – no world rendering behind the text – so reading is noise-free; Direct lineage from Obra Dinn and Her Story (Wikipedia Development)  
- Почему подходит: Its keyword-tile + blank-slot sentence ('The rhythm is ___ at ___ bpm with ___ block') is a proven, satisfying way to make the player commit to an interpretation without free text, and it validates in segments – ideal for ECG rule application. The frozen scene = a frozen patient encounter with the strip.  
- Риски: Pixel art again conflicts with vector strip precision; the grotesque character style would clash with a clinical setting; dense tableaux can be noisy if copied literally.  
- Реализуемость в Blender: Hard to reproduce the hand-pixelled look faithfully; medium if you render low-poly scenes at ~400×225 and upscale nearest-neighbour. The thinking-mode UI is pure HTML/SVG and trivial.

### Strange Horticulture (Bad Viking / Iceberg Interactive)
- Тип: game  
- Ссылка: https://store.steampowered.com/app/1574580/Strange_Horticulture/  
- Стиль: candle-lit wooden shop desk with a hand-drawn identification book, map and specimen cards  
- Визуальные черты: Whole game is one desk: counter, customers at top, drawers; 'we opted for a tactile UI' like a board game rather than menus; map is 'a physical map that you drag out of your drawer and onto your desk', with paper sounds (Game Developer deep dive); Identification loop: compare an unlabelled specimen to the incomplete 'Strange Book of Plants' by scent, leaf and petal shape; correct deliveries unlock more pages; a labelling system lets you tag items for later (Wikipedia); Palette approx.: dark wood #3B2A1E, candle amber #E3A64C, bottle green #2F4F3A, parchment #E9DDC1, ink #1E1A17; 'mysterious ye olde world feel'; Hand-drawn ink illustrations of plants on cream pages; handwriting-style text; 2D only; tags Cozy/Dark/Atmospheric; Animations draw the eye to important items instead of a tutorial  
- Почему подходит: This is the ECG task in another costume: a reference book (ECG criteria), an unlabelled specimen (a strip), clues (patient letter/history), and a labelling system (your diagnosis). The warm parchment/wood palette is naturally harmonious with cream ECG paper and pink grid; the single-desk layout keeps the strip central with zero scene noise.  
- Риски: Tone is occult/gothic; the fully 2D desk forgoes the 3D hospital tour; too dim a palette could reduce strip legibility if copied exactly.  
- Реализуемость в Blender: Easy: a top-down or slightly tilted orthographic 'desk still' (wood, lamp, clipboard, coffee cup) is a trivial Cycles scene; the book/strip/cards are HTML/SVG overlaid on it.

### Tiny Room Stories: Town Mystery (Kiary Games)
- Тип: game  
- Ссылка: https://store.steampowered.com/app/1259640/  
- Стиль: rotatable isometric cel-shaded low-poly dioramas with tap-to-zoom object close-ups  
- Визуальные черты: 'Fully 3D levels that can and should be rotated to inspect them from another angle' (Steam); 'isometric cell-shaded art style', Unity (MobileSyrup review); Rooms are roofless boxes seen from above at ~35–45° in 90° rotation steps; interior walls cut away toward the camera; Flat or two-tone cel shading, soft ambient occlusion, almost no texture detail; palette approx. slate #4A5560, teal #4F8A8B, mustard #D9A441, brick #A4553D, off-white #ECE7DF; Objects (notes, keypads, drawers) open as centred close-up panels over a dimmed room – the standard mobile escape-room 'document view'; Detective/escape-room structure: 'a mixture of escape the room and classic quests'  
- Почему подходит: It is the closest shipped example of what a procedural bpy pipeline naturally produces: isometric low-poly rooms, toon shading, no hand-painting. Hospital rooms (reception, ward, ICU) as rotatable dioramas, with ECG strips popping up as close-up panels, is a direct transfer.  
- Риски: Grey-brown palette is a little dreary; rotation adds engineering if scenes are pre-rendered stills (render 4 views per room instead); generic look unless the palette is tuned to the ECG cream/pink/teal set.  
- Реализуемость в Blender: Easy: orthographic camera, Freestyle or inverted-hull outlines, Shader-to-RGB toon ramp (Eevee) or Cycles with flat diffuse + AO; cutaway walls via Boolean. Four 90° renders per room cover rotation.

### Rusty Lake / Cube Escape series (Rusty Lake studio)
- Тип: game  
- Ссылка: https://www.rustylake.com/  
- Стиль: flat 2D four-wall rooms with centred item close-ups, surreal muted palette  
- Визуальные черты: Studio self-description: 'eerie and atmospheric point-and-click adventures with an escape room feeling', 'surrealistic world'; Twin Peaks is the stated inspiration (Wikipedia); Navigation by four fixed wall views; tapping an object replaces the view with a large centred close-up (document, painting, device) against a flat backdrop; Flat vector-like shapes with thick dark outlines and almost no gradients; desaturated palette approx. #3A3F3B dark green-grey, #8A7A5A dirty ochre, #B8B2A0 bone, accent blood red #8E2A2A; Each entry is colour-themed (Cube Escape: Arles imitates Van Gogh 'to a limited degree' – HG101); Originally Flash, later ported; extremely low asset count per scene  
- Почему подходит: Cheapest proven pattern for 'wall view → object close-up → back' which an ECG game needs (monitor on wall → full-screen strip). Their colour-per-chapter approach suggests colour-coding hospital locations (ER red, cardiology teal) while keeping the strip constant.  
- Риски: Horror/surreal mood is wrong for medical learning; thick outlines and very dark tones would fight the strip if used in the close-up layer.  
- Реализуемость в Blender: Easy: render each wall of a room as a flat-lit orthographic still with Freestyle outlines and a 3-step toon ramp; close-ups are HTML.

### Monument Valley (ustwo games)
- Тип: game  
- Ссылка: https://ustwogames.co.uk/our-games/monument-valley/  
- Стиль: isometric pastel impossible-architecture, flat shading, every frame a print  
- Визуальные черты: 'Impossible Geometry … fantastical architecture and impossible geometry', 'Unfolding optical illusions' (ustwo page); influences: M. C. Escher, Middle Eastern architecture, Japanese flower arrangement, low-poly 3D (GDC 2015 'The Art of Monument Valley', Ken Wong); Strict orthographic isometric camera; unlit flat colour fills with large vertical gradients on sky/walls; no outlines, no textures; Unity; Ken Wong aimed to make each frame 'worthy of public display'; colour signals interactivity (Wikipedia); Palette approx. (chapter-dependent): salmon #F2B5A0, teal #5FB7B3, cream #F7EBD3, dusty mauve #C48CB3, indigo #3E4A7C, mustard #E6B85C; large uncluttered negative space; Minimal UI: thin geometric sans-serif, tiny chapter titles  
- Почему подходит: Demonstrates that a pastel isometric world can be calm yet 'catchy', and its salmon/cream/teal family harmonises with pink-grid ECG paper rather than competing. Negative space around a single focal object is exactly what a strip needs.  
- Риски: Architecture-puzzle vocabulary is unrelated to hospitals; without the impossible geometry the look can feel generic; portrait-first composition.  
- Реализуемость в Blender: Easy: orthographic camera, emission-only or very flat diffuse materials, gradient world background, no textures; renders fast on CPU with few samples.

### Assemble with Care (ustwo games)
- Тип: game  
- Ссылка: https://ustwogames.co.uk/our-games/assemble-with-care/  
- Стиль: hand-illustrated impressionist workbench where one object fills the screen  
- Визуальные черты: 'Handcrafted Visuals'; 'a story about taking things apart and putting ourselves back together' (ustwo); App Store copy calls it 'rendered in an impressionist style' with a 'fully hand-illustrated story' (via AppSpy); Repair view: a single object (camera, cassette player, watch) on a plain cloth/table, screws and parts dragged around it; nothing else on screen – the object is the document; Warm 'sun-soaked' palette approx. terracotta #D97B5B, teal #3E8E8C, cream #F5E9D6, mustard #E2B04A, plum #6B3F5B; soft painterly edges, visible brush texture, crayon-like character art; story in comic panels between repairs; Lead artist Chris Cox, art director David Fernández Huerta (Creative Review)  
- Почему подходит: The repair bench is the 'one artefact, full attention' layout: an ECG strip laid on a desk with callipers, a ruler and a pen, parts (intervals) you measure and tag. Warm cream/terracotta/teal is friendly, adult, and sits well next to pink-grid paper.  
- Риски: True impressionist hand-painting is not achievable procedurally; story panels would need an illustrator; mobile-first portrait framing.  
- Реализуемость в Blender: Medium: the bench still (table, cloth, tools) is easy; a painterly feel needs post-processing (Kuwahara/oil filters, paper grain overlay) rather than Cycles alone.

### Alba: A Wildlife Adventure (ustwo games)
- Тип: game  
- Ссылка: https://www.albawildlife.com/  
- Стиль: sun-lit low-poly Mediterranean with gradient-atlas shading and a species-cataloguing loop  
- Визуальные черты: 'Handcrafted visuals. Every little corner of the island has been looked after with great detail'; 'There are animals everywhere, can you find all the species?' – photograph and catalogue wildlife (Steam/official site); Production recipe (ustwo environment-art post): low-poly 'clean, simple shapes'; colours from on-location photos and painter Joaquín Sorolla; shading via UVs stretched across gradient colour atlases; opaque decals for floor/wall texture instead of tileables; baked lighting; no normal maps; boolean 'chipping' for worn edges; 4 terrain splats (dirt, clay, grass, sand); Palette approx.: sand #E8D4A8, sea teal #3FA7A3, whitewash #F6F1E8, terracotta roof #C8674A, pine #4F7A47, sky #BFE3F2; bright but low-contrast shadows; Soft outline-free silhouettes; third-person camera; UI is clean white cards with rounded corners and a field-guide list  
- Почему подходит: Its catalogue/identify loop (spot animal → photograph → match to guide entry) is the gamified version of 'spot pattern → match to ECG criterion'. The gradient-atlas technique is exactly what a bpy script can generate (colour ramps per material), giving the current pastel prototype more depth cheaply.  
- Риски: Open-world island does not map onto hospital interiors; gradient atlases need care to avoid banding on large walls.  
- Реализуемость в Blender: Easy: gradient shading = ColorRamp on a single UV coordinate or Object-space Z; decals via simple planes; baked or direct sun light with filtered shadows renders fast in Cycles CPU.

### Untitled Goose Game (House House / Panic)
- Тип: game  
- Ссылка: https://goose.game/  
- Стиль: untextured flat-colour low-poly English village with a lined-paper to-do list  
- Визуальные черты: 'low poly meshes, flat colours, and untextured 3D models' extending the 2D flat-colour look of Push Me Pull You (Wikipedia Development); Unity; Setting chosen for 'properness'; UK children's TV (Postman Pat, Fireman Sam, Brum) cited for its 'storybook' feel; Palette approx.: lawn #9CC46A, hedge #5E8F4A, cream render #F4EFE4, slate roof #7B8A99, brick #B8705C, sky #CFE6F3; shadows are soft, uniform, barely darker than base colour; Camera: slightly elevated, mild perspective, large calm compositions; no outlines; The only UI is a diegetic to-do list on a lined paper sheet in handwriting, ticked as tasks complete  
- Почему подходит: Proves flat-shaded untextured 3D is read as warm and charming rather than cheap – the ideal 'quiet' backdrop for a high-detail strip. Its paper to-do list is a model for a diegetic ECG checklist (rate ✓, rhythm ✓, axis …).  
- Риски: Mischief tone would need re-targeting; totally flat shading can make small hospital props unreadable without AO or bevel highlights.  
- Реализуемость в Blender: Easy: diffuse-only materials with a single sun lamp and large soft shadow, or Eevee/Shader-to-RGB with 2-step ramp; no textures at all, so CPU render is fast.

### Lumino City (State of Play Games)
- Тип: game  
- Ссылка: https://www.stateofplaygames.com/luminocity  
- Стиль: photographed paper-and-card miniature city with miniature lights, filmic grain  
- Визуальные черты: Made 'entirely by hand using paper, card, wood, miniature lights and motors' (State of Play); sets combine into a 'ten-foot high model city' and were shot with a Talos motion-control film rig (MCV); laser-cut parts; Characters built from photographs of coloured paper, animated in Flash, with code adding 'film grain and blur' so they sit in the plates (MCV); Look: visible paper edges and fibre, warm tungsten miniature lights, shallow depth of field, slight vignette; palette approx. kraft #C9A978, cream card #F3EBDD, warm bulb #FFD37A, teal paint #4E8C8A, brick-red paint #B5453B; BAFTA 2015 Artistic Achievement (Wikipedia); Gameplay hints live in a giant paper handbook the player pages through – the instructions are themselves a document  
- Почему подходит: Paper-cutout is the one 'craft' look that physically rhymes with ECG paper: a cream card hospital with a printed strip looks like one object family. The in-world handbook shows how a rulebook can be a beloved prop instead of a menu.  
- Риски: Real photography is out of scope; procedural paper can look like generic 'cardboard' if edges, grain and DOF are not convincing; dim tungsten light must not tint the strip.  
- Реализуемость в Blender: Medium: solidify-modifier card thickness, subtle translucency/SSS, procedural paper-fibre bump, filmic DOF and compositor grain are all scriptable; Cycles handles translucent card well but needs more samples (denoise).

### Two Point Hospital (Two Point Studios / SEGA)
- Тип: game  
- Ссылка: https://store.steampowered.com/app/535930/Two_Point_Hospital/  
- Стиль: claymation-style cartoon hospital, bright rounded forms, free isometric camera  
- Визуальные черты: Founders Webley and Carr (Theme Hospital's producer and lead artist) chose claymation-like visuals as 'future-proof' and because they make on-screen situations easy to read; critics compare to Aardman/Wallace & Gromit (Wikipedia); Unity; Rounded, bevelled furniture and chunky characters; saturated but soft palette approx. mint #9FD8C4, hospital white #F4F6F3, coral #F08A6A, teal #3C9A9C, mustard #F2C14E, grey-blue floor #B9C6CE; Free-rotating elevated camera, dollhouse cut-away walls, ambient-occluded clean floors; UI: rounded flat panels, bold humanist sans, pill-shaped buttons; Humour via 'Light-headedness to Cubism' illnesses; dense animated crowds  
- Почему подходит: Directly validates the hospital setting in a pastel, bevelled-low-poly style – essentially the team's current Blender prototype, proven commercially. Its readability-first rationale ('graphics support the game') is the right principle for an educational title.  
- Риски: Comedy diseases could undercut clinical credibility; busy crowds and sim UI are far noisier than a learning quest should be; must avoid looking like a Two Point clone.  
- Реализуемость в Blender: Easy: bevel modifier + smooth shading + soft area lights + AO is already what the prototype does; cutaway rooms via camera-facing wall culling.

### Botany Manor (Balloon Studios / Whitethorn Games)
- Тип: game  
- Ссылка: https://whitethorngames.com/botany-manor  
- Стиль: bright stylised 19th-century manor where clues are read from posters, letters and newspapers  
- Визуальные черты: 'an exploration puzzle game where you play as a retired botanist'; clues in 'botanical posters, newspapers, letters, paintings and postcards'; 'literally anything you encounter can be useful for your research'; objects can be turned and flipped (Whitethorn); Clues are collected into a notebook; a bloomed plant reveals an illustration and unlocks the next stage (Wikipedia); Unity; founder Laure De Mey ex-ustwo; references Darwin's Down House; Reviewers: 'bright', 'bouncy', 'picturesque'; stylised hand-painted-looking textures, soft daylight, no outlines; palette approx. sage #9DB58A, cream plaster #F3ECDC, oak #8A5E3B, botanical green #4F7F4A, rose #E3A0A8, sky #BFDDEB; Document view: picking up a letter/poster brings it to the centre of the screen, world blurred behind; serif Victorian typography on cream  
- Почему подходит: It is the closest tonal and structural analog: a calm stylised 3D building you walk through, where progress comes from reading documents and deducing conditions, then applying them to a specimen (plant → patient). Its cream/sage/rose palette is already ECG-paper-friendly.  
- Риски: First-person walking is heavier than point-and-click stills; hand-painted texture detail is beyond pure procedural generation; manor scale vs. clinical rooms.  
- Реализуемость в Blender: Medium: stylised interiors with soft daylight are easy; replicating painterly textures needs procedural noise + colour ramps; document close-ups are HTML.

### Her Story (Sam Barlow)
- Тип: game  
- Ссылка: https://www.herstorygame.com/  
- Стиль: diegetic 1990s police-database desktop (Apple II / Win 3.1 / Win 98 hybrid) as the whole interface  
- Визуальные черты: 'a police database full of live action video footage'; interface described by Barlow as 'part Apple II, part Windows 3.1 and part Windows 98'; 'the conceit of making the computer itself a prop in the game' (Wikipedia); L.O.G.I.C. database: search box, result list, 271 clips; checker grid turns red boxes green as clips are viewed – progress shown as data, not score; Footage run through two VHS players for period artefacts; dark desktop with cool greens/teals, bevelled grey window chrome; palette approx. desktop #0E1A1A, window grey #C0C0C0, highlight teal #2EC4B6, text green #9BE564; Everything the player reads is on one simulated screen; no world outside the monitor  
- Почему подходит: Shows a monitor can be the entire stage: an ICU/telemetry workstation with green-on-black traces, patient lists and a search/sort of past strips is a credible 'document mode' that contrasts with the paper mode. Its progress-as-data grid suits tracking which rules a learner has mastered.  
- Риски: FMV and retro OS chrome are irrelevant to Blender; retro-screen scanlines/blur would damage strip precision if applied to the ECG layer.  
- Реализуемость в Blender: Easy to irrelevant: the only 3D needed is a desk with a CRT/monitor as a framing still; the screen content is HTML/SVG.

**Выводы агента:**

- Every acclaimed 'read the evidence' game uses a strict two-layer architecture: a stylised, low-contrast WORLD layer (pixel, dither, flat low-poly, paper) and a flat, high-value DOCUMENT layer (cream/white paper, crisp black type, no perspective, no lighting). Papers Please, Obra Dinn's logbook, Golden Idol's parchment, Strange Horticulture's book, Botany Manor's letters and Goose Game's to-do list all keep the document outside the 3D pipeline. For the ECG game this means: Blender renders only backgrounds/props; the SVG strip, callipers and rule cards are always HTML overlays with their own white/cream background.
- Make the world darker and less saturated than the strip, never the reverse. Obra Dinn (1-bit), Papers Please (olive/grey) and Her Story (dark desktop) show that when the environment lives in mid/low values, a cream strip with a pink grid becomes the brightest, most chromatic object and needs no further emphasis. Practically: keep hospital-scene average luminance around 40–60 % and desaturate reds in the world so the #F4A6A6/#E57373 grid stays unique.
- Harmonise the world palette with ECG paper instead of avoiding it: Monument Valley's salmon/cream/teal, Assemble with Care's terracotta/teal/cream and Botany Manor's sage/rose/cream all sit comfortably next to pink-grid paper; complementary teal/mint (#4F8A8B, #9FD8C4) is the natural 'hospital' counterweight to the grid's pink and is already in the team's prototype.
- The commit-to-a-diagnosis mechanic is solved: Golden Idol's word tiles dropped into blank slots with per-segment validation, and Obra Dinn's book entries, are far more satisfying than multiple choice. An ECG 'thinking mode' sentence ('Rhythm __ , rate __ , PR __ , QRS __ , axis __ , conclusion __') with drag-in tokens from the strip and the rule card is a direct, proven design.
- The reference book as a diegetic prop (Strange Horticulture's Book of Plants, Lumino City's paper handbook, Papers Please's rulebook, Alba's species guide) outperforms a help menu: it makes rule lookup part of play and lets the game withhold/unlock pages as a progression system – ideal for staging ECG rules from rate/rhythm to blocks and ischaemia.
- Freeze-frame is the right temporal model: Obra Dinn and Golden Idol freeze a scene so the player can study it indefinitely; for ECG, each encounter can be a frozen diorama still (one Cycles render) plus a live SVG strip, which also removes any need for animation on the CPU-only pipeline.
- Flat/gradient-shaded untextured low-poly (Untitled Goose Game, Alba, A Short Hike – https://ashorthike.com/ , flat shading, no anti-aliasing, soft outline) is both the cheapest Cycles workload and the least visually noisy world style; Alba's gradient-atlas trick (colour ramp over a single UV/Z coordinate) is one line of bpy node setup and adds depth without textures.
- Two looks that physically rhyme with the ECG artefact: paper-cutout/card miniatures (Lumino City) for the 'paper strip' chapters, and a dark diegetic monitor (Her Story; Obra Dinn's IBM 5151/Zenith palettes) with green/cyan trace (#00FF7F / #00E5FF on #0B0F10) for ICU/telemetry chapters. Switching between the two by location (ward = paper, ICU = monitor) gives variety without changing the strip geometry.
- Avoid the hand-pixelled route (Papers Please, Golden Idol, Unpacking – https://www.unpackinggame.com/) for the main art: pixel grids alias against a millimetre-precise SVG strip and cannot be produced procedurally in Blender with the same charm; if a retro feel is wanted, downsample only the world band and keep the strip vector.
- Hospital-specific precedents (Theme Hospital 1997 – https://www.gog.com/game/theme_hospital ; Two Point Hospital) confirm that rounded, claymation-like bevelled props read clearly from an elevated isometric camera, but their comedic tone and crowd density are the main things to avoid; keep rooms sparse (3–6 props), one patient, one staff member.
- Typography lesson from the document games: period/handwritten faces for in-world letters (Strange Horticulture, Golden Idol), but measurement UI should use a neutral humanist sans plus a monospace for numbers (ms, mV, bpm) so values align under the strip; never place type over the grid.
- Outlines are optional, not mandatory: Monument Valley, Goose Game and Alba have none and remain readable through colour separation and soft AO; Tiny Room Stories and Rusty Lake use outlines mainly to keep tiny mobile objects legible. For desktop/HTML presentation, a 1–2 px Freestyle line only on silhouettes is enough if used at all.
- Monochrome-plus-one-accent (Obra Dinn; Lorelei and the Laser Eyes – https://simogo.com/work/lorelei-and-the-laser-eyes/ , 'black and white', 'line rendering and vector art', red accent) is a cheap, striking option for emergency/arrhythmia chapters where the only colour is the strip's grid and a red alarm – usable as a mode, not the whole game.
- Calm-but-catchy titles that are less relevant mechanically but confirm the palette direction: Gris (https://store.steampowered.com/app/683320/GRIS/ , watercolour, 'delicate art'), Florence (https://annapurnainteractive.com/en/games/florence , slice-of-life webcomic panels), Townscaper (https://www.townscapergame.com/ , 'No goal… plenty of beauty'), Lost in Play (https://www.happyjuice.games/ , 'feel like you're playing a cartoon'), Machinarium (https://amanita-design.net/games/machinarium.html , hand-drawn, hint sketches as a document). All are hand-drawn or painterly and therefore hard to generate with bpy; borrow their palettes and framing, not their technique.

## Существующие продукты для обучения ЭКГ

### SkillStat Six Second ECG Simulator
- Тип: game  
- Ссылка: https://www.skillstat.com/tools/ecg-simulator/  
- Стиль: white trace on saturated orange gradient panel, arcade timer HUD  
- Визуальные черты: Strip panel 928x157 px: orange gradient background (#FF6326 / #FB5616 with lighter swooshes) over which a 1 mm/5 mm grid is drawn as semi-transparent white lines (rgba(255,255,255,0.33) minor, 0.5-1.0 major). Lead II only, no calibration pulse, no true mm scale.; Trace is a white ~2 px sprite PNG (2654x90 px per rhythm) scrolled with a CSS keyframe animation (20 s linear infinite, repeat-x) to fake a live monitor sweep; hovering freezes it. Learn mode uses the identical panel in blue (#3C96D2).; HUD: 'HEART RATE' numeral 60 px bold white with hard 4 px black drop shadow; page background pale mint-grey gradient (#E7EFED to #F9FBFA); stats text teal #005071; selected rhythm name #FF6600; outer site typography Poppins/Spectral, accent #05AAEB.; Game loop: PLAY/RESET/STOP, mm:ss timer, counters 'Rhythms / Correct / Attempts', Novice (3 tries) vs Practitioner (1 try), 27 rhythms from an XML list, heartbeat and right/wrong sounds. Free, HTML5 (Flash port), SkillStat claims 15M+ downloads.  
- Почему подходит: Proves a timed name-the-rhythm micro-game works with almost no chrome; a good template for an ER/ICU 'glance at the monitor' mini-game inside the quest.  
- Риски: Saturated orange fights the pink/cream paper palette; the white-on-orange grid loses millimetre precision so intervals cannot be measured; 2013-era design reads dated.  
- Реализуемость в Blender: Easy but not recommended for the strip itself: an emissive plane with gradient + grid texture is trivial in bpy, yet the sweep animation and readability belong in HTML/SVG, not in a render.

### ECG Stampede (app + curriculum)
- Тип: game  
- Ссылка: https://www.ecgstampede.com/app/  
- Стиль: clean white-card learning app, pastel pink ECG-paper motif, colour-coded triage urgency  
- Визуальные черты: Glossary/practice strips are schematic: ~2 px near-black trace (#323232) on pale pink paper #FDEDED with 1 mm/5 mm lines #DEA9A9, same geometry as real paper, lead labels, grey bull mascot watermark in the corner.; UI chrome: white cards with 1 px borders and soft shadow, dark-grey Lato-style sans headings, black primary button; page header is a blush gradient with a faint pink ECG-line illustration; a thin 4-colour top stripe (#EEEDA7 yellow, #9CD7F2 blue, #FEC7CD pink, green).; Acuity choices are colour-coded tiles: 'Code STEMI' red text #B12535 on tint #FEEFF0, 'Room Immediately' orange on tint #FDF2DE, lower acuities in cooler tints; small rounded icon squares (flame, speedometer).; Stampede mode: 10 ECGs, limited beds that fill up, cannot revisit, warnings for over/under-triage, missed STEMI counts as an error (WestJEM / JETem papers); 10-unit curriculum with 57 video lessons; first two units free, then subscription (iatroX, Sept 2026: Basic $59.99/yr, Pro $199.99/yr incl. CME). iOS, Android, web (WordPress/LearnDash).  
- Почему подходит: Closest existing product to the author's 'apply rules, make a decision' goal; shows the pink-paper strip can double as brand motif and that engagement comes from scarcity (beds) and urgency, not visual noise.  
- Риски: White-card UI is generic; strips are schematic, not real recordings; competitor-written reviews (iatroX) are the only third-party commentary.  
- Реализуемость в Blender: Easy: nothing is 3D; the strip style is exactly what the team's SVG renderer already produces; the rest is HTML cards.

### ECG Wave-Maven (BIDMC / Harvard)
- Тип: app  
- Ссылка: https://ecg.bidmc.harvard.edu/maven/mavenmain.asp  
- Стиль: early-2000s ASP quiz site, red-grid GIF ECGs, dark-red and cream palette  
- Визуальные черты: Each case is a single 800x400 16-colour GIF 12-lead (3x4 layout plus lead II rhythm strip): black trace on white, red grid (#DC9696 minor, saturated red 5 mm), blue lead labels (#0000FF), calibration pulses, monospace copyright footer; no zoom or caliper tool.; Stylesheet maven.css: dark-red headings/borders #5C0303, dusty-pink panels #DCC7C7, cream #FFF8CB, indigo links #2F3396, Helvetica/Arial; GIF logos; a demographic survey form gates the first case.; Multiple-choice question with 1-3 star difficulty rating, quiz mode (answer hidden) vs reference mode, random / most recent / search by diagnosis; 500+ cases drawn directly from the hospital ECG repository (Nathanson et al., AMIA 2001, PMC2243537; Med Educ Online 2003).  
- Почему подходит: Shows that red-grid-on-white paper plus MCQ carries content even with dated design; a baseline for what 'dry' looks like.  
- Риски: Walls of text, no feedback animation, GIF artefacts, survey-gate friction; visually the least engaging of the set.  
- Реализуемость в Blender: Not applicable as a style; the paper look is trivially reproduced in SVG.

### Life in the Fast Lane ECG Library
- Тип: app  
- Ссылка: https://litfl.com/ecg-library/  
- Стиль: scanned hospital printouts on a white blog with red accents  
- Визуальные черты: Real scanned ECGs (JPEG ~1024 px wide) with faded pink paper #ECE0DD and lines #D2BEC0 / #C8B8B6, black trace with baseline wander and noise; sometimes coloured arrows or boxed annotations.; Page: white background, Open Sans, dark navbar, red link colour #FA4242, green CC BY-NC-SA badge; sections ECG Basics, A-Z by diagnosis, Top 100, 'ECG Exigency' cases.; Images may be reused for non-profit teaching with credit to litfl.com.  
- Почему подходит: Reference for how authentic strips look (faded pink, noise, wander); useful for 'real-world' cases next to the team's clean schematic strips.  
- Риски: Pure reference, no game; NC licence; low-res scans upscale poorly.  
- Реализуемость в Blender: Easy: scans as textures on slightly curled paper planes.

### Dr. Smith's ECG Blog
- Тип: app  
- Ссылка: https://drsmithsecgblog.com/  
- Стиль: raw machine printouts (GE MUSE blue grid, Philips pink) inside long-form case narratives  
- Визуальные черты: GE MUSE viewer screenshots: pale blue-grey grid (#EEF1F8 paper, #BBC2C7 lines), black trace, machine measurement table and green 'Signed' badge; Philips printouts: pink paper #F6E3E4, lines #CFACB0.; WordPress theme: navy #1A222F primary, blue accent #2066F5, Raleway headings; serial ECGs stacked chronologically with expert commentary and Queen of Hearts AI annotations.; Blog moved from hqmeded-ecg.blogspot.com (redirects).  
- Почему подходит: Proves real strips come in both pink and blue grids; the blue-grid variant harmonises with a mint/teal room palette; 'case unfolding over serial ECGs' is a natural quest structure.  
- Риски: Dense expert-level prose, no interactivity.  
- Реализуемость в Blender: Easy (textures only).

### ECGpedia
- Тип: app  
- Ссылка: https://en.ecgpedia.org/  
- Стиль: MediaWiki textbook with vector schematic strips on pink grid and soft pastel anatomical illustrations  
- Визуальные черты: Schematic strips: black ~1.5 px trace on pink paper #FBE0E2 with 1 mm/5 mm lines #E0B2B4, lead labels at left, pink caption text (e.g. the LQT1/2/3/8 comparison figure).; Anatomical and conduction illustrations in soft pastel vector: teal myocardium, lilac atria, yellow conduction bundle; illustrator Rob Kreuger credited; default Vector skin, white page, CC BY-NC-SA.  
- Почему подходит: Demonstrates the clean schematic-on-pink style the team's SVG renderer can reproduce exactly, plus a pastel anatomical palette (teal/lilac/yellow) that coexists with the pink grid.  
- Риски: Wiki chrome is dull; NC licence on figures.  
- Реализуемость в Blender: Easy: flat pastel materials, no textures; toon/flat shading matches the illustration look.

### ECG Academy (Dr. Nicholas Tullo) - ChalkTalks
- Тип: app  
- Ссылка: https://www.ecgacademy.com/  
- Стиль: hand-annotated real strips with neon marker colours over white 'whiteboard' slides  
- Визуальные черты: Real rhythm strips and 12-leads scanned to greyscale (paper #F3F3F0, faint grid, black trace) overlaid with handwritten marker annotations in magenta #9C508E, green, blue and cyan; circles, calipers and arrows drawn live; magnifier inset in marketing imagery.; ~800 six-minute 'ChalkTalk' videos plus step-by-step lessons and monthly live masterclasses; free intro tier, monthly/annual subscription, CE/CME tiers; site uses a plain white layout with grey trust logos.  
- Почему подходит: The handwritten annotation layer is an engaging 'mentor explains' device that leaves the strip readable; good model for feedback screens after a decision.  
- Риски: Video-only; marker colours need taming to fit the palette.  
- Реализуемость в Blender: Not applicable (SVG overlay with hand-drawn stroke filters in HTML).

### 12 Lead ECG Challenge (Limmer Education / LC Ready)
- Тип: app  
- Ссылка: https://apps.apple.com/us/app/12-lead-ecg-challenge/id461149429  
- Стиль: flash-card app: scanned pink-grid 12-leads with red arrows under a slate-blue header  
- Визуальные черты: 180 real 12-leads (Tom Bouthillet) as scans: paper #EED4CC, lines #E0C4BC, black trace, red annotation arrows; magnifier icon opens the full image.; UI: slate-blue header, light-grey body, thin blue progress bar, 'Study Card N' answer text; store marketing on a blue-to-green gradient; $5.99; sets of 5/10/20 cases.; Reviewers complain there are no quiz questions, only look-then-read.  
- Почему подходит: Minimal viable 'look at strip, decide, read answer' loop and the red-arrow annotation convention.  
- Риски: Dry; low-res scans hard to read on phone; mixed ratings.  
- Реализуемость в Blender: Not applicable.

### Resuscitation! (EM Gladiators)
- Тип: game  
- Ссылка: https://www.imedicalapps.com/2012/10/resuscitation-app-patient-simulation/  
- Стиль: 2012 glossy iOS dark UI, cartoon patient on gurney, black bedside monitor  
- Визуальные черты: Near-black background #050608, blue glossy gradient buttons (#192E5D / #34538C), grey bevels; action scoreboard colour-coded Critical/Bonus green, Neutral/Unnecessary yellow, Harmful red.; 'Place Monitor' black screen that then shows the live rhythm with real-time deterioration when choices are poor; vector cartoon patient; history/exam shown as white-on-black text modals; scoring from student to attending.; Verification note: App Store pages (US/FR/GB/CA) and Google Play returned 404 on 2026-10-10, so the app appears delisted; the 2012 iMedicalApps review and casimedicos product page remain as sources.  
- Почему подходит: Shows that engagement can come from consequence (monitor changes as you act) rather than art.  
- Риски: Dated skeuomorphism, heavy dark UI, product likely unavailable.  
- Реализуемость в Blender: Easy to emulate (dark room + emissive monitor) but the style is not worth copying.

### Full Code Medical Simulation
- Тип: serious-game  
- Ссылка: https://fullcodemedical.com/  
- Стиль: semi-realistic 3D ED/ambulance scenes with photoreal props and a black wall monitor  
- Визуальные черты: Rendered 3D rooms: grey-blue walls #A3B6CA, whites #E6E6E7, navy #3B5172, 23 semi-realistic patient models, LIFEPAK-style transport monitor in the ambulance.; Wall monitor: black #090909 with green ECG trace; numerics HR green, Temp white, O2 cyan, BP red, RR yellow (standard clinical colour code).; UI: white rounded side tabs (Patient / Exam / Stabilize / Differential on the left, Investigate / Intervene / Communicate / Hand-off on the right), avatar badges for attending and nurse, brand purple/teal; 250+ peer-reviewed cases, AI patient dialogue, CME; web, tablet, mobile, free trial.  
- Почему подходит: Nearest existing 'hospital locations + patient + monitor + decisions' structure; shows the monitor as a small dark island inside a light room.  
- Риски: Realistic humans drift into uncanny valley and are expensive; ECG is a secondary, small element.  
- Реализуемость в Blender: Hard as-is (PBR assets, rigged characters, Cycles CPU render times); medium if rooms are rebuilt as stylized low-poly.

### Prognosis: Your Diagnosis (Medical Joyworks)
- Тип: game  
- Ссылка: https://apps.apple.com/us/app/prognosis-your-diagnosis/id392489854  
- Стиль: flat text-first case game, navy-to-sky gradient, medal scoring  
- Визуальные черты: Vertical background gradient #053B52 (top) to #D4E8F1 (bottom); white cards; tabs PLAY / REVIEW / DISCUSS with yellow underline; checkbox lists for investigations and management.; Score shown as a silver medal with percentage and 'Try again / View analysis'; 400+ cases, free; almost no imagery, no ECG emphasis.  
- Почему подходит: Lightweight gamification (score, medal, retry) with the three-tab play/review/discuss structure that maps to quest/feedback/teaching screens.  
- Риски: Text-heavy, little visual identity; teaches nothing about strip rendering.  
- Реализуемость в Blender: Not applicable.

### Laerdal LLEAP Patient Monitor / Monitor by Laerdal
- Тип: studio  
- Ссылка: https://laerdal.com/information/patient-monitor-options-lleap-and-simpad-plus/  
- Стиль: clinical patient-monitor realism: colour-coded waveforms on black  
- Визуальные черты: Black background #100F0D; ECG green (#52B737 trace, brighter numerals), Pleth/SpO2 yellow #C2CA23, ABP red #CC2A34, PAP yellow, CO2 white; large bold numerics in a right column colour-matched to each waveform; 12-lead view, alarm limits (LLEAP spec sheet 14-14353).; Monitor by Laerdal offers skins replicating ZOLL, LIFEPAK 15, Tempus Pro and IntelliVue plus a generic monitor; LLEAP home screen uses grey Metro-style tiles.  
- Почему подходит: Canonical colour code learners already know; use it for ICU/ER scenes and reinforce 'monitor = rhythm, paper = 12-lead'.  
- Риски: Commercial sim software, not a game; branded hardware looks need care.  
- Реализуемость в Blender: Easy: emissive plane with a procedural or baked trace texture, bloom via compositor Glare node; CPU-friendly.

### Nasco Life/form Interactive ECG Simulator (101-102 / LF03670)
- Тип: studio  
- Ссылка: https://shop.nascohealthcare.com/products/101-102  
- Стиль: cream plastic rhythm box with blue-violet membrane buttons feeding a real monitor  
- Визуальные черты: Beige/cream housing; 17 labelled rhythm keys printed in blue-violet (VF, VT fast/slow/poly, AFIB, AFLTR, SVT, S TACH, NSR, ASYS, SINUS+PVC, S BRDY, J BRDY, 2nd I, 2nd II, 2nd II+PVC, 3rd), 'convert' and adult/ped keys; colour-coded 3-/4-lead snap posts (red, black, white, green); defib pads on top.; Outputs 3- or 4-lead signals to a real monitor, supports pacing and defibrillation; about $1,200-1,230.  
- Почему подходит: A real artefact for cardiology-office/ICU props, and the labelled rhythm-button grid is a ready-made UI metaphor (rhythm palette).  
- Риски: Hardware only, no screen of its own.  
- Реализуемость в Blender: Easy: bevelled box with text decals; a few minutes of bpy.

### Reanimation Inc. (Dmitrii Lomakin)
- Тип: game  
- Ссылка: https://store.steampowered.com/app/1089820/Reanimation_Inc/  
- Стиль: flat-shaded low-poly 3D ambulance, pastel mint/coral/orange UI, black monitor with green and cyan traces  
- Визуальные черты: Scene palette: white #EAEBEA, mint-teal #5ACBB0, green #4FC17C, coral #DD5E60, orange #BC4929, tan #C4986C; unlit flat shading, no textures, rounded props, pill-shaped icon buttons (Research green, Actions red, Medication cyan).; Monitor: black #151515, ECG trace #11EA79 ~2 px, HR numerals #04FB81, pleth #0CF2E4, NIBP #F70A05, RR yellow; white bezel with cyan soft keys and a red button.; Realistic protocols (defibrillation, drugs, MI vs angina by ECG), content reviewed by doctors/paramedics; $9.99, Steam Nov 2019, also mobile.  
- Почему подходит: The closest existing analogue to the author's stylized-3D Blender prototype: pastel low-poly room plus a dark monitor island keeps the ECG legible and still feels like a game.  
- Риски: Toy-like look may undercut seriousness for residents; saturated red/orange UI overload; thin trace on black reads poorly at small size.  
- Реализуемость в Blender: Easy: flat/emission materials, no textures, Cycles at low samples renders fast on CPU; optional Freestyle outlines.

### Lecturio ECG Interpretation course and 'Understanding a Normal ECG' infodoc
- Тип: app  
- Ссылка: https://www.lecturio.com/medical-courses/electrocardiogram-interpretation.course  
- Стиль: flat vector infographic: navy type, mint and coral pill tags, pink-grid paper strip  
- Визуальные черты: Infodoc (cdn.lecturio.com/assets/Lecturio_Cardiology_ECG_Infodoc.pdf): light blue-grey background #E6EBF3, dark navy headings #2D2D2D, green pills #ADD59A, coral pills #D36C6C / #DC989A, flat heart illustration with a pink ECG line, and a pink-grid paper strip with black trace emerging from a drawn ECG machine.; Course: Dr. Joseph Alpert, 44 videos and 97 questions inside the cardiology course; concept pages show a normal 12-lead with V1 rhythm strip and a labelled schematic of waves/intervals; free account unlocks ~20%.  
- Почему подходит: Its mint/coral/navy plus pink-grid palette is nearly the author's pastel palette and demonstrably reads as 'medical education'.  
- Риски: Lecture-video format; mint/coral pills can look like generic SaaS marketing.  
- Реализуемость в Blender: Easy (flat materials); mostly an HTML/SVG reference.

### AMBOSS 'EKG' knowledge article (German)
- Тип: app  
- Ссылка: https://www.amboss.com/de/wissen/ekg  
- Стиль: textbook knowledge base: greyscale scanned printouts plus schematic figures, blue UI  
- Визуальные черты: Content images are greyscale scans of real printouts (grey 1 mm/5 mm grid, black trace) and figures labelled 'schematisch', Cabrera circle and electrode-placement diagrams; lead tables; collapsible sections and 'Praxistipp' callouts about counting grid squares.; UI colours: buttons #5C90FA / #2668F8, dark #29333C; an 'overlay' feature lets users compare their findings in practice cases.  
- Почему подходит: German-language terminology reference for the team and evidence that neutral greyscale scans are an accepted alternative to pink paper.  
- Риски: Subscription-only, dense reference.  
- Реализуемость в Blender: Not applicable.

### 'Shocking Escape' cardiovascular escape room (Morrell & Eukel)
- Тип: research-paper  
- Ссылка: https://stti.confex.com/stti/nerc20/webprogram/Paper101770.html  
- Стиль: physical escape room: printed strips, padlocks, nine sequential puzzles  
- Визуальные черты: 60-minute room with 9 sequential puzzles; correct answers open locks and decode clues; content includes ECG rhythm-strip analysis, shock types, cardiac drugs, drip calculations (Simulation & Gaming 2021;52(1):72-78 gives design and materials).; Mixed-methods outcome: pre/post knowledge 58% to 61% (p<0.05), strongly positive perception ratings; a related UPMC virtual escape room on arrhythmias and a Brazilian RCT (NCT06266845) exist.  
- Почему подходит: Lock/code mechanics for in-game puzzles (crash cart, ICU door) where the correct ECG interpretation is literally the key.  
- Риски: Visual design undocumented; small learning effect.  
- Реализуемость в Blender: Easy: lockbox and crash-cart props.

**Выводы агента:**

- Nearly every serious ECG product shows the strip as paper (pink/red grid, black trace) and never restyles it; engagement comes from the frame around it (timers, bed scarcity, scores, consequences), not from decorating the strip. The team's exact-mm SVG strip is already best-in-class; keep it untouched and invest in the frame.
- Two canonical displays coexist and are used for different tasks: monitor (black, green ECG ~#11EA79/#52B737, cyan pleth, red BP, yellow RR; Laerdal, Full Code, Reanimation Inc) for live rhythm and emergencies, and paper (pink #FDEDED-#FBE0E2 with lines #DEA9A9-#E0B2B4, or GE-blue #EEF1F8/#BBC2C7) for 12-lead diagnostic reading. Mapping monitor to ER/ICU scenes and paper to ward/cardiology-office scenes matches learner expectations.
- The one product that strongly 'designs' the strip (SkillStat: white trace on saturated orange) loses millimetre readability and clashes with paper colours; avoid saturated or dark-coloured backgrounds behind the trace. Real strips also appear on neutral greyscale grids (AMBOSS, ECG Academy scans), which harmonise with any room palette.
- The most engaging mechanics found: ECG Stampede's four colour-coded acuities (red Code STEMI, orange Room Immediately, cooler tints below) with limited beds and no backtracking; SkillStat's timer and Novice/Practitioner tries; Resuscitation!/Reanimation's monitor that deteriorates in real time; Prognosis's medal score with play/review/discuss tabs; escape-room locks opened by correct interpretation.
- Modern ECG apps use neutral chrome: white cards, one accent, Lato/Open Sans/Poppins, soft shadows, and a thin pink ECG line as a brand motif (ECG Stampede), which naturally harmonises with grid colours. Dated ones (Wave-Maven, 2012 Resuscitation!, EKG Academy app) feel dry because of dark heavy UI or walls of text with no spatial context.
- Reanimation Inc. is the closest analogue to the author's Blender prototype (flat-shaded low-poly mint/coral/orange ambulance + black monitor island) and proves pastel stylized 3D keeps a monitor ECG legible; Full Code shows the realistic-3D alternative is expensive and pushes the ECG into a minor role. Stylized low-poly with Cycles CPU is the right trade-off.
- Annotation conventions worth adopting for feedback screens: red arrows on scans (12 Lead ECG Challenge, LITFL), handwritten neon marker over greyscale strips (ECG Academy ChalkTalks), schematic side-by-side comparison strips with pink captions (ECGpedia). All are SVG overlays, not 3D.
- Pastel palettes already proven in ECG education: Lecturio infodoc (bg #E6EBF3, mint #ADD59A, coral #D36C6C, navy) and ECGpedia illustrations (teal/lilac/yellow) sit comfortably next to pink-grid paper, supporting the author's cream/mint/teal/coral direction.
- Verification caveats: no credible 'Code Blue' ECG video game or 'Rhythm Trainer' app could be confirmed (dropped); Resuscitation! store pages now 404 (likely delisted); Osmosis and Medmastery pages block bots so their visual style could not be verified first-hand; Google Play's ECG Stampede listing returned unrelated screenshots, so only App Store/official-site imagery was used for it.

## Наука об обучении: когнитивная нагрузка и визуальный дизайн

### Fiorella & Mayer (2021) — Principles for Reducing Extraneous Processing (coherence, signaling, redundancy, spatial & temporal contiguity), Cambridge Handbook of Multimedia Learning, 3rd ed., ch. 14, pp. 185–198
- Тип: research-paper  
- Ссылка: https://www.cambridge.org/core/books/cambridge-handbook-of-multimedia-learning/principles-for-reducing-extraneous-processing-in-multimedia-learning/F29A19FCD34C542806F736E0661C05F5  
- Стиль: "Coherence-first" focal hierarchy: one high-frequency element (the strip), everything else low-frequency and quiet  
- Визуальные черты: COHERENCE: anything on screen that is not needed to apply the current ECG rule is extraneous load. Secondary summaries of Mayer's chapters report coherence supported in 23/23 experiments, median d ≈ 0.86 (strongest of all principles); signaling 24/28, median d ≈ 0.41 (not verified against the 2021 full text, which is paywalled).; SIGNALING: add cues that show HOW the essential material is organised — on the strip this means a persistent, low-alpha colour band over the interval the rule concerns (e.g. PR segment), a bracket with the millimetre count, and the rule card using the same hue. Not arrows all over the room.; SPATIAL CONTIGUITY: put the rule text and the measurement next to the trace (callout anchored to the complex), never in a side panel the eye must travel to; put lead names on the strip, not in a legend.; TEMPORAL CONTIGUITY: when the mentor explains a feature, the highlight on the strip must appear at the same moment as the sentence, not after a click.; REDUNDANCY: do not show the mentor's spoken line AND a full transcript AND a tooltip; one verbal channel (short on-screen text is fine for a silent game).; Practical screen-area rule derived from the above: strip ≥ 45–60% of viewport when a case is open; environment visible only as a dimmed frame; pure black ink #141414 on paper, grid 1 mm #F4C7C3 / 5 mm #E9A3A0 on cream #FFFBF5 so the grid reads at ~1.5:1 / ~2.2:1 (present but receding) while trace-to-paper contrast is >15:1.  
- Почему подходит: The whole game's learning object is a single dense visual pattern. The three Mayer principles with the biggest and most replicated effects (coherence, contiguity, signaling) translate directly into (a) a strict prop/texture budget for the Blender room, (b) overlay-based signaling drawn in the team's existing SVG, (c) anchoring rule text to the trace. They also give the author's requirement 'not too distracting' an operational definition.  
- Риски: Effects were measured with short (6–12 min) lessons and novices; signaling can backfire if cues are dense or inconsistent (see Schneider 2018 'blinking' result). Over-applying coherence makes a sterile game; keep décor, but away from the strip and at low spatial frequency.  
- Реализуемость в Blender: easy — bpy can enforce a per-scene prop count, keep materials flat/low-noise (no procedural noise textures near the strip's screen region), and the compositor can desaturate/blur the background when the strip is enlarged (Cycles DoF or a compositor blur node; CPU cost moderate). Signaling and contiguity live in HTML/SVG, not Blender.

### Sundararajan & Adesope (2020) — Keep it Coherent: A Meta-Analysis of the Seductive Details Effect, Educational Psychology Review 32:707–734 (58 studies, >7,500 learners)
- Тип: research-paper  
- Ссылка: https://doi.org/10.1007/s10648-020-09522-4  
- Стиль: No decorative detail adjacent to the diagram; décor only where it cannot compete  
- Визуальные черты: Overall small-to-moderate negative effect of interesting-but-irrelevant material (secondary sources report g ≈ −0.33; strongest subgroups ≈ −0.70). Press release: https://news.wsu.edu/press-release/2020/03/19/seductive-details-inhibit-learning/; Harm is LARGER when the seductive detail sits NEXT TO an informative, relevant diagram → nothing cute (posters, plush toys, wall art, animated monitors, patient photos) within the strip's bounding box or its margins; keep a clear 'ink-only' margin ≥ 2 grid cells (10 mm) around the paper.; Harm is larger when the detail is CONSTANT/STATIC (a permanent joke or image) → avoid permanent decorative items in the case-review layout; transient narrative beats (a nurse walking in, a phone ringing) belong to scene transitions, not to the strip-reading screen.; Learners with low prior knowledge and low working-memory capacity are most vulnerable (Park et al. 2015 eye-tracking; Sanchez & Wiley) → the beginner tier (students, nurses) needs the plainest strip screens; décor can scale up with level.; Detail that is DIRECTLY related to the learning objective is not seductive: a patient's visible pallor, an IV pump, a defibrillator cart near a VT strip are legitimate cues; a potted plant next to the strip is not.  
- Почему подходит: Gives the art director a yes/no test for every prop: 'Would a cardiologist use this to decide?' If no, it must not be in the strip's neighbourhood. This is the research basis for the author's 'catchy but not distracting' brief and directly constrains the pastel diorama: keep it as the hub/transition world, strip the case-reading screen down.  
- Риски: Most studies are short lab sessions measuring cognitive outcomes only; motivational benefits of décor in a long game are not captured. Format moderator findings are inconsistent between the press release and other summaries; cite the paper for exact numbers.  
- Реализуемость в Blender: easy — procedural scene generation can expose a 'decor_level' parameter (0 for strip-reading camera, 1–2 for exploration), and the camera for case screens can frame only neutral surfaces (desk, wall) behind the paper.

### Schneider, Beege, Nebel & Rey (2018) — A meta-analysis of how signaling affects learning with media, Educational Research Review 23:1–24 (103 studies, N = 12,201); German summary by TUM Clearinghouse Unterricht (Kurzreview 22)
- Тип: research-paper  
- Ссылка: https://doi.org/10.1016/j.edurev.2017.11.001  
- Стиль: Static colour highlighting on the picture; never blink  
- Визуальные черты: Overall: retention g = 0.53, transfer g = 0.33; signaling lowers cognitive load (g = 0.25), slightly raises motivation (g = 0.13); eye-tracking confirms learners dwell longer on signaled parts (g = 0.39). (TUM summary: https://www.clearinghouse.edu.tum.de/wp-content/uploads/2018/12/CHU_KR-22_-Schneider_2017_Lernmaterial_Hervorhebungen.pdf); Signals IN PICTURES, by type (retention/transfer g): COLOUR highlighting of a part of the picture 0.44*/0.39* (significant, best single type); arrows/pedagogical agents 0.33*/0.21; labels 0.32/0.38 (ns); spotlight circle 0.17/0.29 (ns); BLINKING −0.56/−0.47 (harmful). Mixed signals 0.77*/0.48*.; Permanent signals 0.58*/0.31* vs temporary 0.46*/0.35* → keep the interval highlight ON while the learner measures, don't flash it.; Low prior knowledge 0.42*/0.39* and high 0.67*/0.55* both benefit → no expertise-reversal; keep signals at all levels but let the player toggle them off.; Supporting primary study — Ozcelik et al. 2009 (Computers & Education 53:445–453, n = 52, eye-tracking): colour-coding corresponding parts of text and illustration improved retention and transfer; mechanism = faster search for the matching element. https://doi.org/10.1016/j.compedu.2009.03.002; Concrete scheme: one 'signal hue' far from the grid's red-pink, e.g. teal #1C9C9C or blue #2F6FDE at 20–30% alpha under the trace; same hue on the rule card's keyword and the caliper handles. Never use red/orange/pink for signals (they vanish into the grid). Hue-only signals must also differ in luminance (colour-blind safe).  
- Почему подходит: Tells the SVG strip renderer exactly which overlay types are worth building (static colour fill of the relevant segment, tied by hue to the rule text) and which to avoid (blinking, spotlights, floating arrows). Also validates the author's plan to render strips procedurally: overlays can be generated from the same millimetre geometry.  
- Риски: Signal studies mostly used text/diagrams, not high-density traces; too many simultaneous colour signals recreate clutter. Limit to one active signal per rule step.  
- Реализуемость в Blender: not a Blender task — implement in the SVG/HTML strip layer (a <rect>/<path> under the trace with fill-opacity). Trivial.

### Um, Plass, Hayward & Homer (2012) — Emotional design in multimedia learning, Journal of Educational Psychology 104(2) (with replications: Plass et al. 2014 Learning & Instruction 29:128–140; Münchow, Mengelkamp & Bannert 2017; meta-analysis Brom, Stárková & D'Mello 2018)
- Тип: research-paper  
- Ссылка: https://doi.org/10.1037/a0026609  
- Стиль: Warm, saturated accents + rounded forms, in the frame, not in the content  
- Визуальные черты: Um et al. 2012 operationalised 'positive emotional design' as warm colours ('bright and highly saturated colours of higher wavelengths' — yellows/oranges) plus round, baby-face-like anthropomorphic figures vs. achromatic + angular; it improved comprehension, transfer and achievement motivation (as described in Münchow 2017, open access: https://doi.org/10.1155/2017/2148139).; Plass et al. 2014 (https://doi.org/10.1016/j.learninstruc.2013.02.006): replicated comprehension but NOT transfer; in Exp. 2 warm colour alone did not raise positive affect while face-like round shapes did → faces/roundness carry more than hue.; Münchow 2017 (n = 111, neuroanatomy, 20 min): positive design (yellow/orange backgrounds, round frames) beat the achromatic/sharp-edged version on comprehension and transfer only when learners' initial positive affect was high.; Brom et al. 2018 meta-analysis (33 samples, N = 2,924; https://doi.org/10.1016/j.edurev.2018.09.004) as cited by later reviews: retention d = 0.39, comprehension 0.32, transfer 0.33, intrinsic motivation 0.26, perceived difficulty −0.21.; Venni & Désiron 2022 (https://archive-ouverte.unige.ch/unige:169401) warn that study materials are inconsistent (blue 'warm' cells, pointed 'round' shapes) → treat the effect as real but modest and implement it properly: warm = yellow→orange→coral family (e.g. #F5C04A, #F28C38, #F08A74), round = bevelled/filleted furniture, rounded UI corners (8–12 px), soft character silhouettes.; Boundary: keep the warm/round treatment on the FRAME (room, UI chrome, mentor avatar) and keep the strip itself achromatic ink-on-paper. The team's cream/mint/teal/coral pastel low-poly with bevels is already an emotional-design palette; the only correction is to desaturate coral/pink in rooms that frame a strip so the red-pink grid stays the only warm high-saturation element.  
- Почему подходит: Directly supports the author's instinct for a friendly pastel 3D world: positive emotional design lowers perceived difficulty and raises motivation (useful for a topic many learners fear) with small-to-moderate learning gains. It also defines where NOT to apply it (the strip).  
- Риски: Effects are small and heterogeneous; transfer gains often fail to replicate; the manipulation must not raise visual noise (Park 2015 found anthropomorphic décor can be a seductive detail).  
- Реализуемость в Blender: easy — bevel modifiers (segments 3–4, width 1–2 cm) for roundness, material base colours set from a warm pastel table, soft area-light key with warm temperature (≈4,000–4,500 K) and cool fill; all parameterisable in bpy.

### Plass, Homer, MacNamara, Ober, Rose, Pawar, Hovey & Olsen (2020) — Emotional design for digital games for learning: the effect of expression, color, shape, and dimensionality on the affective quality of game characters, Learning and Instruction 70:101194 (plus Mayer 2019, Computer Games in Education, Annual Review of Psychology 70)
- Тип: research-paper  
- Ссылка: https://doi.org/10.1016/j.learninstruc.2019.01.005  
- Стиль: Characters: expression first; colour medium; shape small; realism not a learning feature  
- Визуальные черты: Four studies (forced choice + PANAS-X; adults and adolescents): facial EXPRESSION and DIMENSIONALITY had the largest effects on the perceived affective quality of game characters; COLOUR (warm vs grayscale) medium; SHAPE (round vs square) small-to-medium.; Implication for patients/staff NPCs: a readable face (worried patient, calm cardiologist) does more emotional work than any body modelling → invest in 6–8 expression states, not in mesh detail. 3D (dimensionality) mattered most in immersive VR, so flat/low-poly bodies are fine for a 2D screen.; Mayer 2019 value-added review (https://doi.org/10.1146/annurev-psych-010418-102744): features with evidence are modality, personalization (conversational style), pretraining, coaching, self-explanation — none is 'richer graphics' or realism; games are 'less consistent' in Mayer's own meta-corpus. Spend budget on a mentor who coaches, on pre-training (grid, 1 mm = 40 ms, calibration pulse) before cases, and on 'explain why' prompts.; Concrete: NPC faces as simple SVG/2D decals or shape-key sets (eyebrows, mouth, eye openness); skin/clothes in the pastel palette; speech in second person, informal register ('Schau dir V1 an…').  
- Почему подходит: The game is NPC-driven (patients, nurses, chief). This is the only emotional-design evidence specifically about game characters, and it says where the art budget should go. Mayer's review says graphics richness is not among the proven value-added features, which protects the strip from an arms race of visual spectacle.  
- Риски: Affective-quality ratings, not learning outcomes, were measured; adolescents and adults differed. Facial expressiveness in procedural Blender characters is costly.  
- Реализуемость в Blender: medium/hard for faces in pure bpy (procedural rigging of expressive faces is laborious); easy workaround: flat-shaded heads with 2D face textures swapped per expression, or pre-made shape-key heads instanced by script. Body/pose generation is easy.

### Nielsen Norman Group — Kate Moran, The Aesthetic-Usability Effect (Kurosu & Kashimura 1995: 26 ATM layouts, 252 participants), with WCAG 2.2 SC 1.4.3/1.4.11 and Buchner & Baumgartner 2007 on display polarity
- Тип: research-paper  
- Ссылка: https://www.nngroup.com/articles/aesthetic-usability-effect/  
- Стиль: Polished frame buys tolerance; luminance contrast and dark-on-light carry the reading task  
- Визуальные черты: Aesthetic-usability effect: attractive products are perceived as more usable; it forgives MINOR usability problems only and masks problems in testing → a polished pastel world will make learners tolerate friction, but will not fix a hard-to-read strip. Test with behaviour (time to find PR, measurement error), not opinions.; WCAG 2.2 SC 1.4.3 (https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html): text ≥ 4.5:1, large text (≥18 pt or 14 pt bold ≈ 24 px / 18.5 px) ≥ 3:1; SC 1.4.11 non-text UI elements ≥ 3:1. Apply to lead labels, caliper readouts, rule cards; the strip's ink (#141414 on #FFFBF5) is far above this; the grid is intentionally BELOW it (it is background, not information).; Buchner & Baumgartner 2007, Ergonomics 50(7):1036–1063 (https://doi.org/10.1080/00140130701306413): proofreading (a fine-detail task) was better with dark text on light background than light-on-dark, regardless of ambient light or colour scheme; red-on-green without luminance contrast failed. → Paper mode (black on cream) should be the default analysis view; monitor mode (green #39FF88 or cyan #4FE3F0 on #071410) is an atmosphere/skin for ICU/ER scenes, with one-click switch to paper for measuring. Never rely on hue-only contrast (e.g. orange trace on pink grid).; Typography: one humanist sans (e.g. Inter/Source Sans) for UI, tabular figures for ms/mV readouts; lead labels 12–14 px in ink colour on the paper.  
- Почему подходит: The author wants 'catchy'; this literature says catchiness improves perceived usability and tolerance but the strip must stand on luminance contrast and dark-on-light polarity. It also settles the paper-vs-monitor aesthetic question with data rather than taste.  
- Риски: Buchner's task was text proofreading, not ECG reading; clinicians are habituated to green-on-black monitors, and some learners prefer dark mode — offer both, default to paper for measurement tasks.  
- Реализуемость в Blender: not Blender — HTML/SVG. Easy: two CSS themes for the strip (paper/monitor) sharing the same millimetre geometry.

### Amani-Beni et al. (2025) — A systematic review of eye-tracking technology in ECG interpretation research, Eur J Med Res 31:50 (19 studies, 573 participants) incl. Wood et al. 2014 (Med Decis Making 34:75–83) and Scherff et al. 2024 EYE-ECG RCT (GMS J Med Educ 41:Doc40)
- Тип: research-paper  
- Ссылка: https://pmc.ncbi.nlm.nih.gov/articles/PMC12797453/  
- Стиль: Design the strip for the expert scan path: stable lead map, rhythm strip, fast access to V1/V2/II  
- Визуальные черты: Experts orient to V1, V2, lead II and the rhythm strip within ~3–4 s and ignore the TP segment; novices scatter. Wood 2014: experts fixated critical leads at 3.43 s vs 6.62 s, diagnosed in 19.5 s vs 37.3 s, accuracy 6.05/8 vs 2.90/8. Bortolotti 2025: ~68 vs ~144 fixations, 108 s vs 205 s. Sqalli 2022: ~1,400 vs ~2,800 fixations per 10 ECGs.; Bond 2012: the rhythm strip received 26% of fixations, aVR 1%; Breen: rhythm strip most fixated (9.6 s), lead I least (0.1 s) → the 10 s lead-II rhythm strip must always be present, full width, bottom of the sheet, at the same pixel position in every case (standard 3×4 + 1 layout) so spatial memory builds.; Augustyniak: experts spend 50% longer on the QRS; students waste time on TP → signaling should pull attention to QRS/ST/T and the PR/QT brackets, never to baseline.; Sibbald et al.: a checklist verification step raised corrected errors per ECG from 0.04 to 0.27 → a persistent, collapsible systematic checklist (rate → rhythm → axis → PR → QRS → QT → ST/T) is a UI element, not a tutorial popup.; Scherff 2024 EYE-ECG (n = 91; https://books.publisso.de/en/journals/jme/volume41/zma001695): a 9-min video of an expert's gaze with think-aloud gave small, non-significant extra gains (d = 0.12–0.24); authors suggest PAUSING the gaze spot on the key feature while narration continues → a 'mentor's eye' mechanic: a soft circle that parks on V1 while the mentor explains, rather than a moving cursor.; Breen RCT: gaze feedback alone did not improve scores, but interpretation duration correlated r = −0.81 with performance → time-on-strip is a fair, cheap in-game metric; give feedback like 'you never looked at V2'.; Alahmadi 2019 (JAMIA 26:404–411, laypeople): format matters — a 10 s rhythm strip was inspected longer (3.85 s vs 1.82 s) and judged more reliably than a single aligned complex → never present interval tasks on a single complex.  
- Почему подходит: These are the only data on how the target users actually look at the central art asset. They dictate layout invariants (standard 12-lead map with rhythm strip), what to signal (QRS/ST/intervals, critical leads), what metrics to gamify (fixation economy, time), and a mentor mechanic borrowed from eye-movement modelling.  
- Риски: Small samples, mostly students; 3/19 studies high risk of bias; layouts were only compared in one study (Davies). No eye-tracking evidence on grid colour or paper vs monitor exists.  
- Реализуемость в Blender: not Blender — SVG layout rules (fixed lead map, rhythm strip) are easy; a gaze-spot overlay is a simple animated SVG circle.

### Oh, Cook, Van Gerven, Nicholson, Fairbrother, Smeenk & Pusic (2022) — Physician Training for ECG Interpretation: A Systematic Review and Meta-Analysis, Academic Medicine 97(4):593–602 (59 studies, 17,251 participants), with Eslava et al. 2009 (J Electrocardiol 42:693–697) and the Taif misreading study on novice errors
- Тип: research-paper  
- Ссылка: https://doi.org/10.1097/ACM.0000000000004607  
- Стиль: Make the systematic approach the UI skeleton; target the classic novice misses  
- Визуальные черты: Pooled SMD: SYSTEMATIC interpretation approach vs other approaches 0.92 (95% CI 0.48–1.37, 8 studies) — by far the largest effect; group vs individual study 0.35; peer-led vs faculty-led 0.38; computer-assisted vs face-to-face 0.23 (0.09–0.36); contrasting-features practice 0.23 (ns).; Design consequence: the case screen's fixed left/top rail IS the systematic sequence (rate → rhythm → axis → PR → QRS → QT → ST/T → conclusion), each step unlocking the matching strip overlay; progress is shown per step, not per case.; Eslava 2009 (n = 52 PGY-1, https://doi.org/10.1016/j.jelectrocard.2009.07.020): only half of ECGs read correctly; mean scores /2: acute MI 1.73, atrial flutter 1.50, VT 1.11, COMPLETE HEART BLOCK 0.23; certainty 18.5/40. Taif 2018 (n = 297 students/interns, https://www.ijcmph.com/index.php/ijcmph/article/view/3654): 2nd-degree AV block type II misread by 60.6%, type I by 50.2%.; → Content/visual priority list for signaling and repetition: AV blocks (P-QRS relationship — signal P waves with a colour dot and draw the dropped-beat gap), VT vs SVT with aberrancy, flutter waves, STEMI patterns. These need the strongest, most persistent overlays and the most deliberate-practice cases.; Peer/group effects suggest a 'second-opinion' NPC (a fellow student) and discussion-style feedback rather than solitary quizzes.  
- Почему подходит: Gives the author (a physician) the evidence-ranked instructional backbone and tells the art/UI team which strip features deserve the richest signaling. The novice-error data pick the exact waveform elements (P waves, PR constancy, QRS width) whose rendering fidelity and highlighting must be best.  
- Риски: Heterogeneous, mostly weak primary studies; 'systematic approach' trials differ in what the approach is. Novice error rates are from single-site quizzes.  
- Реализуемость в Blender: not a Blender item; the checklist rail and overlays are HTML/SVG — easy.

### Alahmadi, Davies, Vigo & Jay (2020) — Pseudo-colouring an ECG enables lay people to detect QT-interval prolongation regardless of heart rate, PLoS ONE 15(8):e0237854 (n = 43, 40 ECGs, MRMC ROC + eye-tracking)
- Тип: research-paper  
- Ссылка: https://doi.org/10.1371/journal.pone.0237854  
- Стиль: Scaffolded colour-filled intervals that fade with mastery  
- Визуальные черты: Four visualisations tested: Cartesian vs polar coordinates, each with/without pseudo-colouring of the interval of interest. Pseudo-colouring significantly improved detection accuracy across heart rates and T-wave morphologies, shortened reaction time, raised satisfaction; eye movements showed colour steered gaze to the diagnostically relevant region.; Polar coordinates are a research curiosity; keep Cartesian strips (clinical transfer). Take the colouring idea: a translucent fill under the QT (or PR, QRS) region computed from the same SVG geometry, in the signal hue (teal #1C9C9C ~25% alpha), optionally shaded by deviation from normal (e.g. green within limits → amber #F5C04A → red #D83A3A beyond QTc 500 ms).; Progression: level 1 shows the fill automatically; level 2 shows it after the player places calipers; level 3 removes it (fading scaffolds), so the learner ends up reading plain paper as in the ward.; Companion 2019 JAMIA study (https://pmc.ncbi.nlm.nih.gov/articles/PMC7787352/): laypeople's 50% JND for QT change ≈ 30 ms, 75% JND ≈ 88 ms on a 10 s rhythm strip — a useful calibration for how big a difference an exercise must present to a beginner.  
- Почему подходит: It is the one controlled visual-design experiment on an ECG strip and it shows a colour overlay, not a redesign of the trace, is what helps non-experts. It harmonises with the team's millimetre-exact SVG: fills are derived from measured fiducial points.  
- Риски: Lay participants, QT only; experts might find the fill patronising — hence the fade-out progression and a global toggle.  
- Реализуемость в Blender: not Blender — SVG rect/path fills under the trace, trivial.

### Kligfield et al. (2007) — AHA/ACCF/HRS Recommendations for the Standardization and Interpretation of the Electrocardiogram, Part I: The ECG and its Technology, Circulation 115:1306–1324; plus ECG-Image-Kit (Shivashankara et al., arXiv:2307.01946) on paper conventions
- Тип: research-paper  
- Ссылка: https://doi.org/10.1161/CIRCULATIONAHA.106.180200  
- Стиль: Clinically exact paper: 25 mm/s, 10 mm/mV, 1/5 mm grid, 3×4 + lead II strip, red-pink grid by convention (not standard)  
- Визуальные черты: Standard presentation (as the team already renders): 25 mm/s and 10 mm/mV; fine grid 1 mm = 40 ms / 0.1 mV; coarse grid 5 mm = 0.2 s / 0.5 mV; calibration pulse 1 mV, 0.2 s wide at the left; most paper ECGs use the 3×4 lead block (2.5 s per lead) + a 10 s rhythm strip of II (sometimes V1, V2 or V5) (ECG-Image-Kit full text: https://arxiv.org/html/2307.01946v4).; Grid colour: 'While most paper ECG grids are red-pink in color, there is no widely accepted standard for ECG paper color' (ECG-Image-Kit). Therefore the team is free to tune grid luminance for readability as long as hue stays in the red-pink family that learners will meet on the ward. Suggested tokens: paper #FFFBF5, 1 mm grid #F4C7C3, 5 mm grid #E9A3A0, ink #141414, calibration pulse ink; ink stroke ≈ 0.25–0.3 mm paper-equivalent (crisp, non-antialiased look avoided — use 1.5–2 px at 100% zoom).; Keep lead labels printed at the top-left of each 2.5 s segment as on real sheets (ECG-Image-Kit), so recognition transfers to real printouts; show the sheet's header (name/age/date) only in the narrative, not as decorative text (coherence).; Monitor variant for ICU/ER scenes: same geometry, green trace on near-black with a faint grid, but any MEASUREMENT task reopens the paper view (see polarity evidence).; Note: the display-requirement paragraphs of Kligfield were not fetched (paywalled); geometry facts above are confirmed via ECG-Image-Kit and general standards.  
- Почему подходит: Anchors the central art asset to clinical reality (the author's own standard) and explicitly frees the palette decision: hue is convention, luminance is design. It also fixes the layout that eye-tracking studies showed experts rely on.  
- Риски: Regional practice differs (50 mm/s in parts of Germany, 6×2 layouts, black-grid Philips/orange-grid Nihon Kohden paper); offer speed/layout toggles so the game does not train a single vendor's look.  
- Реализуемость в Blender: easy — the paper can be a texture generated from the same SVG (rasterised at 200–300 DPI) and placed as an emissive-free, matte plane in the Blender scene for establishing shots; the interactive strip itself stays SVG in HTML.

**Выводы агента:**

- Treat the ECG strip as the only high-spatial-frequency region on screen. Everything the Blender scene contributes (walls, furniture, light) should be large, smooth, low-contrast shapes; no textures whose spatial frequency resembles the 1 mm grid (fabric, tiles, noise, wood grain) within or near the strip's viewport. Coherence has the largest and most replicated effect size in the multimedia-learning literature.
- Separate the 'frame' from the 'content' in the colour system: warm, rounded, pastel emotional design (yellow/orange/coral, bevelled low-poly, soft key light) for rooms, UI chrome and NPCs; strictly achromatic ink-on-cream for the strip; one cool 'signal hue' (teal/blue) reserved for overlays that tie rule text to the trace. Never use red/pink/orange as a signal — it disappears into the grid.
- Signal with static, permanent colour fills under the trace; never blink, avoid floating arrows and spotlights (meta-analytic g for blinking is negative). Keep one active signal per rule step and fade scaffolds out as the player levels up (pseudo-colouring evidence).
- Design the layout for the expert scan path: fixed 3×4 + 10 s lead-II rhythm strip at identical screen positions in every case; make V1, V2, II and the rhythm strip the cheapest to reach; gamify time-on-strip and 'leads you never looked at' rather than exotic scoring.
- The systematic interpretation approach is the single strongest training intervention (SMD 0.92) — make the step sequence a persistent UI rail, with checklist verification before the player commits a diagnosis; prioritise AV blocks, VT, flutter and STEMI patterns, which novices miss most.
- Paper mode (dark trace on light cream) should be the default for any measuring task; monitor mode (green/cyan on near-black) is scene flavour for ICU/ER, one click away from paper. Contrast must be luminance-based: trace ≥ 15:1, UI text ≥ 4.5:1 (WCAG AA), UI non-text ≥ 3:1, grid deliberately low (≈1.5–2.2:1) so it recedes.
- Characters carry emotion mainly through facial expression (largest effect in game-character emotional-design research); body detail and 3D realism add little on a flat screen. For a procedural-Blender pipeline, invest in a small expression set (decals or shape keys) and conversational, second-person mentor dialogue, not mesh detail.
- Rich graphics are not a proven value-added game feature; pretraining (grid, calibration, 1 mm = 40 ms), coaching, personalization and self-explanation prompts are. Spend production effort there and let the pastel diorama remain a hub/transition world rather than a backdrop to every strip.
- Aesthetic polish raises perceived usability and tolerance for minor friction, but it also masks problems in testing: evaluate the strip UI by measured behaviour (time to find PR, caliper error, missed leads), not by learner ratings.
- Evidence gaps to acknowledge: no study has tested grid colour, paper vs monitor skin, or decorative environments specifically on ECG learning; effect sizes above come from short lab lessons. Keep décor and signal density as runtime parameters so the team can A/B them cheaply with its own learners.

## Визуальная идентичность вокруг самой ЭКГ

### Philips IntelliVue MX100/X3 Instructions for Use – factory default measurement colours (Default Settings appendix)
- Тип: studio  
- Ссылка: https://images.philips.com/is/content/PhilipsConsumer/Campaigns/CA08092022_nbp/Mx100_X3_ifu_eng.pdf  
- Стиль: ICU monitor: colour-coded waveforms + big numerics on black  
- Визуальные черты: Factory defaults (verified in appendix 25): ECG = Green; Resp = Yellow; SpO2/pleth = Cyan (light blue); NBP = Red; invasive arterial pressures (ABP/ART/Ao…) = Red; CVP/RAP/LAP = Cyan; PAP = Yellow; ICP/IAP/CPP = Magenta; CO2 = Yellow; Temp = Green; Cardiac output = Green; SpHb = Red, SpOC = Magenta, SpMet = Orange; ST-snippet text confirms the convention: 'drawn in the same color as the ECG wave, usually green'; Alarm semantics: red = high-priority patient alarm, yellow = lower priority, light blue = INOP (technical); alarm message background flashes in severity colour; numerics flash; Numerics are label- and colour-matched to their wave ('color-coded to match its source wave'); screen trends reuse the measurement colour; Electrode colour table printed in the ECG chapter: AAMI RA white / LA black / LL red / RL green / V brown; IEC R red / L yellow / F green / N black / C white (C1–C6 white with red/yellow/green/brown/black/violet rings); Default ECG size x1 (10 mm/mV); monitor display 1024x480 active-matrix colour  
- Почему подходит: This is the authoritative 'monitor mode' palette for the ICU/ER locations: one hue per physiological channel, saturated colour reserved for data and alarms, everything else neutral. Using these exact mappings makes the game's monitors read as real to residents and nurses.  
- Риски: Defaults are configurable per hospital and the APSF notes there is no universal standard (some sites use yellow for SpO2). Colours are given as names, not hex; pick hex yourself (e.g. green #00FF66-ish, cyan #00E5FF, yellow #FFE600, red #FF3B30, magenta #FF4DFF on #000).  
- Реализуемость в Blender: easy – emission shader on a screen plane with a procedurally generated texture (bpy can write the panel as an image via PIL/numpy or use an HTML/SVG overlay composited on the render); no GPU needed, emission with slight bloom in compositor

### ZOLL X Series Operator's Guide (Rev. G, 2013) – display modes and colour coding
- Тип: studio  
- Ссылка: https://documents.cdn.ifixit.com/ZOY5FA4FoCEfvPe4.pdf  
- Стиль: Defibrillator/transport monitor: configurable colour on black, white high-contrast mode  
- Визуальные черты: 'Color-coded waveforms and ECG lead identifiers'; 'each type of information in a specific user-configurable color'; Two brightness modes with explicit rationale: 'high contrast with white background (for optimal display in bright sunlight)' and 'color with black background (numerics and waveforms are easy to read)', plus an NVG-friendly mode; Spec: colour LCD 640x480 px; sweep speed 25 or 50 mm/s user-selectable; trace size 1 cm/mV default; up to 4 waveforms; split-screen 12-lead; Screen chrome: date/time, patient mode, battery, elapsed time, quick-access keys, waveform source label, HR/SpO2/RR/Temp numerics – all in a strict grid  
- Почему подходит: Gives a documented, device-native justification for offering BOTH a light (paper-like, white) and a dark (monitor) theme with identical geometry – exactly the light/dark question the team asked. The defib is also the natural 'emergency' prop for the ER chapter.  
- Риски: The ifixit link is a mirror of the 2013 guide (official manuals are at zoll.com but served via a landing page); exact RGB values are not published, only the principle.  
- Реализуемость в Blender: easy – a boxy orange/grey handheld with a screen plane; screen content generated procedurally; ZOLL trade dress should be abstracted (no logos)

### ECG electrode colour codes – IEC vs AHA/AAMI (My-EKG reference page; same table printed in the Philips IFU)
- Тип: research-paper  
- Ссылка: https://en.my-ekg.com/tips-ekg/ekg-electrode-color-coding.html  
- Стиль: Standardised 10-colour semantic palette for leads  
- Визуальные черты: IEC (Europe, incl. RU/DE): R red, L yellow, F green, N black; C1 red, C2 yellow, C3 green, C4 brown, C5 black, C6 violet (chest electrodes alternatively all white); AHA/AAMI (US): RA white, LA black, LL red, RL green; V1 red, V2 yellow, V3 green, V4 blue, V5 orange, V6 purple (chest alternatively all brown); Letter labels R/L/F/N vs RA/LA/LL/RL are part of the visual code and appear on cable clips and monitor lead selectors  
- Почему подходит: A ready-made, meaningful colour vocabulary for electrode-placement mini-games, lead-selector UI and even NPC accessories (cable colours on the ward). For a Russian/German audience the IEC set is the correct one.  
- Риски: Two incompatible standards; pick one (IEC) and state it in the UI to avoid teaching the wrong mapping. Red+green pairs are a colour-blindness hazard – always show the letter label too.  
- Реализуемость в Blender: easy – coloured cable/clip materials in bpy; letters as decals or UI overlay

### ECG-Image-Kit (Shivashankara, Shervedani, Clifford, Reyna, Sameni – Physiological Measurement 2024; open-source generator used for the PhysioNet 2024 Challenge)
- Тип: research-paper  
- Ссылка: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11135178/  
- Стиль: Photoreal 'printed 12-lead on paper' with exact grid palettes  
- Визуальные черты: Exact grid palettes in code (github.com/alphanumericslab/ecg-image-kit, ecg_plot.py): pink paper major #FFCBDD / minor #FEEDF8; red paper major #FF0000 / minor #FEDFDB; brown major #6D322F / minor #966B65; blue major #000066 / minor #0000B3; green major #004D00 / minor #00CC4D; B/W major #666666 / minor #BFBFBF, trace #000000; Grid metrics: big square 0.2 s x 0.5 mV = 5 mm, minor via AutoMinorLocator(5); grid_line_width 0.5, trace 0.75, calibration pulse 1.5x trace width, lead separator ticks 3x; hard-coded labels '25mm/s' and '10mm/mV'; 0.2 s calibration pulse at row start; Trace colour sampled as near-black grey (0–0.2) for realism; optional realism layers: wrinkles/creases, shadows, handwritten text, perspective transform, printed text artifacts  
- Почему подходит: The most rigorous published spec for making a strip look like real paper while staying metrically exact – precisely what the team's SVG renderer needs for 'paper mode' and for in-world props (a crumpled strip handed over by a nurse).  
- Риски: Palette values are for ML augmentation, not aesthetics (the pure-red #FF0000 major grid is harsher than real paper); use the pink set or soften the red. Code is Python/matplotlib, not SVG – port the numbers, not the code.  
- Реализуемость в Blender: easy – procedural paper material (Brick/Wave texture nodes for 1 mm/5 mm lines, Noise for fibre, slight displacement for creases) renders fine on CPU Cycles; or bake the SVG to a texture

### Open-source ECG paper renderers: dy1901/ecg_plot, pmecg, VintaSoft EcgRenderingSettings (default colours compared)
- Тип: app  
- Ссылка: https://github.com/dy1901/ecg_plot  
- Стиль: Classic red/pink grid with black or blue trace (screen rendering defaults)  
- Визуальные черты: ecg_plot defaults: major grid #FF0000, minor #FFB3B3, trace #0000B3 (blue), all lines 0.5 pt; bw style #666666/#BFBFBF/#000000; major ticks 0.2 s, minor 5 per major; lead labels 9 pt placed 0.07 s right / 0.5 mV below row origin; 12-lead layout 3x4 + rhythm at 50 mm/s uses 2 in per second; pmecg defaults: single grid colour #F4AAAA, speed 25 mm/s, voltage 10 mm/mV, row distance 3 mV, trace 0.5 pt, calibration pulse on, time-axis labels 7 pt monospace; VintaSoft (commercial DICOM SDK) defaults: minor grid (255,229,229) = #FFE5E5, major (255,187,187) = #FFBBBB  
- Почему подходит: Three independent, widely used implementations converge on the same recipe – light pink minor lines, stronger pink/red major lines, dark trace – which gives the team defensible hex tokens (minor ~#FFE5E5–#FEDFDB, major ~#FFB3B3–#FFBBBB, trace #000/#0000B3) for a readable, non-garish paper mode.  
- Риски: Pure #FF0000 major lines (ecg_plot) vibrate against black traces on screens; pmecg's single-colour grid loses the 5 mm emphasis unless line weight differs. None of these handle HiDPI sub-pixel line crispness – snap lines to device pixels in SVG (shape-rendering: crispEdges).  
- Реализуемость в Blender: easy – numbers port directly into a node-based grid or an SVG overlay

### US Patent 5,673,702 (Cambridge Heart, 1997) 'Improved electronic display of physiologic waveforms' + ECG chart-paper colour variants (Nihon Kohden/Burdick orange, red, green grid)
- Тип: research-paper  
- Ссылка: https://patents.google.com/patent/US5673702A/en  
- Стиль: How to simulate ECG paper on a screen (and what real paper looks like)  
- Визуальные черты: Paper description in the patent: 1 mm lines with every fifth emphasised; 'background is generally white or pale grey, and the lines are typically red or grey'; Proposed screen rendering: minor lines thinner than major lines (also allowed: different intensity or colour); preferred 'major and minor lines be red or gray' with the signal 'of a black or blue color'; grid drawn by line commands or by tiling a stored bitmap; dithering for sub-pixel smoothing; erase only trace pixels then restore grid so it looks like 'a pen drawing on paper'; electronic calipers; prior art criticised for black background and 1 cm coarse grid; Rationale: a 0.1 mV ST shift (1 mm) is invisible without a fine grid – i.e. the grid is diagnostic, not decoration; Real paper variants on the market: red grid (GE, Philips, Welch Allyn, Edan, Precision Charts), orange grid (Nihon Kohden, Burdick – https://wellbefore.com/products/nihon-kohden-z-fold-recording-chart-paper-with-orange-grid), green grid (Livingstone 50 mm rolls); supplier note: red/orange contrast most with the trace, black photocopies best, green/blue exist to match legacy records  
- Почему подходит: Explains why the strip must keep thin minor lines and a light background in any 'beautiful' treatment, and legitimises an orange- or green-grid variant if the team wants a house colour that still reads as ECG paper (e.g. coral-orange grid harmonises with the existing coral/teal 3D palette).  
- Риски: Patent language gives no hex; 'pale grey background' on screen can look dirty – prefer warm off-white (#FFFDF8-ish) with pink/orange lines. Orange-grid paper is less familiar to many learners than red/pink.  
- Реализуемость в Blender: easy – same procedural grid; orange variant is a one-token change

### ecglibrary.com – 12-lead ECG Library (classic web ECG atlas, FAQ describes the production technique)
- Тип: app  
- Ссылка: https://ecglibrary.com/ecgfaq.html  
- Стиль: Scanned black-on-pink strips with grid drawn as CSS page background  
- Визуальные черты: Originals are 'black on pink' printouts scanned at 300 dpi in 2 colours; for dark originals keep only the red channel: 'The pink grid is very red and hence is turned white by this technique' while the trace stays black; Scans reduced to 76.5 dpi so each small square is '3 pixels across', saved as transparent GIF and laid over a tiled grid background image – trace and grid are separate layers; Printing guidance: enlarge 400 % to regain 1 mm = 1 mm  
- Почему подходит: Oldest proof of the 'separate trace layer over a vector/tiled grid' pattern the team already uses in SVG; also quantifies the minimum legibility (3 px per mm then; on HiDPI aim for 4–6 px per mm so small squares stay countable).  
- Риски: 1990s aesthetics (GIFs, 3 px/mm) are too coarse for modern screens; the red-channel trick is irrelevant to procedural strips but useful if the physician wants to import scanned teaching ECGs.  
- Реализуемость в Blender: easy / not needed – purely 2D

### Eleanor Lutz (Tabletop Whale) – 'Electrocardiography Basics' / 'Heartbeats and heart attacks' poster for Nerdcore Medical (Curative Design series, 2016)
- Тип: art-reference  
- Ссылка: http://tabletopwhale.com/2016/10/19/heartbeats-and-heart-attacks.html  
- Стиль: Rhythm-strip silhouettes as colour bands on a blue-to-pink 'sunrise' gradient  
- Визуальные черты: Each EKG wave (normal + asystole, 1st-degree AVB, Mobitz I/II, 3rd-degree AVB, torsades, VT, VF, flutter, AF) is drawn in Illustrator and used as the upper boundary of a coloured horizontal band – 12 bands in the final (planned 15); Colour: blue-to-pink gradient as the focal point; white text throughout; black overlay/shading under the text and below each band edge for contrast; textured shadows and colour overlays in Photoshop; Typography: display serif Abril Fatface (TypeTogether) for titles; 18 x 24 in print; sold at https://store.nerdcoremedical.com/products/poster-1  
- Почему подходит: Shows how rhythm morphologies can become the game's branding/chapter art (arrhythmia 'levels' as colour bands) without touching the diagnostic strips – catchy and educational, and it maps 1:1 onto the rhythm chapter list.  
- Риски: Decorative, non-metric traces must never appear where the player is measuring; keep this style to menus, level cards and loading screens. Saturated gradient could compete with pastel 3D rooms – use it sparingly.  
- Реализуемость в Blender: easy – pure SVG/CSS; in Blender could be a wall poster texture in the cardiology office

### Matt Beevers – 'ECG Waveform Panel' (Dribbble, part of a Medical Device UI concept)
- Тип: art-reference  
- Ссылка: https://dribbble.com/shots/5312787-ECG-Waveform-Panel  
- Стиль: Glowing green-on-near-black monitor panel  
- Визуальные черты: Palette (Dribbble extraction): trace #19D823, background #03050A, darker greens #13A61C / #0C6613 for grid and label accents, greys #4E525E / #797C88 / #DCDDDF for chrome and text; Thin grey 5 mm-style grid on navy-black, single lead with soft glow; sweeping trace (animated GIF) with the newest segment brightest; Big numeric '108' in trace green inside thin corner brackets; label chips ('ECG Waveform', 'Heart Rate') with diagonal stripe accent; unit 'bpm' small-caps grey  
- Почему подходит: A clean template for the in-game bedside monitor widget: one accent hue, high contrast, large numeric, grid present but subdued – readable from a 3D room shot and consistent with the Philips green-ECG convention.  
- Риски: The glow/bloom reduces fine-detail readability – acceptable for ambience monitors, not for the diagnostic strip. Concept work, not a shipped device.  
- Реализуемость в Blender: easy – emission material + compositor Glare (Fog Glow) node, CPU-friendly

### Daria Gugnisheva – 'ECG WEB view and PDF print' (Dribbble, telemedicine ECG viewer concept)
- Тип: art-reference  
- Ссылка: https://dribbble.com/shots/26283172-ECG-WEB-view-and-PDF-print  
- Стиль: Light clinical viewer: grey mm-grid on white, blue trace, explicit gain/speed controls  
- Визуальные черты: Palette: #FBFBFB background, trace blue #1E40EB with lighter #6B8BEE / #A2BDF4 accents, text #000000 / #4D4D4D / #A4A4A4, dark navy #142751 for header icons; Toolbar is the ECG grammar itself: Duration (sec) 10; Gain (mm/mV) 5 | 10 | 20 | 40; Speed (mm/sec) 12.5 | 25 | 50 | 100 as segmented pills; HR 120 bpm; Abnormality 'Tachycardia'; filter checklist (low-pass 0.5–1 Hz, tremor suppression 35 Hz, notch 50/60 Hz); zoom +/-; overview mini-strip with highlighted viewport; Print/PDF variant on white A4 with the same grey grid and blue trace, patient header block with HR, gain, speed  
- Почему подходит: Demonstrates 'paper vs screen' as one design system with shared tokens, and turns the measurement parameters (gain, speed, filters) into visible UI – these can become the player's tools/upgrades. Grey grid + blue trace is a calm alternative to pink/red for long study sessions.  
- Риски: Grey grid loses the 5 mm/1 mm hierarchy at small sizes; 10-second strip squeezed into a widescreen pane distorts the 25 mm/s feel unless pixel-per-mm is enforced.  
- Реализуемость в Blender: easy – HTML/SVG only

### Sergei Polyuk – 'ECG monitor app' (Dribbble 2018, 'sono health' handheld + phone concept)
- Тип: art-reference  
- Ссылка: https://dribbble.com/shots/5819543-ECG-monitor-app  
- Стиль: Teal/navy pastel: navy trace on light grey mm-grid, teal device  
- Визуальные черты: Palette (Dribbble extraction): navy #031D35, light grey #E9EAEA, mid grey #A4A6A8, teal #63ACC0, slate #435D67 / #5C7283, pale cyan #9CD3E2; Phone screen: fine light-grey 1 mm grid with darker 5 mm lines on white, single-lead navy trace, verdict line 'No Abnormalities' + red heart + '70 bpm' large; 30 sec marker; print/email actions; Backdrop: large cyan trace on navy-teal monitor grid (ambient); device screen shows a red trace on white grid – three strip treatments in one composition; Rounded, matte pastel-teal device with big circular button – toy-like product language  
- Почему подходит: Closest existing match to the team's cream/mint/teal/coral 3D palette: proves a pastel world can host a strictly neutral grey-grid strip with a dark trace and still feel friendly. The 'verdict + one number' pattern suits level feedback.  
- Риски: Grey-grid-on-white deviates from the pink-paper convention learners see in textbooks; consider pastel teal only for chrome and keep pink/red grid for the strip. Concept, not a real product.  
- Реализуемость в Blender: easy – matches current bevelled low-poly pastel style; device prop is a rounded cube with emissive screen

### Samuel Garijo – 'ECG Demo for Embedded World 2025' (Dribbble, LVGL embedded GUI for a patient-monitor demo)
- Тип: art-reference  
- Ссылка: https://dribbble.com/shots/26067760-ECG-Demo-for-Embedded-World-2025  
- Стиль: Flat black multi-screen monitor: 12-lead 3x4, mixed-parameter view, big-numerics view  
- Визуальные черты: Palette: #040404 background, #E7E7E7 traces/text, greys #616161 / #A7A7A7, green #419245 / #3E4A1C for primary action and HR accent; Three layouts shown: (1) 12-lead 3x4 white traces + HR 60 / NIBP 120/70 + timer ring; (2) HR green, pleth cyan, ART red, RR yellow rows with matching numerics (same channel-colour convention as Philips); (3) 'big numerics' tiles HR 122 / Pleth 95 / ART 120/70 / RR 15 with limits; Bottom bar of flat icon buttons (Electrode position, Start recording, Change view, End case); thin grey separators, no grid on traces  
- Почему подходит: Reference for a 'monitor mode' that scales from a small widget to a full-screen 12-lead without noise; shows how a game screen can switch between strip-focused and numeric-focused states (useful for emergencies chapter).  
- Риски: No mm grid at all – acceptable for monitoring ambience but not for interval measurement; white traces on black can strobe when animated.  
- Реализуемость в Blender: easy – flat emissive panels; or pure HTML overlay

### Rimma Samortseva – 'Program for monitoring long-term ECG Sinus!' (Dribbble, Russian-language Holter app concept)
- Тип: art-reference  
- Ссылка: https://dribbble.com/shots/18313022-Program-for-monitoring-long-term-ECG-Sinus  
- Стиль: Blue-violet gradient brand + beat-morphology tiles with N/S/V/A classification  
- Визуальные черты: Blue-to-violet gradient background with giant outlined wordmark 'Sinus! Be h…' and a large black single-lead trace running across the bottom as a brand device; smiley red heart mascot; In-app: patient card (ФИО, дата рождения, № отчета), four beat-template thumbnails (selected one with red highlighted beat), three stacked mini-strips with red-marked abnormal beats, speed slider '50 мм/с', navigation arrows and N | S | V | A classification buttons (normal/supraventricular/ventricular/artifact); Strips: black trace on light grey grid; red used only for the beat being classified  
- Почему подходит: Shows a beat-classification loop as tappable buttons – a direct mechanic for arrhythmia levels – and uses red strictly as 'attention on this beat', which is the discipline the game needs. Russian UI language matches the team.  
- Риски: The decorative background ECG is non-metric; the violet gradient clashes with pink grid paper – keep brand gradient off the strip area.  
- Реализуемость в Blender: easy – UI only

### Apple Watch ECG app (Apple support article + ECG IFU) and AliveCor KardiaMobile – consumer single-lead 'strip + number + verdict' pattern
- Тип: app  
- Ссылка: https://support.apple.com/en-us/120278  
- Стиль: Minimal consumer ECG: animated Lead I trace, calm classification colours, PDF export  
- Визуальные черты: Lead I, 30 s recording; Health export data is 512 Hz in microvolts (Hugging Face export sample) – PDF report via 'Export a PDF for Your Doctor' then Share/print; Result taxonomy drives the UI: Sinus rhythm, Atrial fibrillation, Low or high heart rate (<50 / >120–150 bpm), Inconclusive, Poor Recording (v2); Secondary source (Digital Synopsis review): 'calm colour coding' – green for sinus rhythm, yellow for inconclusive; KardiaMobile described as 'one waveform, one number (BPM), one verdict'; KardiaMobile samples at 300 Hz (reseller spec)  
- Почему подходит: The three-element composition (strip / big number / verdict chip) is the simplest way to make a strip the hero of a game screen and to deliver feedback after a decision; the muted green/yellow/red verdict scale maps to correct/partial/wrong without shouting.  
- Риски: Trace colours of the Apple PDF and Kardia report could not be verified (AliveCor labeling server returned 503); do not cite specific hex for them. Consumer apps hide gain/speed – the game must show them.  
- Реализуемость в Blender: easy – UI only; wearable props optional

### Philips Visual Patient Avatar (Tscholl & Nöthiger, Visualization Technology Research Group, University Hospital Zurich; Bioengineering 2024 evaluation)
- Тип: app  
- Ссылка: https://www.philips.de/a-w/about/news/archive/standard/news/2023/202311-visual-patient-avatar.html  
- Стиль: At-a-glance patient avatar: colour, shape and animation encode vitals  
- Визуальные черты: Simplified human silhouette next to the numerics; vital signs translated into colour changes, shape changes and animations (synthetic-vision idea borrowed from aircraft cockpits); Runs as an option on IntelliVue MX400–MX850 in 185 countries; first commercial use at University Hospital Bonn; Claimed in USZ studies: about twice as many vital signs recalled after a 3- or 10-second glance vs conventional displays; 2024 survey (n=63) criticised threshold adjustability  
- Почему подходит: A research-backed way to show patient state in a game without competing with the strip: the NPC/patient card can change colour, breathing animation and posture while the ECG stays the only detailed graphic. Fits the stylised 3D characters already in the prototype.  
- Риски: Proprietary visual language – imitate the principle, not the design; evidence is mostly Philips/USZ-sourced simulation studies.  
- Реализуемость в Blender: medium – needs a simple rigged low-poly character with material/shape-key states; procedural in bpy is doable but more work than static props

**Выводы агента:**

- Two legitimate ECG 'looks' exist and both are documented by device makers: PAPER (dark trace on white/cream with red/pink 1 mm/5 mm grid, 25 mm/s, 10 mm/mV, calibration pulse) and MONITOR (ECG green, SpO2 cyan, Resp/CO2 yellow, arterial pressure red, ICP magenta on black – Philips factory defaults; ZOLL additionally offers a white 'high contrast' mode for sunlight). Map them to locations: cardiology office/reception = paper strips and printouts; ICU/ER = monitors and defib screens. Keep strip geometry identical and only swap colour tokens.
- Hex tokens that real renderers use for paper mode: minor grid #FEEDF8–#FFE5E5–#FEDFDB, major grid #FFCBDD–#FFBBBB–#FFB3B3 (pure #FF0000 only in ML tools), trace #000000 or #0000B3 (blue), paper #FFFFFF/#FBFBFB or warm off-white; neutral alternative #BFBFBF/#666666 grid. Monitor mode: trace green ~#19D823/#00FF66 on #03050A/#000, grid as dark green (#0C6613) or grey at ~15 % alpha. The 1994 Cambridge Heart patent states the rule that survives every style: minor lines thinner (or fainter) than major lines, light background, because a 1 mm (0.1 mV) shift must stay visible.
- Make the strip the hero by subtraction: the only saturated colours on a game screen should carry meaning (lead colours, alarm red/yellow, INOP light blue, 'this beat' red highlight as in the Sinus! concept). Room, furniture and UI chrome stay in desaturated cream/mint/grey; when the strip appears, dim and defocus the 3D scene (lower exposure + depth of field, both cheap in Cycles CPU) and present the strip either as a paper prop with soft shadow/wrinkle cues (ECG-Image-Kit realism layers) or as a glowing monitor panel (emission + Fog Glow).
- Readability rules from the sources: keep >= 4–6 CSS px per mm on HiDPI (ecglibrary's 3 px/mm was the 1990s minimum), snap grid lines to device pixels, show gain and speed as visible controls (5/10/20/40 mm/mV, 12.5/25/50/100 mm/s) and filters (0.5 Hz, 35–40 Hz, notch 50/60 Hz) – these parameters double as in-game tools; add electronic calipers (patent) as the measurement mechanic. Landscape panels show longer strips, portrait shows more parameters (Mindray BeneVision N22 iF-award rationale) – choose landscape for strip-centred screens.
- Typography pairing that matches the evidence: plain grotesk for labels and big numerics (monitors use large, colour-matched sans numerals), monospace with tabular figures for measurements and time-axis ticks (pmecg uses monospace ticks; reports list 'HR 120 bpm, Gain 10 mm/mV, Speed 25 mm/s' in a fixed header block). Recommended open fonts (team choice, not device-verified): Inter or IBM Plex Sans + IBM Plex Mono / JetBrains Mono; a display serif like Abril Fatface (Lutz poster) only for chapter/title cards.
- Use the lead-colour standard as a semantic palette for puzzles and props: IEC (red R, yellow L, green F, black N; C1–C6 red/yellow/green/brown/black/violet) for a Russian/German audience; always pair colour with the letter label (red/green confusion).
- Rhythm morphology as brand, exactness as content: Lutz's poster (traces as colour-band boundaries) and the Sinus! concept (giant background trace) show ECG silhouettes work for level cards, menus and loading screens, but decorative/non-metric traces (including dot-matrix or logo-style heartbeats like Nixtio's dashboard, https://dribbble.com/shots/27689695-Heart-Health-Monitoring-ECG-Dashboard) must never sit next to a strip the player is measuring.
- Feedback pattern from consumer ECG apps: strip + one big number + one verdict chip with calm green/yellow/red scale (Apple, Kardia). Pair it with a Visual-Patient-style avatar whose colour/animation reflects the patient's state so NPC status is readable at a glance without adding graphics that compete with the trace.
- Pastel 3D worlds (Polyuk's teal/navy concept) coexist well with strips when the strip panel is strictly neutral (white/grey/pink grid, dark trace) and the pastel hues are confined to chrome and props; an orange/coral grid variant (Nihon Kohden/Burdick orange paper exists) is the one way to tie the grid colour into the existing coral/teal palette while still reading as ECG paper.
- Most of this angle is 2D: generate strips and panels in SVG/HTML and composite them over Blender stills rather than baking them into renders; in bpy, paper and monitor materials are easy (Brick/Wave texture grids, emission shaders, compositor glare), the only 'medium' item is a rigged patient avatar.

## Стилизованные 3D-стили, воспроизводимые в Blender на CPU

### Grow Home (Ubisoft Reflections, 2015)
- Тип: game  
- Ссылка: https://store.steampowered.com/app/323320/  
- Стиль: flat-shaded low-poly, origami/paper-cutout geometry, saturated primaries  
- Визуальные черты: Low-poly planet, flora and islands built in Unity; shapes are simple geometric primitives (BUD = squares, plants = triangles), per the developer interview quoted in PC Gamer / Wikipedia; Flat faceted shading with no textures; colour comes from per-face material slots; Bright, saturated palette: grass greens ~#5FBF4F, sky ~#8ED1F0, BUD red ~#E3473B, rock greys ~#9FA5AB (approximate samples from screenshots, not developer-published); Lighting matters more than geometry: Reflections cited Pixar's Wall-E lighting to make flat geometry feel solid (soft sun + strong ambient); Procedural animation; no outlines  
- Почему подходит: Demonstrates that flat-shaded low-poly reads as 'designed', not 'cheap', when lighting is good; procedurally generated furniture (bpy primitives + Bevel) is the natural match for this look.  
- Риски: Saturated primaries compete with the ECG's red-pink grid; the hospital version must desaturate and reserve the red hue family for the strip. Faceted triangles can look like a 2014 'low-poly trend' cliché.  
- Реализуемость в Blender: EASY. mesh.shade_flat(); Principled BSDF roughness 1.0 or Emission for fully flat fills; one Sun (angle 10-20 deg) + world colour; Render > Light Paths > Fast GI Approximation (AO-based, manual: https://docs.blender.org/manual/en/latest/render/cycles/render_settings/light_paths.html) instead of full bounce GI; Film > Pixel Filter Box 1.0 for crisp facet edges. ~32-128 samples + OpenImageDenoise (CPU). Estimated 10-40 s per 1080p frame on 8-16 cores (my estimate, not a published benchmark).

### Alba: A Wildlife Adventure (ustwo games, 2020)
- Тип: game  
- Ссылка: https://ustwogames.co.uk/news/the-environment-art-of-alba-a-wildlife-adventure/  
- Стиль: low-poly solid-colour geometry with gradient-atlas shading, warm saturated Mediterranean palette  
- Визуальные черты: Environment art began as 'simple geometric shapes and solid colours'; characters kept that look through release (ustwo dev post); Shading via gradient colour atlases: UVs stretched over a gradient to control detail in shadowed areas; no normal maps; normals transferred from smooth proxy meshes to fake soft forms; Palette taken from location photos and painter Joaquin Sorolla: warm whites ~#F7EBD8, sea ~#3E9FD1, terracotta ~#D9784E, olive ~#8FA35A (approximate); Baked lighting; decals (concrete, breezeblock) packed with gradients; chipped edges via boolean cuts; Clean silhouettes, no outlines  
- Почему подходит: Shows a precise, documented recipe for 'low-poly but soft': smooth normal transfer + gradient ramps. In Blender this is Data Transfer modifier (custom normals) + ColorRamp driven by Layer Weight or object-space Z, all scriptable.  
- Риски: Saturated warm palette is lovely for a seaside, less so for a clinic; needs a cooler, lower-chroma re-tune so the strip stays the only warm-red element.  
- Реализуемость в Blender: EASY-MEDIUM. Data Transfer modifier (Custom Normals from a smoothed duplicate) to soften bevelled furniture; material = ColorRamp (two pastel stops) fed by Separate XYZ of Object coordinates or Layer Weight; Bevel modifier (width 0.01-0.02, 3 segments) for highlight edges. Cycles cost same as flat low-poly (fast, little noise).

### Button City (Subliminal, 2021)
- Тип: game  
- Ссылка: https://store.steampowered.com/app/1273750/Button_City  
- Стиль: pastel low-poly diorama, N64-like chunky models, soft shading  
- Визуальные черты: Described by press as 'a low poly pastel game' with each main area presented 'similar to a diorama'; Pastel palette: mint ~#BFE6D5, lavender ~#CFC3F0, peach ~#F6C9B0, butter ~#F8E7A8 (approximate from screenshots); Rounded, chunky characters; soft, low-contrast shadows; no outlines; Small self-contained areas viewed from a slightly elevated camera  
- Почему подходит: Closest commercial analogue to the author's current prototype palette (cream/mint/teal/coral). Proves pastel low-poly dioramas can carry a narrative game for adults without visual noise.  
- Риски: Pastel-on-pastel can become mushy; the ECG strip panel must have hard black trace and a crisp border to anchor contrast. Reviews called the overall game thin, so the look alone is not a draw.  
- Реализуемость в Blender: EASY. Same pipeline as the current prototype: Bevel + flat pastel Principled materials, large Area light fill, Sun key; AgX 'Base' view transform to avoid pastel highlights clipping; optional Glare Bloom (Threshold 1.0, Strength 0.1) in compositor. 128-256 samples + OIDN.

### Timothy J. Reynolds - 'Low-Poly, Isometric Worlds'
- Тип: art-reference  
- Ссылка: https://turnislefthome.com/  
- Стиль: isometric flat-shaded low-poly illustration (Cinema 4D), high-key lighting, muted palette  
- Визуальные черты: Series of isometric dioramas (factory, race car, city) on white/cream backgrounds, covered by Gigazine in 2012 (https://www.gigazine.net/gsc_news/en/20121230-low-poly-world); Flat facets with visible triangulation; ambient-occlusion-heavy soft shadows; no outlines; Muted, slightly desaturated palette with one accent colour per piece; typical values ~#E9E4D8 ground, #8BA8B7 water, #D96F4B accent (approximate); Orthographic 30 deg/45 deg isometric framing; objects float on a plinth  
- Почему подходит: The canonical reference for the 'low-poly isometric illustration' wave that Blender tutorials (Polygon Runway, Chahin) later popularised; a hospital 'floor plate' per location in this manner is a clean, non-distracting backdrop for a 2D strip overlay.  
- Риски: Static, illustrative; locations may feel like infographics rather than places. Dated if facets are too visible.  
- Реализуемость в Blender: EASY. Camera type ORTHO, rotation (54.736 deg, 0, 45 deg) for true isometric or (60, 0, 45) for a friendlier dimetric; ortho_scale sized to the room; Film Transparent so the HTML page supplies the background; AO via Fast GI; 64-128 samples.

### Monument Valley (ustwo games, 2014)
- Тип: game  
- Ссылка: https://www.monumentvalleygame.com/  
- Стиль: isometric Escher-inspired architecture, flat colour planes, minimal shading, gradient skies  
- Визуальные черты: Inspired by Escher ('Ascending and Descending'), Japanese prints and minimalist 3D design, per ustwo (Creative Bloq making-of); Isometric/orthographic camera; architecture in flat colour planes with minimal AO; colour used as navigation cue; Per-level monochrome-plus-accent palettes: e.g. dusty rose ~#D7A6A1 / ochre ~#D9B36A / teal ~#2E7F86 with cream highlights (approximate); Soft vertical gradients on skies; no outlines; very few textures; Architectural references from Spain, Morocco, India, Iran, Uzbekistan  
- Почему подходит: Shows how an orthographic diorama with restrained colour lets a single foreground element dominate; reserving one saturated accent per scene maps neatly onto 'the ECG strip is the accent'.  
- Риски: Its impossible-geometry identity is irrelevant to a hospital; copying the look invites comparison. Flat planes with no bevel can look like UI, not a room.  
- Реализуемость в Blender: EASY. Ortho camera; Emission or near-flat Diffuse materials; one Sun with sharp shadows (angle 0.5 deg) plus world AO; compositor Color Balance for per-scene tint. Fastest of all looks on CPU (emission-heavy scenes converge in <32 samples).

### The Almost Gone (Happy Volcano, 2020)
- Тип: game  
- Ссылка: https://store.steampowered.com/app/1115780/  
- Стиль: rotatable isometric dollhouse dioramas, muted pastel, soft shadows  
- Визуальные черты: Each scene is a miniature diorama the player rotates in 90-degree steps to reveal hidden objects ('digital dollhouse aesthetic', Guardian/Vice); Rooms cut open like a dollhouse: two walls removed, furniture as bevelled blocks; Muted pastel palette with low saturation: dusty pink ~#E8C9C4, sage ~#B8C9B5, cream ~#F4EEE2, slate ~#6E7A86 (approximate); Soft directional light, long soft shadows, subtle AO; no outlines; Narrative about death/loss/mental health, aimed at adults: proves the diorama look is not inherently childish  
- Почему подходит: A room-per-location structure (reception, ward, ICU, ER, office) is exactly this game's unit of design; cut-away rooms also give an obvious 'desk' surface on which to present the ECG strip as a found object before it is enlarged into the UI.  
- Риски: Rotation mechanics are not needed; keep a fixed camera. Low saturation can read as gloomy for a teaching game; the author's cream/teal/coral is warmer.  
- Реализуемость в Blender: EASY. Boolean 'room in a box' (cube minus inner cube, delete two walls), Bevel modifier on everything, ortho or long-lens (85-100 mm) camera at ~35-45 deg elevation; Sun angle 3-5 deg for soft shadows. Scenes converge in 128-256 samples + OIDN; ~30-90 s per frame on 8-16 cores (estimate).

### Mohamed Chahin - isometric 'room in a cube' Blender renders
- Тип: art-reference  
- Ссылка: https://dribbble.com/MohChahin  
- Стиль: isometric pastel low-poly room-in-a-box (Blender), the 2017+ 'isometric room' trend  
- Визуальные черты: Rooms cut into a cube with two walls, viewed at 45 deg with almost no perspective (BlenderNation challenge write-up: https://www.blendernation.com/2017/09/14/low-poly-challenge-isometric-room/); Bevelled low-poly furniture, soft pastel materials, one strong sun through the missing wall, visible soft AO in corners; Candy pastel palette: pink ~#F6C1C7, mint ~#BFE3D2, lilac ~#D5C8F2, warm wood ~#D9A878 (approximate); Floating on a transparent/white background; often slightly tilted camera for playfulness  
- Почему подходит: This is literally the style the author's prototype already approximates, and it is the single most reproduced Blender look (thousands of tutorials), so procedural bpy generation has abundant reference.  
- Риски: Over-familiar on social media; can feel like stock illustration. Candy saturation must be dialled down near the strip.  
- Реализуемость в Blender: EASY (textbook Blender). Cube room + Bevel + pastel Principled; Sun + large Area fill; Cycles 128-256 samples; OIDN. Add Film Transparent to overlay onto HTML.

### Polygon Runway (Roman Klco) - Blender isometric/low-poly illustration courses
- Тип: studio  
- Ссылка: https://polygonrunway.com/  
- Стиль: stylised isometric low-poly Blender illustration, pastel with saturated accents  
- Визуальные черты: Hundreds of free YouTube breakdowns and paid courses on isometric rooms (e.g. home studio room, dungeon, desert building), covered by 80.lv (https://80.lv/articles/tutorial-on-isometric-scenes-in-blender); Signature: bevelled blocks, simple Principled materials, Sun key + HDRI fill, ortho camera, slight DoF; Teaches the exact workflow that is trivially expressible in bpy: primitives, modifiers, material slots  
- Почему подходит: A ready-made pedagogy of the look the author is already using; useful as a reference library for furniture proportions and lighting ratios.  
- Риски: Course material is a 'style' many people copy; differentiate with hospital-specific props and the ECG colour discipline.  
- Реализуемость в Blender: EASY. All techniques are modifiers + node materials; nothing GPU-specific.

### Two Point Hospital (Two Point Studios, 2018)
- Тип: game  
- Ссылка: https://store.steampowered.com/app/535930/  
- Стиль: cartoon hospital, Aardman-like caricature, bright clean flat shading, minimal outlines  
- Визуальные черты: Reviewers compare the look to Aardman stop-motion; characters slightly caricatured with 'minimal shading' giving a low-poly feel (GodisaGeek, CGMagazine 2018 coverage); Art director Mark Smart: 'make the graphics to support the game, not the other way around'; Clean, bright, high-key palette: mint walls ~#CFE8DF, lino floors ~#E7E1D3, teal accents ~#2BA3A0, warning orange ~#F29C38 (approximate); Top-down management camera; readable silhouettes of equipment; chosen to avoid dating (per developer comments); Hospital props (reception desks, beds, GP office, wards) in exactly the locations this project needs  
- Почему подходит: The only widely known stylised hospital art direction; it demonstrates that a cartoon hospital can be read as competent rather than silly, and its clean flat shading is cheap in Cycles.  
- Риски: Its comedy register (ghosts, absurd diseases) is the opposite of a physician-authored learning tool; borrow the clarity, not the jokes. Characters would be expensive to produce procedurally; keep NPCs simple or 2D.  
- Реализуемость в Blender: EASY-MEDIUM. Flat Principled materials, rounded Bevel+Subdivision props, one Sun + world AO; optional thin inverted-hull outline for characters. Characters are the hard part (rigging), not rendering.

### Hi-Fi Rush (Tango Gameworks, 2023)
- Тип: game  
- Ссылка: https://80.lv/articles/the-making-of-hi-fi-rush-s-3d-toon-rendering-style  
- Стиль: deferred toon renderer: cel shading + ink outlines + Ben-Day/halftone accents, comic-book colour  
- Визуальные черты: GDC 2024 talk '3D Toon Rendering in Hi-Fi Rush' (https://gdcvault.com/play/1034251/3D-Toon-Rendering-in-Hi): custom deferred toon renderer in UE4 for characters and environments; comic shader, toon lights, face-shadow handling; Two-band cel shading with coloured shadow tint; black outlines of varying thickness; Ben-Day dots in backgrounds (secondary analyses cite Spider-Verse influence); High-saturation palette: hot pink ~#FF4FA3, cyan ~#2BD9E8, yellow ~#FFD23F, deep purple shadows ~#3B2A5E (approximate); Stepped animation and exaggerated poses reinforce the 2D feel  
- Почему подходит: The reference point for 'cel-shaded with outlines' in 2020s games; its outline + flat-fill language is compatible with a black-ink ECG trace because both are 'ink'.  
- Риски: Its saturation level and dot patterns would drown an ECG strip; adopt the shading model only at ~40% of that chroma. Deferred toon lighting cannot be replicated in Cycles; band quantisation must come from Toon BSDF or compositor.  
- Реализуемость в Blender: MEDIUM. Shading: Toon BSDF (Cycles-only, manual: https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/toon.html; Size ~0.5, Smooth ~0.05) or Emission base + Diffuse Direct pass posterised in compositor (Posterize node, Steps 2-3). Outlines without GPU: (1) Freestyle, a CPU line renderer that works with Cycles (silhouette/crease/border line sets, thickness in px); (2) Grease Pencil Line Art modifier (CPU occlusion, strokes composited over the Cycles image; each modifier recomputes occlusion); (3) inverted hull: Solidify (flip normals, thickness 0.005-0.01) + black Emission material, with Geometry>Backfacing -> Mix Shader(Transparent) because material Backface Culling is ignored in Cycles renders (Katsbits 4.2 note: https://www.katsbits.com/codex/?p=9407); (4) compositor Normal/Z pass -> Filter Sobel/Laplace -> Math Greater Than -> Dilate/Erode for width. Shader-to-RGB cel ramps are EEVEE-only and EEVEE needs a GPU/OpenGL context (headless llvmpipe is slow and flaky), so avoid them.

### Rollerdrome (Roll7, 2022)
- Тип: game  
- Ссылка: https://www.gamedeveloper.com/art/deep-dive-rollerdrome-art-direction-q-a  
- Стиль: ligne claire cel shading (Moebius/Herge), flat fills, uniform thin outlines, brutalist concrete palette  
- Визуальные черты: Lead artist Antoine Dekerle: Moebius and Herge were the references, 'two of the masters of the Ligne Claire style'; Flat colour fills, uniform-weight thin dark outlines, almost no gradients; cel shading chosen to preserve gameplay readability; Palette of naked concrete and dark metal with retro-futurist accents: concrete ~#C9C2B4, shadow ~#7A7366, orange ~#F08A2E, sky teal ~#7FC6C9 (approximate); Brutalist architecture; large empty planes keep the eye on action  
- Почему подходит: Ligne claire is the comic tradition closest to a technical diagram: one line weight, flat local colour, no hatching. That is exactly how an ECG strip is drawn, so scene and strip share a graphic grammar.  
- Риски: Uniform outlines on complex hospital equipment create a lot of black line density that competes with the trace; limit outlines to silhouettes (Freestyle 'Silhouette'+'Border' only, not creases).  
- Реализуемость в Blender: EASY-MEDIUM. Emission or very flat Diffuse fills; Freestyle line set with silhouette+border, thickness 1.5-2 px at 1080p, constant colour #1A1A1A; no crease lines; Film Pixel Filter 1.0. Very fast in Cycles (little lighting noise).

### Sable (Shedworks, 2021)
- Тип: game  
- Ссылка: https://www.gamedeveloper.com/marketing/how-shedworks-refined-the-art-of-sable-in-pursuit-of-readability  
- Стиль: Moebius-style flat colour + thin black outlines + sparse dot stippling, no shading  
- Визуальные черты: Objects 'defined by thin black outlines, shapes coloured in soft tones, without any shading apart from the occasional dotting' (Shedworks interviews); Because of flat shading the team layered fog, lighting and lines to recover depth and readability; Desert palette: sand ~#E8C9A0, dusk violet ~#8C6FA8, teal ~#4FA3A5, warm white ~#F6EFE3 (approximate); Edge-detection outlines on depth/normal buffers (community reconstructions: Maxime Heckel's Moebius post-process, Useless Game Dev video)  
- Почему подходит: Shows that fully flat colour + ink line can hold an open-world game; its 'occasional dotting' is a bridge to halftone/riso and to the pink-dot texture of ECG paper.  
- Риски: Flat shading destroys form on bevelled furniture; depth must be restored with fog/AO. Stipple dots near a 1 mm ECG grid will moire; keep stipple away from the strip panel.  
- Реализуемость в Blender: EASY-MEDIUM. Emission fills + AO pass multiplied in compositor (Cycles AO pass is cheap); outlines via Freestyle or compositor Sobel on Normal pass; stipple via Window-space Voronoi (Texture Coordinate > Window) masked by the AO pass in the compositor.

### Tearaway (Media Molecule, 2013)
- Тип: game  
- Ссылка: https://www.mediamolecule.com/games/tearaway  
- Стиль: papercraft world: folded, creased, torn paper with visible fibre and cut edges  
- Визуальные черты: Rex Crowle's team built every asset physically out of paper first, then adapted the engine so objects 'bend and fold like paper' (PlayStation Blog, Game Informer); Early concepts were 'cut-up painted paper' in the Eric Carle picture-book manner; final version pushes recognisable paper behaviour (creases, bending underfoot, tearing); Palette of coloured card: kraft ~#C8A46C, poster red ~#D94F3D, sky blue ~#7EC4E8, grass green ~#7DBE57, white card ~#F5F2EA (approximate); Visible cut edges (white core of coloured card), paper grain, soft drop shadows between layers; players can print real papercraft models  
- Почему подходит: Paper is the material of the ECG strip itself; a world made of card makes the strip a native object, not an overlay from another universe. Cream/kraft card harmonises with cream ECG paper and pink grid.  
- Риски: Paper grain and fibre noise everywhere competes with the strip's 1 mm grid; keep fibre bump very subtle (strength <=0.03) and never behind the strip. Folding/tearing animation is out of scope; use static papercraft.  
- Реализуемость в Blender: MEDIUM. Material: Principled, base colour of card, Roughness 0.85, Specular 0.2, Subsurface 0.05-0.1 (random walk, radius ~2 mm) for translucency, Bump from Noise (Scale 300-600, Detail 2, Strength 0.02) for fibre. Geometry: Solidify 1-2 mm + Bevel 0.3 mm gives the white cut edge (second material slot via Solidify 'Material Offset' set to a white emission). Layers: flat planes offset 2-5 mm, lit by a hard Sun (angle 1-2 deg) so each layer casts a crisp shadow, the key tell of paper. SSS raises noise: 256-512 samples + OIDN; or drop SSS and mix 10% Translucent BSDF for speed. Procedural cardboard reference: Ryan King Art tutorial (https://www.blendernation.com/2021/11/14/procedural-cardboard-material-blender-tutorial/).

### Lumino City (State of Play, 2014)
- Тип: game  
- Ссылка: https://store.steampowered.com/app/205020/Lumino_City  
- Стиль: photographed handmade paper/cardboard model set, miniature lights, soft practical lighting  
- Визуальные черты: A ~10-foot (3 m) physical city built from paper, card, balsa, miniature lights and motors, partly laser-cut, photographed and used directly in the game (PC Gamer, MCV, Kill Screen coverage); studio site: https://www.stateofplaygames.com/; Warm practical lighting from tiny bulbs, natural paper translucency, visible glue and cut marks; Palette: aged paper ~#E9DCC2, card browns ~#B48A5A, warm lamp ~#FFC978, teal paint ~#3F8E8A, night blue ~#2C3E5C (approximate); Fixed 'theatre' camera per scene; characters are 2D animated paper cut-outs  
- Почему подходит: Shows that a point-and-click adventure can live entirely inside paper dioramas, with each location a self-contained set, which is also the structure of this ECG quest. Cream paper everywhere is the ECG strip's native habitat.  
- Риски: Photographic realism of real paper is hard to fake; digital paper tends to look like plastic unless SSS and imperfections are tuned. Warm tungsten light tints cream ECG paper orange; keep the strip colour-managed separately in the HTML layer.  
- Реализуемость в Blender: MEDIUM-HARD for the full photographic look (SSS + practical point lights + DoF are all noisy on CPU). A stylised approximation (card materials without SSS, 2-3 Point lights with soft shadows, DoF f/2) is MEDIUM. 512-1024 samples with OIDN and Path Guiding (CPU-only feature, helps interior bounce light); minutes per frame on 16 cores (estimate).

### Papetura (Petums, 2021)
- Тип: game  
- Ссылка: https://store.steampowered.com/app/593640/Papetura  
- Стиль: everything photographed from real white paper sculptures, warm backlit translucency, dark surroundings  
- Визуальные черты: Every location, character and object is a hand-made paper sculpture, glued, lit on a photo stage and imported 'in unaltered form' (official site https://papetura.com/); Near-monochrome white paper with warm backlighting; strong translucency and rim light; deep shadows; Palette: paper white ~#F3EEE4, warm glow ~#F6C77A, shadow umber ~#4A3B2E, flame orange ~#F2712F (approximate); Point-and-click framing, fixed cameras, no dialogue  
- Почему подходит: Demonstrates paper translucency as the whole aesthetic; an ECG strip (also paper) with a backlit glow would read as 'held up to the window', a physician's actual gesture.  
- Риски: Dark, moody horror-adjacent tone unsuitable for a bright teaching hospital; take only the translucency idea.  
- Реализуемость в Blender: MEDIUM-HARD on CPU: backlit SSS/translucency is the noisiest Cycles case. Use Translucent BSDF + Principled mix (not full SSS), Area lights behind planes, 512+ samples, OIDN with Albedo+Normal passes.

### Yoshi's Crafted World (Good-Feel / Nintendo, 2019)
- Тип: game  
- Ссылка: https://en.wikipedia.org/wiki/Yoshi%27s_Crafted_World  
- Стиль: cardboard/craft-material dioramas: corrugated card, egg cartons, cups, felt ('flocky'), toy-like  
- Визуальные черты: Stages built from everyday household items 'designed to look like miniature dioramas' (reviews); cardboard cut-outs, strings, toilet-paper rolls, egg cartons form roads, trains, houses; Yoshis are made of a flocked fabric material; backgrounds are visibly cardboard with printed-paper surfaces; Bright craft palette: kraft ~#C9A066, card white ~#F2EEE6, Yoshi green ~#5DBB46, felt red ~#D8443C, blue tape ~#4A90D9 (approximate); Side-on camera with parallax layers; 'blends Good-Feel's craftwork aesthetic with the sheen of Unreal Engine'  
- Почему подходит: Craft-material dioramas offer a ready vocabulary for hospital props (cardboard beds, paper-roll IV poles) that are unmistakably stylised, so nobody mistakes the environment for medical realism while the ECG remains precise.  
- Риски: Reads as children's media; adult learners may find it patronising. Keep craft cues subtle (card edges, matte materials) rather than literal toilet rolls.  
- Реализуемость в Blender: MEDIUM. Corrugated edge via Solidify + Array of small cylinders or a Wave-texture displacement on edge faces; printed-paper look via flat colours + light Noise bump; felt via Velvet/Sheen in Principled (Sheen 0.5). Standard Cycles cost.

### Claybook (Second Order, 2018)
- Тип: game  
- Ссылка: https://store.steampowered.com/app/661920/Claybook  
- Стиль: ray-traced clay world (signed distance fields), soft SSS, fingerprint-free smooth plasticine, miniature-diorama framing  
- Визуальные черты: GPU clay/fluid simulator with SDF modelling and ray-traced visuals on top of UE4 (GDC tutorial: https://www.gdcvault.com/play/1025316/Advanced-Graphics-Techniques-Tutorial-GPU); Rounded, blobby forms with subsurface-scattered plasticine look; soft shadows; table-top diorama scale with books and toys as set dressing; Plasticine palette: red ~#D6453A, blue ~#3C6FD1, yellow ~#F2C230, green ~#4FAE5A, board cream ~#EFE8D8 (approximate); Slight DoF and tilt-shift-like camera reinforce miniature scale  
- Почему подходит: Reference for the clay/toy look's key tells: SSS, rounded edges, matte-but-not-dead specular, and a table-top scale. A 'clay hospital on a desk' keeps the ECG strip as the one crisp, precise object.  
- Риски: SSS and DoF are the two most expensive things in Cycles on CPU; the look can drift toward a children's toy; large smooth surfaces show denoiser smearing.  
- Реализуемость в Blender: MEDIUM. Principled: Subsurface Weight 0.3-0.5, Radius (1.0, 0.5, 0.3) with Scale 0.01-0.02 m, Roughness 0.5-0.7, Specular IOR Level 0.3; Bevel modifier + Subdivision 1-2 for rounded forms; fingerprints via low-strength Noise/Voronoi bump (Jamie Dunbar's 5-step clay: https://bazaar.blendernation.com/listing/5-easy-steps-to-make-realistic-clay/; paid procedural clay shader on Superhive). Tilt-shift: camera DoF f/0.8-2 focused on the subject, long lens (85-135 mm), camera shift_y for straight verticals, slight saturation boost. 512-1024 samples + OIDN; Path Guiding on CPU helps. Several minutes per 1080p frame on 16 cores (estimate).

### Moss (Polyarc, 2018)
- Тип: game  
- Ссылка: https://gamesbeat.com/polyarcs-moss-hides-clever-vr-game-design-under-its-cuteness/  
- Стиль: storybook diorama within arm's reach, true-to-scale miniature, Ghibli-like warm naturalism  
- Визуальные черты: Scenes 'laid out like a diorama, within arm's reach' (Polyarc CEO); world is 'true to scale' so the player feels like a giant looking into a model; Each room is a self-contained diorama framed by stone/wood edges; the fairy-tale set rises out of a book; Warm, naturalistic palette: moss green ~#6F9A4E, stone ~#9C9385, warm lamp ~#F5C97A, night blue ~#2B3C5A (approximate); Soft global illumination, strong AO in crevices, slight DoF toward the edges  
- Почему подходит: The 'diorama you look down into' camera is the natural framing for a physician-player who looks at a desk/bed and then at a strip; it also justifies tilt-shift DoF as diegetic scale rather than a filter.  
- Риски: Naturalistic texturing is costly to generate procedurally; keep materials flat-coloured and let only lighting be naturalistic.  
- Реализуемость в Blender: MEDIUM. Diorama plinth + room; camera 30-45 deg down; DoF f/2.8 with focus on the key prop; HDRI fill (Poly Haven) 0.3 strength + Sun; Fast GI off, Path Guiding on. 256-512 samples + OIDN.

### Tiny Glade (Pounce Light, 2024)
- Тип: game  
- Ссылка: https://store.steampowered.com/app/2198150/Tiny_Glade  
- Стиль: cozy storybook procedural architecture, warm soft sunlight, pastel stone and foliage, no outlines  
- Визуальные черты: Swedish two-person studio; 'refined art style and warm colour palette', storybook castles (press coverage); official page https://pouncelight.games/tiny-glade/; Everything procedurally generated (walls, roofs, ivy) with soft rounded geometry and gentle colour variation; Soft golden-hour sun with long shadows, strong sky fill, light bloom; mild DoF; Palette: stone ~#D8CDBB, roof terracotta ~#C97B5B, ivy ~#7FA65E, sky ~#A9D3EE, warm light ~#FFE2B0 (approximate); Custom temporal upscaler (TGSR); runs on GPU in real time, so the look itself (not the tech) is the reference  
- Почему подходит: The clearest current example of the 'cozy render' trend the author's prototype belongs to: pastel materials + warm soft sun + bloom. It shows that procedural generation (this project's constraint) and a hand-crafted feel are compatible.  
- Риски: Warm bloom and haze lower local contrast; the ECG strip panel needs a flat, unbloomed region (composite the strip in HTML above the render). Golden tint shifts cream ECG paper toward orange if the strip is rendered in-scene.  
- Реализуемость в Blender: EASY-MEDIUM. Sun 3-5 W/m2, angle 3-5 deg, colour ~#FFE2B0, elevation 20-30 deg; world HDRI 0.3-0.5 or sky colour ~#A9D3EE; AgX view transform with 'Medium Contrast' or 'Punchy' look (Blender 4.0+); compositor Glare (Bloom, Threshold 1.0, Size 6-7, Strength 0.05-0.1) and a light Vignette. Interior GI needs Path Guiding (CPU-only) + Light Tree + adaptive sampling (Noise Threshold 0.01, 256-512 samples) + OIDN. 1-4 min per 1080p frame on 8-16 cores (estimate).

### Townscaper (Oskar Stalberg, 2020)
- Тип: game  
- Ссылка: https://store.steampowered.com/app/1291340/Townscaper  
- Стиль: pastel watercolour-like procedural town, soft shading, white trim, calm palette  
- Визуальные черты: 'Vibrant, pastel visual style reminiscent of watercolor paintings' (press); Raw Fury: 'calming art style', player-chosen colours; Procedural wave-function-collapse geometry; smooth rounded blocks with white window trims and red-tile roofs; Pastel house palette (player-selectable swatches): pink ~#F4B9B8, yellow ~#F5D67A, mint ~#9FD6C0, blue ~#8FB8E8, sea ~#4F9DC9 (approximate); Soft ambient lighting, sky-blue fill, thin AO; no outlines  
- Почему подходит: A procedurally generated world whose whole appeal is palette discipline; its swatch-based colouring is exactly how a bpy generator should assign hospital colours (a fixed swatch table per room type).  
- Риски: Watercolour softness can make interiors look foggy; indoor scenes need stronger key light than Townscaper's outdoor ambient.  
- Реализуемость в Blender: EASY. Swatch-driven materials; Sun + sky-colour world; Fast GI Approximation (AO distance 1-2 m) is enough for exteriors; 128 samples + OIDN.

### Blueprint 3D (FDG Entertainment / Zedarus, 2011)
- Тип: game  
- Ссылка: https://www.fdg-entertainment.com/games/blueprint-3d/  
- Стиль: blueprint linework: white/cyan line drawings on blue, rotated in 3D until they resolve  
- Визуальные черты: Each level is a jumble of dots and lines rotated in 3D until it resolves into a blueprint line drawing (Wikipedia; FDG page); Pure linework: thin white/cyan strokes, no fills, on blueprint blue; theme packs vary the paper (graph paper, parchment); Palette: blueprint blue ~#1E4FA3 / #0B3D91, line white ~#F2F6FF, cyan ~#7FD7FF, grid lines ~#2F63B8 (approximate); Grid background is part of the identity  
- Почему подходит: Linework over a grid is the ECG strip's own idiom (ink on graph paper). A blueprint-styled 'cardiology office' or 'exam mode' could show equipment as technical drawings while the strip itself is the only full-colour element, or invert the strip to monitor mode (cyan on dark) to unify.  
- Риски: Grid-on-grid: a blueprint grid behind a 1 mm ECG grid creates moire and false scale cues; suppress the scene grid under the strip panel or align it to 5 mm. Whole-game blueprint is monotonous; better as a mode or for diagrams.  
- Реализуемость в Blender: EASY and the cheapest of all. View layer Material Override with an Emission material of blueprint blue; Freestyle line set (silhouette+crease+border) with Line Style colour #EAF3FF, thickness 1.2 px, optional Dashed Line (dash 8 / gap 4); Blender ships a Freestyle 'blueprint' Python style module among its presets (manual intro: https://docs.blender.org/manual/en/latest/render/freestyle/introduction.html); Wireframe modifier for construction lines; a Checker/Brick texture plane or compositor overlay for the grid. Emission-only scene converges in 8-16 samples; outlines are Freestyle (CPU), so no GPU needed at all.

### Manifold Garden (William Chyr Studio, 2019)
- Тип: game  
- Ссылка: https://history.siggraph.org/?p=77384  
- Стиль: flat-colour Escher architecture with edge-shaded outlines, minimal gradients, pastel sky  
- Визуальные черты: SIGGRAPH 2020 talk 'That's a wrap: Manifold Garden rendering retrospective' (Brussee, Saraev, Chyr) keywords: 'edge shading', 'stylized-rendering', 'toroidal geometry'; cites Decaudin 2009 cartoon rendering; Flat local colour on large architectural planes, thin dark edge lines where faces meet, no textures; Pastel-to-saturated gradient skies; local palettes like cream ~#F3EEDC, slate ~#5A6B7A, lilac ~#C8B6E8, accent orange ~#F08A3C (approximate); Clean anti-aliased lines at any distance (vector-texture style magnification referenced)  
- Почему подходит: Edge-shading on flat planes is exactly what Freestyle crease lines or a compositor Laplace on the Normal pass produce; it gives 'drawn' structure without hatching noise, so an ECG strip stays the busiest element on screen.  
- Риски: Large flat planes read as sterile; hospital rooms need props with bevels to avoid looking like a diagram. The SIGGRAPH abstract does not detail the line algorithm; treat it as a look reference, not a recipe.  
- Реализуемость в Blender: EASY. Emission/flat Diffuse materials; Freestyle crease lines (Crease Angle ~120 deg) + silhouettes, 1 px; or compositor Normal pass -> Filter Laplace -> Math Greater Than 0.3 -> Mix Multiply. Converges in <64 samples.

### Antichamber (Alexander Bruce, 2013)
- Тип: game  
- Ссылка: https://en.wikipedia.org/wiki/Antichamber  
- Стиль: minimalist white world with black edge lines and primary-colour accents  
- Визуальные черты: Deliberately 'simple art style' chosen to stand apart from other Unreal Engine 3 titles and to mask the non-Euclidean trickery (Wikipedia; Digital Spy: 'visually interesting but... austere'); White surfaces, black lines along edges, saturated primary accents for interactive elements; Palette: white ~#FAFAFA, line black ~#111111, accent red ~#E53935, blue ~#1E88E5, yellow ~#FDD835, green ~#43A047 (approximate)  
- Почему подходит: White-with-black-edges is the whiteboard/textbook register; an ECG's black trace and pink grid would be the only non-primary colours on screen and thus unmissable.  
- Риски: Austere and cold; an adult learner may find a whole hospital in this look clinical in the bad sense. Primary accents collide with alert colours; reserve them.  
- Реализуемость в Blender: EASY. White Emission or Diffuse under a white world; Freestyle silhouette+crease lines; or compositor Sobel on Normal pass. Fastest CPU category.

### Spider-Man: Into the Spider-Verse (Sony Pictures Imageworks, 2018) - comp-built print look
- Тип: art-reference  
- Ссылка: https://www.foundry.com/insights/film-tv/graphic-look-in-comp-spiderman  
- Стиль: halftone dots + hatch lines + CMYK misregistration + ink outlines, built in compositing  
- Визуальные черты: Foundry interview: the graphic look was 'created almost entirely in comp' in Nuke; the 'Hatcher' and 'Thresher' tools produced halftone dots and hatch lines; other tools did offset colours, accent ink lines, smearing; Ben-Day dots in mid-tones, hatch lines in shadows, colour-channel offset (misregistration) used to suggest depth of field (secondary breakdowns); Stepped animation (on twos) and hand-drawn accent lines over CG; Riso/offset-print palette feel: CMYK-ish cyan ~#00AEEF, magenta ~#EC008C, yellow ~#FFF200, deep ink ~#1B1B2F (approximate)  
- Почему подходит: Proof that a print-process look (halftone, misregistration, hatching) is a post-process layered on a conventional render, which is exactly how a CPU Cycles pipeline must do it (compositor), not in the shader.  
- Риски: Halftone dots at 1-2 mm screen scale and channel misregistration are destructive to a 1 mm ECG grid and a 1 px trace; the strip must bypass the post-process entirely (render it in SVG/HTML above the image).  
- Реализуемость в Blender: MEDIUM. All in the CPU compositor: Diffuse Direct pass -> RGB to BW -> Posterize (Steps 3-4, manual: https://docs.blender.org/manual/en/latest/compositing/types/creative/posterize.html) -> Math thresholds -> multiply with a screen-space dot pattern (Texture node or an image of a 45 deg dot screen; shader-side alternative: Texture Coordinate > Window -> Mapping -> Voronoi Smooth F1 -> ColorRamp) -> per-channel Separate Color -> Translate nodes (+2/-2 px) -> Combine; hatch lines from a Wave texture at 45/135 deg masked by the shadow band; Kuwahara (Anisotropic) node for painterly flattening (https://docs.blender.org/manual/en/latest/compositing/types/creative/kuwahara.html). Note the common Blender Spider-Verse tutorials (e.g. GarageFarm) use Shader to RGB, which is EEVEE-only; in Cycles drive the masks from render passes instead. OSL halftone shaders are another route and OSL runs only on CPU/OptiX in Cycles, so the CPU constraint is an advantage here (Superhive 'Advanced Halftone Shader Pack, 5 OSL shaders for Cycles': https://superhivemarket.com/products/advanced-halftone-shader-pack--5-osl-shaders-for-cycles; also the older node-only CMYK halftone group by Ben Simonds: https://bensimonds.com/2013/02/14/halftone-shader/).

### Return of the Obra Dinn (Lucas Pope, 2018)
- Тип: game  
- Ссылка: https://obradinn.com/  
- Стиль: 1-bit dithered 3D (early-Macintosh look), stable screen-space dither, wobbly ink outlines  
- Визуальные черты: Real-time 1-bit dithering over a 3D first-person world; Pope's TIGSource devlog (topic 40832) documents the effort to make the dither stable and legible ('keeping everything legible without it becoming an unreadable mess of dithered pixels'); Dither pattern fixed to the scene so it reads as texture rather than shimmer; optional palettes (Mac white/black, amber, green phosphor); Palette: paper ~#E9E2CF / ink ~#1E1D1B, or phosphor green ~#33FF66 on ~#0B1A12 (approximate); Line-work edges plus dither tone; no gradients at all  
- Почему подходит: Two-colour dither on a cream/black or green/black palette is literally the look of a thermal ECG printout or an old monitor; a 'monitor mode' using Obra Dinn's green phosphor palette would unify scene and trace perfectly.  
- Риски: Dither pixels at 1 px interfere with a 1 px ECG trace; strips must be excluded from the dither pass. Whole-game 1-bit is fatiguing for long study sessions; use for a specific location (e.g. ICU monitor view) or as a toggle.  
- Реализуемость в Blender: EASY in the compositor: render Diffuse/Combined -> RGB to BW -> Mix with an ordered Bayer-matrix image (tiled via Scale/Translate, or a Texture node Checker/Brick) -> Math Greater Than; community recipe on BlenderArtists 'Halftone pattern in Blender' thread (https://blenderartists.org/t/halftone-pattern-in-blender-update/1136023) renders grayscale then maps a Bayer matrix. Outlines via Freestyle with the 'Perlin Noise 1D' geometry modifier for wobble. Negligible render cost beyond the base pass.

### NUTS: A Surveillance Mystery (Joon, Pol, Muutsch, Char & Torfi / Noodlecake, 2021)
- Тип: game  
- Ссылка: https://www.gameinformer.com/2021/02/01/nuts-a-squirrel-surveillance-game-comes-to-switch-and-pc-this-week  
- Стиль: three-colour flat 3D silhouettes per chapter, print-like limited palette, luminous outlines  
- Визуальные черты: 'Striking 3D art style made up of only about three different colors at any point'; each chapter swaps the palette (AppUnwrapper, A Most Agreeable Pastime reviews); 'Moody, flat-coloured silhouettes that fade eerily into the distance' (Everand preview); 'spectral, vibrant outlines' (Game Informer); Example chapter palette: forest ~#1F3A2E / ~#E8A33D / ~#F4E9D8; later chapters shift to pink/violet (approximate); No textures, no shading gradients; depth via colour-banded fog  
- Почему подходит: The nearest thing in 3D games to a risograph print: two or three spot colours plus paper, with depth as flat bands. A hospital in 'three colours + ECG black/pink' is a disciplined, memorable palette strategy. (No source states a riso intent; this is a visual analogy.)  
- Риски: Three colours leave no room for medical colour semantics (cyanosis, red alerts); use it for cut-scenes/transitions rather than the main play view.  
- Реализуемость в Blender: EASY. Emission materials + Mist pass -> ColorRamp with 3 constant stops in the compositor (Interpolation Constant) to band depth; Freestyle outlines in the accent colour. Converges in <32 samples.

### Mundaun (Hidden Fields / Michel Ziegler, 2021)
- Тип: game  
- Ссылка: https://store.steampowered.com/app/720350/Mundaun  
- Стиль: hand-pencilled greyscale textures on 3D geometry, graphite hatching, paper grain  
- Визуальные черты: Every texture is hand-sketched in pencil by Ziegler and mapped onto 3D models; 'working in a rather painterly way with pencil makes the art fairly tolerant of being mapped onto 3D' (Game Informer, Gematsu coverage); Greyscale with occasional desaturated colour; visible graphite hatching for tone; paper-grain overlay; soft vignette; Palette: paper ~#E6E1D6, graphite mid ~#8C8780, deep ~#2E2B28, with a rare sepia ~#9A7B5A (approximate); First-person, Alpine horror; the technique, not the tone, is the reference  
- Почему подходит: Pencil hatching on cream paper is the 'medical textbook plate' register (Gray's Anatomy, Netter); an ECG trace in black ink on pink grid sits naturally on a graphite-drawn desk.  
- Риски: Hand-drawn textures cannot be generated procedurally with the same charm; procedural hatching looks mechanical unless jittered. Hatch strokes are lines like the trace; use lighter weight (0.5 px) and 45 deg orientation to differentiate from the 2 px horizontal-scrolling trace.  
- Реализуемость в Blender: MEDIUM. Compositor hatching: Diffuse Direct (or AO) pass -> RGB to BW -> Posterize 4 steps -> per-band Math thresholds -> multiply by 1-3 layered Wave textures (Texture node, Window/screen space, 45/135 deg, slight Noise distortion) -> Mix Multiply over a cream paper plate; outlines via Freestyle with a stroke Texture (Line Style > Texture, pencil alpha brush) and Perlin Noise 1D geometry modifier; the Freestyle Python API's BlenderTextureShader assigns textures to strokes (https://docs.blender.org/api/current/freestyle.shaders.html). OSL hatching shaders are also CPU-native. Cheap in render time; the work is in tuning.

### Borderlands (Gearbox, 2009) - 'inked' hand-drawn style
- Тип: game  
- Ссылка: https://gamespot.com/articles/behind-borderlands-11th-hour-style-change/1100-6253257/  
- Стиль: inked outlines over hand-drawn scanned textures with hatching in recesses ('concept art style')  
- Визуальные черты: Gearbox calls it 'inked', not cel-shaded: always-present black outlines placed on top of 3D, plus hand-drawn, scanned and Photoshop-coloured textures with software that 'adds outlines, sharpens shadows, and draws lines on hills and inclines' (GameSpot/Destructoid-era coverage); Hatched lines in recessed surfaces; 'the less important the line, the thinner it should be' (Polycount artists' analysis); Desert palette with saturated accents: sand ~#D8B27A, rust ~#B5542F, teal ~#2E8B8B, ink ~#141414 (approximate)  
- Почему подходит: The most widely shipped example of cross-hatch tone + ink outline in 3D; demonstrates line-weight hierarchy (thick silhouette, thin detail, thinnest hatch), a rule that keeps hatching from competing with an ECG trace.  
- Риски: Grimy, aggressive texturing is tonally wrong for a clinic; keep only the line-weight hierarchy. Hand-drawn textures are not procedural.  
- Реализуемость в Blender: MEDIUM. Freestyle with two line sets: silhouette (2 px) and crease (0.8 px); hatching as described for Mundaun; a subtle Noise-based 'scanned paper' overlay in the compositor.

### Gray's Anatomy (1858) plates by Henry Vandyke Carter
- Тип: art-reference  
- Ссылка: https://adlib.rcseng.ac.uk/Details/archive/110004656  
- Стиль: wood-engraved anatomical plates: black ink cross-hatch tone on cream paper, labelled leader lines  
- Визуальные черты: Carter drew directly in reverse onto woodblocks; engraved by Butterworth and Heath (Royal College of Surgeons archive of India proofs; HathiTrust scans); Tone built entirely from parallel and cross hatching; contour lines thicker than hatch; serif capital labels with thin leader lines; Palette: paper ~#F2E9D6 / #EFE4C8 (aged), ink ~#1C1A17, label red (later editions) ~#B23A2E (approximate); Form read by hatch direction following surface curvature  
- Почему подходит: For a physician-authored ECG course, the engraving register signals 'textbook authority'; black ink on cream is the same material family as an ECG printout, so a plate-style office or reference cards harmonise with the strip without any colour clash.  
- Риски: Dense hatching is visual noise by definition; must be reserved for small vignettes, borders and portraits, never as full-screen environment art behind a strip.  
- Реализуемость в Blender: MEDIUM-HARD to do convincingly (curvature-following hatching needs UV- or tangent-aligned Wave textures per object, or OSL); EASY for screen-space hatching (compositor) which looks more like a photocopy than an engraving. Use Freestyle for contours and compositor hatch for tone; render only diffuse passes, so very fast.

### Max Brodel - carbon dust technique (Johns Hopkins, Dept. of Art as Applied to Medicine, 1911)
- Тип: art-reference  
- Ссылка: https://en.wikipedia.org/wiki/Max_Br%C3%B6del  
- Стиль: carbon-dust medical illustration: smooth velvety greyscale tone, crisp highlights, halftone-print ready  
- Визуальные черты: Brodel pioneered carbon dust as the dominant medical-illustration technique; founded the Hopkins Department of Art as Applied to Medicine in 1911 (Hopkins Biomedical Odyssey blog, LITFL); Tone laid as powdered carbon on coated board, lifted with erasers for highlights: continuous mid-grey gradients, deep blacks, no visible strokes (unlike engraving); Palette: board white ~#F4F1EA, mid grey ~#8A8A8A, black ~#141414, occasional red-ink labels ~#C0392B (approximate); Designed to reproduce well in halftone printing  
- Почему подходит: A smooth-greyscale rendering mode (no hatching) that still reads as 'medical plate'; it is cheap in Cycles (greyscale diffuse + AO + a little grain) and does not fight the ECG trace with extra lines.  
- Риски: Greyscale environments can look like unfinished clay renders; needs the carbon-dust tells (paper texture, eraser highlights, vignette) and a typographic frame.  
- Реализуемость в Blender: EASY. Greyscale materials or a desaturate in compositor; AO pass multiplied; Glare Fog Glow for eraser highlights; subtle film grain; vignette. 128 samples + OIDN.

### Blender Freestyle (CPU line renderer, works with Cycles)
- Тип: app  
- Ссылка: https://docs.blender.org/manual/en/latest/render/freestyle/introduction.html  
- Стиль: engine-independent edge/line NPR renderer (silhouette, crease, border, material boundary) with line styles and Python styles  
- Визуальные черты: Manual: 'edge/line-based NPR rendering engine' using mesh data and Z-depth; enabled in Render properties, configured per View Layer (view map -> line sets -> line styles); Ships Python styles including 'Japanese big brush, cartoon, blueprint, thickness-with-depth'; Line styles support dashed lines, thickness/alpha modifiers, textures on strokes, geometry modifiers (Backbone Stretcher, Perlin Noise 1D/2D for hand-drawn wobble); Limitations (manual): memory-heavy (all meshes loaded at once), mesh-only, no face-intersection edges, output has no Z-depth, no panoramic cameras  
- Почему подходит: Directly answers 'are outlines achievable in Cycles without a GPU': yes. Freestyle is a CPU post-pass independent of the render device, and it runs under `blender -b` with the Cycles CPU device.  
- Риски: Adds seconds to minutes per frame on dense scenes; no intersection lines (use the Line Art modifier for those); lines are rasterised after the render so they ignore DoF/motion blur unless composited with masks.  
- Реализуемость в Blender: EASY. bpy: scene.render.use_freestyle=True; view_layer.freestyle_settings.linesets.new(); lineset.select_silhouette/crease/border; linestyle.thickness, color, use_dashed_line.

### Blender Grease Pencil Line Art modifier (CPU, 2.93+)
- Тип: app  
- Ссылка: https://docs.blender.org/manual/en/latest/grease_pencil/modifiers/generate/line_art.html  
- Стиль: camera-based line generation from scene/collection/object into Grease Pencil strokes (contour, crease, intersection, material border, loose, light contour, cast shadow)  
- Визуальные черты: Manual: generates stylised lines from scene, collection or object; needs an active camera; edge types include Contour/Silhouette, Crease (threshold), Intersections, Material Borders, Edge Marks, Loose, Light Contour and Cast Shadow; Illumination filtering; Fill Strokes option; Occlusion computed per modifier ('each Line Art modifier will run the entire occlusion calculation for itself'); strokes can be baked; Grease Pencil strokes are rendered by Blender's GP pipeline and layered over the Cycles image (community Cycles workflows: Lester Banks 2021 https://lesterbanks.com/2021/07/a-fast-way-to-create-a-line-art-effect-in-blender/; BlenderNation 2024 notes it is 'great if you want to render NPR style in Cycles, but... resource-demanding' https://www.blendernation.com/2024/05/03/baking-line-art-modifier/)  
- Почему подходит: Second CPU route to outlines in Cycles, with intersection lines (which Freestyle lacks) and GP stroke materials (textured, tapered). Lines can also be exported as SVG from Grease Pencil, which matches the project's SVG UI layer.  
- Риски: Slow on heavy scenes (occlusion is CPU brute force); strokes are camera-locked (bake per shot); GP Visual Effects (pixelate, blur) are viewport-oriented and the manual recommends the compositor for precision.  
- Реализуемость в Blender: EASY-MEDIUM. bpy: add a Grease Pencil object, modifier type 'GP_LINEART' (GPv3 in 4.3+: 'GREASE_PENCIL_LINE_ART'), source_type='SCENE', use_crease/use_intersection, thickness; bake with bpy.ops.object.lineart_bake_strokes().

### BNPR 'Edge Nodes' - compositor edge detection for Cycles
- Тип: art-reference  
- Ссылка: https://blendernpr.org/?p=1191  
- Стиль: compositor outlines from Normal/Z passes (Laplace/Sobel + threshold), engine-agnostic  
- Визуальные черты: Normal pass 'holds most of the information necessary to detect edges'; Laplace filter on the Normal pass, blur, per-channel Math Greater Than, recombine, use as a mix factor for dark lines; Z-pass variants need fiddly curve/ramp tuning; early results gave >=3 px lines and noise; Dilate/Erode is the standard width control (manual Filter node types: Soften, Laplace, Sobel, Prewitt, Kirsch, Shadow: https://docs.blender.org/manual/en/latest/compositing/types/filter/filter.html); Works on any engine because it only consumes render passes  
- Почему подходит: Third CPU route to outlines; useful when lines must respect DoF or be colour-graded with the image, and it runs in the CPU compositor during `blender -b` renders.  
- Риски: Line width is hard to keep constant (devtalk thread on Sobel width); noisy on fine geometry; needs anti-aliased passes (render at 1.5-2x and downscale) to avoid jaggies.  
- Реализуемость в Blender: EASY. Enable Normal and Z passes; node chain Filter(Laplace) -> Blur(1 px) -> Math(Greater Than 0.2) -> Dilate/Erode(-1..+1) -> Mix(Multiply) with the Combined pass.

### ParaNormal Toon Shader (light-driven NPR for Cycles & EEVEE)
- Тип: app  
- Ссылка: https://superhivemarket.com/products/paranormal-toon-shader/docs  
- Стиль: Cycles-compatible cel shading by re-aligning normals toward a reference light (no Shader to RGB)  
- Визуальные черты: Vendor docs: procedurally 'parallelizes shaded surface normals relative to the primary light source'; works in Cycles without Shader to RGB; needs a reference light object; multi-light scenes are awkward; Vendor also notes most toon assets rely on Shader to RGB (EEVEE-only), 'which will limit your ability to take advantage of existing resources' in Cycles  
- Почему подходит: Documents the practical constraint that shapes this whole project: banded cel shading in Cycles must be driven either by the Toon BSDF, a normal/light-direction trick in the shader (Vector Math dot product with a driver-fed light direction), or by posterising passes in the compositor.  
- Риски: Paid add-on; single-light assumption; author should prefer a self-written node group (dot(N, L) via Normal Map + Vector Math, ColorRamp Constant) to stay fully procedural.  
- Реализуемость в Blender: EASY-MEDIUM. DIY version: Geometry>Normal -> Vector Transform (World) -> Vector Math Dot with a Combine XYZ driven by the Sun rotation -> ColorRamp (Constant, 2-3 stops) -> Emission. Converges in <32 samples.

### ECG-Image-Kit (Shivashankara et al., arXiv 2023)
- Тип: research-paper  
- Ссылка: https://arxiv.org/abs/2307.01946  
- Стиль: synthetic ECG-paper image generator documenting grid geometry and typical colours  
- Визуальные черты: Standard paper ECG: coarse 5 x 5 mm grid (0.5 mV / 0.2 s) and fine 1 x 1 mm grid (0.1 mV / 40 ms) at 25 mm/s, 10 mm/mV; 'Most paper ECG grids are red-pink in color, but there is no widely accepted standard for ECG paper color' (some devices use blue or green grids); Typical reproduction values (approximate, consistent with the paper's red-pink description): paper #FFF8F0, 1 mm grid #F6C6C6, 5 mm grid #E88C8C-#D9534F, trace #111111  
- Почему подходит: Fixes the colour anchors every environment palette must harmonise with: warm cream + pink/red grid + near-black ink. Rule of thumb derived from it: keep scene chroma in the red hue range (0-15 deg) below the grid's, so the strip is the only saturated red-pink object.  
- Риски: If scene palettes include coral (the prototype's #E8A598-ish accents), they sit close to the grid's hue; shift coral toward salmon-orange (hue ~20-25 deg) or lower its saturation.  
- Реализуемость в Blender: n/a (reference). For in-scene strips, render the SVG to an Image Texture on an Emission plane at 1:1 pixel scale and keep view transform 'Standard' for that plane via a separate view layer, or composite the strip in HTML above the render (recommended).

### APSF: 'Colors for ECG Tracings, SpO2 Pulse Oximetry on Patient Monitors in the OR and ICU'
- Тип: research-paper  
- Ссылка: https://www.apsf.org/article/colors-for-ecg-tracings-spo2-pulse-oximetry-on-patient-monitors-in-the-or-and-icu/  
- Стиль: monitor-aesthetic colour conventions (green ECG, red arterial, contested SpO2) for dark 'ICU mode' palettes  
- Визуальные черты: Green is the common convention for ECG waveform/HR and red for invasive arterial pressure; APSF proposes pulse oximetry yellow, CO2 white, temperature cyan, while many monitors and exam sources use blue/cyan for SpO2 pleth; Colour-blindness caveat: red-green deficiency in ~10% of men; standardisation 'helpful but not practical'; Suggested dark-mode palette: background #0A0F14, ECG green #33FF66 or #00E676, pleth cyan #00E5FF (or yellow #FFD500 per APSF), ABP red #FF3B30, text grey #B0BEC5  
- Почему подходит: Gives the second legitimate colour world for the game (ICU/ER scenes on dark monitors) with a cited rationale; green-on-black traces harmonise with teal/mint pastel rooms better than with coral.  
- Риски: Mixing paper-mode (pink grid) and monitor-mode (green on black) strips in one screen is jarring; switch mode per location (ward = paper, ICU = monitor).  
- Реализуемость в Blender: n/a (reference). For monitor props in-scene: Emission plane, strength 2-4, with Glare Bloom; keep real strips in the HTML layer.

**Выводы агента:**

- Outlines in Cycles without a GPU are not a problem: there are four fully CPU routes (Freestyle, Grease Pencil Line Art modifier, inverted-hull geometry, compositor edge detection on Normal/Z passes). The only outline/cel technique that is off the table is anything built on Shader to RGB, which is EEVEE-only, and EEVEE itself needs an OpenGL/Vulkan context (headless llvmpipe is slow and unreliable). Toon BSDF, by contrast, is Cycles-only.
- The CPU constraint is an advantage for print-process looks: OSL shaders (halftone, line screens, hatching) run only on the CPU (and OptiX) device in Cycles, so risograph/halftone/cross-hatch shaders that GPU users cannot use are available here. Path Guiding is also CPU-only and materially helps interior bounce light for the cozy look.
- Render cost ranking on CPU (estimates for 1080p, 8-16 cores): emission/flat-fill looks (blueprint, Monument-Valley flat, NUTS-style bands) converge in 8-32 samples, seconds per frame; flat low-poly with Sun + Fast GI Approximation 32-128 samples, tens of seconds; cozy pastel interiors with real GI 256-512 samples + OIDN + Path Guiding, 1-4 min; clay/paper with SSS and tilt-shift DoF 512-1024 samples, several minutes. Every post-process look (halftone, dither, hatching, Kuwahara, Posterize, Glare) is nearly free in the CPU compositor.
- Any screen-space post-process (halftone dots, dither, misregistration, hatching, film grain, bloom) must exclude the ECG strip: a 1 mm grid and a ~1-2 px trace are destroyed by dots or channel offsets of the same scale. Composite the SVG strip in the HTML layer above the rendered background; never bake it into the frame.
- Palette discipline is the real harmonisation rule: reserve the red-pink hue band (roughly 0-15 deg hue, saturation above ~40%) for the ECG grid and alerts; keep room palettes in cream/mint/teal/muted wood with coral pushed toward salmon-orange or desaturated. For dark ICU/ER scenes, switch to a monitor palette (green trace #33FF66, cyan pleth, red ABP on #0A0F14) which sits comfortably with teal/mint pastels.
- Grid-on-grid is a specific hazard for blueprint and paper looks: a scene grid or paper fibre at 1-5 mm visual scale creates moire and false scale cues behind the strip. Suppress scene grids under the strip panel or align them to 5 mm, and keep paper-fibre bump strength at or below ~0.03.
- Isometric/orthographic dioramas (room-in-a-box) are both the cheapest to generate procedurally in bpy and the best frame for a 2D overlay: the orthographic camera removes perspective cues that would make a flat SVG panel look pasted on, and the cut-away room gives a diegetic desk/bed surface where the strip can first appear as a prop.
- Ink-line styles (ligne claire, blueprint, engraving) share a graphic grammar with the ECG trace, which makes the strip feel native, but they also compete with it line-for-line. The fix is a line-weight hierarchy: scene silhouettes about 1-1.5 px, creases and hatches at or below 0.5-0.8 px, strip trace 2 px, and hatching oriented at 45 deg so it never reads as a horizontal waveform.
- The hospital setting has one strong stylised precedent (Two Point Hospital, Aardman-like caricature with minimal shading) and it demonstrates that clean flat shading, not detailed texturing, is what keeps equipment readable; its comedic register should not be imported. The Almost Gone and Button City show that pastel dioramas can carry adult, even sombre, narrative content.
- Flat-but-soft low-poly is best achieved as Alba does it: custom normals transferred from a smoothed proxy plus gradient ramps, which in Blender is a Data Transfer modifier and a ColorRamp, both trivially scriptable; this avoids the 2014 'visible triangles' cliche while staying cheap.

## Как сделать больницу приятной: игры, анимация, архитектура

### Two Point Hospital (Two Point Studios / SEGA, 2018)
- Тип: game  
- Ссылка: https://store.steampowered.com/app/535930/Two_Point_Hospital/  
- Стиль: cartoony claymation-like 3D hospital sim, soft pastel rooms with saturated accent props  
- Визуальные черты: Isometric-ish free-orbit 3D camera; rooms read as dioramas with low walls so interiors are always visible; Art director Mark Smart: 'make the graphics to support the game, not the other way around' (CGMagazine); previewed as 'Aardman Animations-esque', deliberately cute/cartoony to stay timeless rather than realistic (DualShockers); Observed palette (my approximation, not published by the studio): cream/off-white walls ~#F3EEE4, pale mint/teal tile floors ~#9FD3C7 / #5FB3A7, orange-coral accents on equipment ~#F28C4B, light wood ~#D9B98A; characters more saturated than rooms; Rounded, bevelled, slightly chunky furniture; no outlines, soft shading, strong ambient occlusion under objects; Exaggerated readable animation sized to read from a distance (Ben Hymers, TheSixthAxis interview); illnesses are visual gags, no gore; Equipment is 'cardiology-coded' instantly: wheeled carts, big single-colour machines with one screen; medical props simplified to silhouettes  
- Почему подходит: It is the canonical proof that a hospital can look warm and funny without visual noise: neutral cream rooms, one pastel floor colour, one accent colour on machines. The same recipe leaves the ECG strip as the only high-contrast element on screen. Its diorama rooms (reception, ward, treatment rooms) map one-to-one onto the game's locations.  
- Риски: Its comedy tone can undermine a physician-authored serious course; copying the look too closely reads as parody. Character style is expensive; the environment recipe is what to borrow.  
- Реализуемость в Blender: medium: room shells, bevelled low-poly furniture (bevel modifier + smooth shading), flat pastel Principled materials, sun + large area fill, Cycles AO/denoise on CPU is cheap at 128-256 samples. Characters in this style are hard in bpy; use 2D portraits in the HTML UI instead.

### Theme Hospital (Bullfrog / EA, 1997) and CorsixTH
- Тип: game  
- Ссылка: https://en.wikipedia.org/wiki/Theme_Hospital  
- Стиль: isometric cartoon pixel-art hospital, cream floors with saturated per-room colour  
- Визуальные черты: Fixed isometric view, pixel art; graphics 'modelled from those of cartoons', reviewed as 'cute', 'large and colourful' (Wikipedia citing PC Gamer / CVG); Flat cream/beige corridor floors, each room type carpeted in its own colour so function is readable at a glance; Thick black-ish outlines on sprites, one-pixel highlight rims; props are chunky and symbolic (big red cardiogram machine, bed with a green blanket); Visual humour via illness shapes (Bloaty Head, King Complex); nothing medical is rendered realistically; CorsixTH (MIT-licensed open-source engine) lets you study the original tile set and palette at any resolution  
- Почему подходит: Demonstrates room colour-coding as wayfinding and that a limited, slightly desaturated environment lets bright UI elements dominate. Its 'one machine = one colour block' convention is a good model for defibrillator / ECG cart props.  
- Риски: Pure pixel art collides with the vector-precise millimetre SVG strip; mixing the two scales looks inconsistent unless the strip is always rendered on top as a UI layer.  
- Реализуемость в Blender: medium: orthographic camera at 30-degree/45-degree isometric angle is trivial in bpy; a convincing pixel look needs low-res render + nearest-neighbour upscale + palette quantisation in the compositor, which can look muddy. Easier to take only the layout and colour-coding ideas.

### Project Hospital (Oxymoron Games, 2018)
- Тип: game  
- Ссылка: https://store.steampowered.com/app/868360/Project_Hospital/  
- Стиль: 2D isometric semi-realistic hospital sim with muted clinical palette and real diagnostics  
- Визуальные черты: Steam tags: 2D, Isometric, Realistic, Stylized; fixed isometric sprites with fine detail (reviewers: 'rendered in excruciating detail'); Muted realistic palette: white/pale-grey walls, light blue-grey floors, pale wood, mid-grey equipment; low saturation so patients and UI icons stand out; Realistic department structure incl. cardiology, ICU and 'cardiography' rooms; ECG is an orderable examination (Steam community / mod changelogs), i.e. a precedent for ECG-as-gameplay in a hospital sim; Diagnostic flow: examinations and lab tests as puzzle, which is close to the ECG game's loop; Customisable materials/colours per room (store description)  
- Почему подходит: Closest existing game to the author's goal: plausible medicine, calm realistic rooms, and an interface where examinations (including ECG) carry the decision-making. Shows that a quiet grey-blue environment plus a strong UI reads as 'serious and credible'.  
- Риски: Its realism is dense and busy; too many small props compete with a strip. Also the palette is cool and slightly sterile, the opposite of the warm pastel prototype; borrow the credibility, not the greyness.  
- Реализуемость в Blender: hard for the full density of props; medium if you keep only a few hero props per room (bed, monitor, ECG cart) and use the muted blue-grey + pale wood materials.

### That Dragon, Cancer (Numinous Games, 2016)
- Тип: game  
- Ссылка: http://www.thatdragoncancer.com/  
- Стиль: flat-shaded low-poly hospital rooms, faceless characters, warm calm lighting  
- Визуальные черты: Low-poly, flat-shaded geometry; reviewers call it 'striking, beautifully lit low-poly art' and 'stripped-back and simple'; Characters have no facial features; emotion carried by posture, colour and light; Hospital rooms described as 'cramped and cluttered, covered in warming and calm colors'; a pediatric ward scene with greeting cards lining walls and ceiling; Warm sunlight through windows, soft shadows; hospital props (IV pole, bed, monitor) reduced to simple extruded shapes; Only the cancer is rendered as black jagged forms: colour contrast is reserved for meaning  
- Почему подходит: Proves that a hospital rendered as faceless low-poly dioramas can feel humane, not sterile, and that reserving pure black for one meaningful element works. Transfer: the only pure black in your scenes should be the ECG trace.  
- Риски: Subject matter is grief; the visual language can read as melancholic. Keep key and fill lights warmer and brighter than the game does.  
- Реализуемость в Blender: easy: this is the cheapest style for bpy on CPU (decimated meshes, flat shading, no textures, single sun + sky, 64-128 samples with denoising). Faceless capsule characters are feasible procedurally.

### Big Hero 6 / Baymax (Walt Disney Animation Studios, 2014; series Baymax!, 2022)
- Тип: art-reference  
- Ссылка: https://en.wikipedia.org/wiki/Big_Hero_6_(film)  
- Стиль: soft white vinyl healthcare robot, rounded forms, white + single red accent  
- Визуальные черты: Baymax's design came from Carnegie Mellon soft-robotics research (Chris Atkeson's inflatable vinyl arm); Don Hall: 'He had me at vinyl'; artist Lisa Keene pushed for a huggable form; Face from a Japanese suzu bell: two dots and a line; concept by mecha designer Shigeto Koyama; Hyperion renderer developed so light passes through translucent vinyl: subsurface-scattered matte white is the 'friendly medical' material; Palette logic: warm oranges for home/Hiro vs cool blues/purples for tech; Baymax stays white with red armour accents; San Fransokyo mixes retro and advanced tech, so medical devices look approachable rather than clinical  
- Почему подходит: Baymax is the best-known example of making healthcare technology feel kind: rounded silhouette, matte translucent white, minimal face, one accent colour. Apply the same to monitors, defibrillator and ECG cart: rounded white shells with one coral/red accent and a dark screen that carries the green trace.  
- Риски: Disney IP; do not copy the character. Pure white SSS surfaces can blow out in Cycles and compete with cream ECG paper; keep device whites slightly cooler than paper whites.  
- Реализуемость в Blender: easy for materials and props: Principled BSDF with subsurface 0.1-0.2, roughness 0.5, bevelled rounded boxes. Hard for an expressive character; keep to props.

### Maggie's Leeds (Heatherwick Studio, 2020)
- Тип: studio  
- Ссылка: https://www.azuremagazine.com/?p=177441  
- Стиль: blonde spruce timber, lime plaster, plants and daylight: cancer-care architecture that feels like a home  
- Визуальные черты: Three mushroom-shaped volumes with prefabricated blonde spruce frames in a radial pattern; curved ceilings; lime-plaster walls (porous, natural); Palette: pale spruce ~#E7CDA6, lime plaster off-white ~#F2EDE3, foliage greens; no institutional colours at all; Sunlit communal spaces along a glass facade; integrated lighting in shelves and roof edges (Architecture Today); Shelves and windowsills hold visitors' own objects and pot plants: 'a sense of home'; custom curved kitchen tables as the social hub; Rooms: private counselling rooms at the centre, communal kitchen, library, exercise room; Thomas Heatherwick: 'kinder, more empathic ways to design places'; Photography: Hufton + Crow  
- Почему подходит: The reference for the game's cardiology office and reception: wood + plants + cream + daylight. Blonde spruce and lime-plaster cream are warm neighbours of ECG paper cream, so a strip pinned on a timber desk harmonises without competing.  
- Риски: Full-scale lush greenery and curved timber fins are heavy for CPU rendering; too much wood grain texture adds noise around the strip.  
- Реализуемость в Blender: medium: radial timber fins via array/curve modifiers, flat 'wood' colour instead of textures, a few low-poly plants; sun through large windows is cheap in Cycles. Avoid high-poly foliage.

### The Royal Children's Hospital, Melbourne (Billard Leece Partnership + Bates Smart, 2011)
- Тип: studio  
- Ссылка: https://www.indesignlive.com/projects/royal-childrens-hospital-by-blbs  
- Стиль: nature-themed colour-per-floor wayfinding, timber and vinyl, 'quiet calm reassurance'  
- Визуальные черты: Base palette mapped from the natural hues of the adjacent Royal Park (bark tones etc.); each level themed on a Victorian landscape (e.g. lower ground 'Underwater' / Port Phillip Bay) for wayfinding; Won Dulux Colour Awards 2012 Grand Prix and the 2012 AIDA Colour in Commercial Design award: 'dynamic, complex and richly researched' palette; Colour applied across signage, paint, joinery, vinyl, furniture and soft furnishings; timber used 'where we could' alongside plasterboard and vinyl (Mark Healey); Nature graphics in high-stress spots (MRI room, transfer lifts); big atrium artwork (Alexander Knox 'Creature', Jade Oakley mobiles); Design intent: 'deinstitutionalise the experience' (Ron Billard), 'quiet calm reassurance' (Kristen Whittle)  
- Почему подходит: Gives the game a defensible rule: one hue family per location (reception, ward, ICU, ER, office, ambulance) so the player always knows where they are, while all hues stay desaturated enough that the pink grid remains the brightest warm element.  
- Риски: Children's-hospital colour intensity can look juvenile for adult learners; take the per-floor system, not the saturation.  
- Реализуемость в Blender: easy as a system: one bpy palette dictionary per location, swap wall/floor/joinery colours; the actual artworks are not needed.

### Sumiyoshido Kampo Lounge acupuncture clinic (id inc, Aichi, Japan, 2014) with Aloop Clinic & Lab (Keiji Ashizawa, Ginza, 2023) as sibling
- Тип: art-reference  
- Ссылка: https://www.dezeen.com/2014/11/05/sumiyoshido-kampo-lounge-clinic-acupuncture-id-inc-mint-interior-cabinets-japan/  
- Стиль: mint-green cabinetry and ceiling, pale wood floor, white treatment rooms with soft drapery  
- Визуальные черты: Tiers of mint-green square-drawer cabinets from a green-painted ceiling down to a pale wooden floor; apothecary jars in open drawers (Dezeen / Ignant); id inc: mint 'freshly expresses a world of herbal medicine'; soft colour creates a 'curiously ambivalent atmosphere'; Separation of zones: green lounge, white waiting room as entrance, white acupuncture rooms wrapped in drapery; Aloop (Keiji Ashizawa): white plaster walls + wood panelling and doors, Karimoku furniture, Kvadrat wool, intentionally rounded corners and furniture edges; 'residential calm... like a hotel or living space' (keijidesign.com/en/works/aloop-clinic-lab/); Suggested hex family derived from these: mint #BFE3D0, deeper mint #8FCDB4, pale maple #EADBC0, warm white #F7F4EE  
- Почему подходит: Mint/teal sits opposite the ECG grid's pink-red on the colour wheel, so a mint environment makes the strip pop while staying calm; white rooms with drapery give an ICU/ward feel that is soft, not sterile. Rounded corners (Aloop) are a cheap bevel in bpy.  
- Риски: A whole mint room can turn 'dental clinic'; use mint on one plane (ceiling or cabinets) only. Dezeen blocks automated fetches; the Ignant and keijidesign pages are the verifiable mirrors.  
- Реализуемость в Blender: easy: array modifier for the drawer grid, flat mint material, white walls with a cloth curtain plane, soft area light; very CPU-friendly.

### Atrium Vårdcentral / Neko Health clinic, Stockholm (Note Design Studio)
- Тип: studio  
- Ссылка: https://www.onofficemagazine.com/?p=20876  
- Стиль: Scandinavian monochrome clinic with warm accents, oak benches and calming blue ceilings  
- Визуальные черты: Monochrome base with 'warm yet fresh' accent colours; examination rooms identical except blue ceilings, chosen because patients lie looking up; Clinical materials turned into design features: sturdy vinyl floor framing doorways as both decoration and a visual guide for impaired vision; Upholstered oak benches and dividers; Toogood Roly Poly chairs, Hem Lolly tables; Integrated lighting that reads as daylight throughout; Intent: 'redefine both the look and the general mood of a typical clinic' (Johannes Karlström); patients report it 'feels warm and welcoming'  
- Почему подходит: Directly usable tricks for ward/ICU scenes: a muted blue ceiling (~#B7D0E2) over a white room gives instant calm and a cool counterpoint to the warm strip; vinyl door frames double as wayfinding colour keys; oak + white + one accent is a safe base palette.  
- Риски: Monochrome bases can look flat in CPU renders without good AO; add a warm wood plane and a window.  
- Реализуемость в Blender: easy: ceiling material swap, door-frame inset with accent colour, oak bench boxes with bevels.

### Patient Room 2020 prototype (NXT Health with Clemson Architecture + Health, 2013)
- Тип: research-paper  
- Ссылка: https://metropolismag.com/projects/patient-room-2020-modern/  
- Стиль: seamless white Corian patient room, integrated headwall, overhead 'Patient Ribbon' with colour halo  
- Визуальные черты: Thermoformed white Corian walls and headwall, rubber floor, modular ceiling; rectilinear, no wood or pastel walls: 'unapologetically modern'; Headwall integrates gas outlets (flush), sharps, waste, supplies; overhead 'Patient Ribbon' canopy carries lighting, controls and a colour halo (Traxon LED pixelboards in a Barrisol light box); Footwall-embedded TV, tablet 'Patient Companion' overbed table with charging pad; colour used only as functional signal (red/green hand-wash light at caregiver sink); First impression: 'a remarkable lack of clutter'; 'without it being cold and sterile' (David Ruthven); Full-scale prototype built at DuPont Corian Design Studio NYC; origins in a DoD-funded Clemson project 2007-09  
- Почему подходит: Shows how to stage an ICU bay that reads as ICU with almost no props: one integrated headwall, one overhead light ribbon, one monitor. Fewer objects means the ECG monitor and the strip are the visual event. The colour-halo idea can become the monitor's alarm glow (green normal, amber/red emergency).  
- Риски: All-white Corian is the sterile look the author wants to avoid; combine with a warm floor and the blue-ceiling trick. Not ICU-specific in the source.  
- Реализуемость в Blender: easy-medium: box room with bevelled headwall, emission strip for the halo, screen plane with the SVG strip as an emissive texture; white materials need slightly grey albedo (~0.8) to avoid Cycles blow-out.

### Redesigning the Emergency Ambulance (Helen Hamlyn Centre for Design + Vehicle Design, Royal College of Art, 2011-12)
- Тип: research-paper  
- Ссылка: https://rca.ac.uk/research-innovation/projects/redesigning-ambulance  
- Стиль: patient-centred ambulance interior: central stretcher, single working wall, modular treatment packs  
- Визуальные черты: Stretcher centred for 360-degree access; all equipment and supplies on one ergonomic 'working wall' (Core77 Design Awards 2012 write-up); Smooth, easy-clean surfaces with no dirt-trapping corners; interior described as better lit, improved ambience, 'less intimidating' for patients; Standardised colour-coded modular treatment packs loaded per shift; coolbox, hand-cleaning station, staff storage; Digital Diagnostics and Communications system sends vital signs and handover to hospital en route (video link, records, navigation); Won Design Museum Designs of the Year 2012 transport award; partners: London Ambulance Service, Imperial College Healthcare NHS Trust, UWE  
- Почему подходит: The ambulance location needs to read instantly and cleanly: one wall of rounded white cabinets with coloured pack labels, central stretcher, one monitor/defib on a bracket. The vitals-transmission concept justifies showing a live ECG trace on the ambulance monitor as a gameplay device.  
- Риски: Original source gives no colours; the pack colours are a design choice. Vehicle interiors are curved and tight to light; use a large soft area light through the rear doors.  
- Реализуемость в Blender: medium: a bevelled box interior with a curved roof (subdivision + simple deform), array of cabinet fronts, stretcher as primitives, monitor as emissive plane; feasible procedurally.

### Wes Anderson framing and palette (The Grand Budapest Hotel, Asteroid City) as a staging rule
- Тип: art-reference  
- Ссылка: https://spotlightfx.com/blog/wes-anderson-color-palette  
- Стиль: dead-centre symmetry, frontal perpendicular camera, limited low-saturation pastel palette with one accent  
- Визуальные черты: Rule set: align doors, windows and props on a vertical axis; shoot frontal, perpendicular, subject centred; 'won't read as Anderson without the symmetry'; Each film uses one dominant colour, one supporting colour and a small accent; saturation held low so pastels stay soft and only deliberate spots pop; Illustrative hex (blog author's approximations, not sampled): Grand Budapest #FFBDD8 cotton-candy pink, #F4A8B9 soft rose, #A4D8FF pale sky blue, #F9D1BC peach, #8B5FBF muted purple; Asteroid City #F4D35E mustard, #A7C5EB dusty blue, #E6A8B5 muted pink, #DDD0C1 beige, #8BAF9F soft muted green; Flat, even, frontal lighting; shallow stage-like depth with layered planes  
- Почему подходит: A centred, symmetric frontal shot of a reception desk, ward bed or ICU bay gives the ECG strip a natural stage in the middle of the frame. The Grand Budapest pinks are the same hue family as ECG grid paper (#F4A8B9 vs grid ~#F2A6A6), so the environment can quote the strip's colour at lower saturation, and the Asteroid City muted green #8BAF9F is a ready complement for walls or scrubs.  
- Риски: Hex values are secondary approximations; sample your own. Over-symmetry can look like a film pastiche; use it for key 'reading the strip' scenes only.  
- Реализуемость в Blender: easy: camera on the room's centre axis with a 35-50 mm lens or orthographic, props mirrored via symmetry in bpy, one soft frontal area light plus sun; the cheapest high-impact look for Cycles CPU.

### Colour-in-healthcare evidence: CHER review (Tofle, Schwarz, Yoon, Max-Royale 2004), Dalke et al. 2006 'Colour and lighting in hospital design', Tabanejad 2024 systematic review; plus APSF note on monitor waveform colours (Venna 2013)
- Тип: research-paper  
- Ссылка: https://brieflands.com/articles/semj-146676  
- Стиль: evidence base: colour supports contrast, wayfinding and mood via light; no proven 'healing hues'  
- Визуальные черты: CHER 2004 (3000+ citations reviewed): no direct linkage between particular colours and health outcomes; existing healthcare colour guidelines not supported by research (summary at healthcaredesignmagazine.com/?p=592, report at brikbase.org/node/580); Dalke et al. 2006, Optics & Laser Technology 38(4-6):343-365, DOI 10.1016/j.optlastec.2005.06.040: NHS-funded guidance on colour contrast, colour design and mood; stresses contrast for wayfinding and the visually impaired, daylight, avoiding bland institutional schemes; Tabanejad 2024 (Shiraz E-Med J 25(12):e146676): six studies 2006-2022; light + colour jointly shape perceived support; contrast aids orientation; green shows only a tendency to reduce stress; evidence 'remains limited'; APSF (Ranga P. Venna, 10 Feb 2013): no standard for monitor waveform colours across industry; a fixed scheme (heart rate/ECG green, arterial pressure red) is useful for basic monitoring; ~10% of men have red-green deficiency, so colour must not be the only cue (https://www.apsf.org/article/colors-for-ecg-tracings-spo2-pulse-oximetry-on-patient-monitors-in-the-or-and-icu/); Exam-prep and stock imagery converge on the de facto convention: ECG green, SpO2 cyan/light blue, ABP red, CO2 yellow/white  
- Почему подходит: Licenses a pragmatic rule for the game: pick colours for readability, contrast and wayfinding (room identity), not for claimed therapeutic effect; and style monitors with the de facto green/cyan/red scheme so the ICU reads as authentic to clinicians while remaining a UI convention you can control.  
- Риски: Do not cite colour-psychology claims as evidence; keep redundant cues (icons, labels) for colour-deficient learners, which also matters for the pink grid on cream.  
- Реализуемость в Blender: n/a (guidance); monitor screens are trivial emissive planes (dark #0B1A1F, trace #33FF77 or #00E676, SpO2 #4DD0E1, ABP #FF5252) in bpy.

**Выводы агента:**

- The common recipe across every 'pleasant clinic' source (Maggie's Leeds, Aloop, Atrium Vårdcentral, Sumiyoshido, Two Point Hospital) is: warm white or cream base + light wood + one chromatic plane (mint/teal/blue ceiling or cabinets) + daylight. Everything else is desaturated. Suggested working palette that harmonises with pink grid paper and black ink: cream #F6F1E7, blonde spruce #E7CDA6, warm oak #C8975C, mint #BFE3D0, teal #3C8C86, ceiling blue #B7D0E2, coral accent #F08A7A (a low-saturation echo of the grid), sage #8BAF9F; ECG strip itself: paper #FFF8F0, 1 mm grid #F4A6A6, 5 mm grid #E8807F, trace #111111.
- Reserve the extremes for the strip: the environment should contain no pure black and no saturated pink-red other than the ECG paper; That Dragon, Cancer shows how reserving one colour for one meaning makes it the focal point automatically.
- Mint/teal is the natural complement to the pink grid; a mint plane (ceiling or cabinets, as in Sumiyoshido) makes the strip pop without a vignette or spotlight. Pure white walls should be slightly grey/cream (albedo ~0.8) so the cream paper still reads warm.
- Fewer, bigger props beat realism: Patient Room 2020 (integrated headwall, one light ribbon) and the RCA ambulance (one 'working wall', central stretcher) read as ICU/ambulance with 3-5 objects. Cardiology signifiers in silhouette: a wheeled ECG cart with a single screen and a cable bundle, a defibrillator with two paddles and an orange/red lid, electrode stickers, a bedside monitor with green trace. These are cheap primitives in bpy.
- Monitor aesthetic: there is no formal standard (APSF 2013), but green ECG, cyan SpO2, red arterial pressure, yellow CO2 on near-black is the de facto convention clinicians expect; use it on in-scene emissive screens and in the HTML UI, with text labels as a redundant cue for colour-deficient learners.
- Research says colour does not heal but contrast, wayfinding and light do (CHER 2004, Dalke 2006, Tabanejad 2024): colour-code each hospital location (as RCH Melbourne does per floor) at low saturation so players always know where they are, and spend effort on daylight and soft fill rather than on 'calming' hues.
- Rounded corners and bevels are the cheapest 'friendly' signal (Baymax vinyl, Aloop rounded furniture, Two Point chunky props): a bevel modifier with 2-3 segments and smooth shading on every box does most of the work in Cycles CPU renders.
- Wes Anderson staging (centred frontal camera, mirrored props, one dominant + one supporting + one accent colour) is the lowest-cost high-impact look for a procedural pipeline and naturally centres the ECG strip; use it for 'read the strip' key scenes and a looser three-quarter isometric for navigation scenes.
- Avoid sci-fi neon and heavy glow (Galacticare's space hospitals, Trauma Center's brown/red palette) because emissive environments compete with the trace; keep screen glow as the only emissive element and keep bloom off or minimal.
- Two Point Hospital's art director rule 'graphics support the game' translates to: every environment decision is tested by whether the strip remains the most legible thing on screen; render test frames with the SVG strip composited before approving a palette.
