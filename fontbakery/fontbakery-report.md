## Fontbakery report

Fontbakery version: 0.8.8

<details><summary><b>[9] KantumruyPro-ThinItalic.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'ANGT' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uni17D2179A.narrow.BRACKET.108
	- eight.dnom
	- seven.dnom
	- one.numr
	- zero.numr
	- eight.numr
	- acutecomb.asc
	- gravecomb.asc
	- six.dnom
	- nine.dnom 
	- And 17 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12 
	- And Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+17BE [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* exclam (U+0021): X=52.5,Y=2.0 (should be at baseline 0?)
	* parenleft (U+0028): X=87.0,Y=0.5 (should be at baseline 0?)
	* period (U+002E): X=44.5,Y=2.0 (should be at baseline 0?)
	* colon (U+003A): X=57.5,Y=2.0 (should be at baseline 0?)
	* question (U+003F): X=173.5,Y=2.0 (should be at baseline 0?)
	* at (U+0040): X=656.0,Y=2.0 (should be at baseline 0?)
	* cent (U+00A2): X=201.0,Y=-2.0 (should be at baseline 0?)
	* sterling (U+00A3): X=65.0,Y=-2.0 (should be at baseline 0?)
	* cedilla (U+00B8): X=280.0,Y=1.0 (should be at baseline 0?)
	* cedilla (U+00B8): X=280.0,Y=1.0 (should be at baseline 0?) and 43 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* M (U+004D): L<<201.0,637.0>--<190.0,582.0>> -> L<<190.0,582.0>--<55.0,0.0>>
	* M (U+004D): L<<213.0,660.0>--<315.0,50.0>> -> L<<315.0,50.0>--<319.0,17.0>>
	* M (U+004D): L<<319.0,17.0>--<337.0,47.0>> -> L<<337.0,47.0>--<724.0,660.0>>
	* M (U+004D): L<<577.0,0.0>--<712.0,582.0>> -> L<<712.0,582.0>--<726.0,637.0>>
	* N (U+004E): L<<203.0,644.0>--<191.0,587.0>> -> L<<191.0,587.0>--<55.0,0.0>>
	* N (U+004E): L<<213.0,660.0>--<476.0,56.0>> -> L<<476.0,56.0>--<493.0,16.0>>
	* N (U+004E): L<<483.0,0.0>--<220.0,604.0>> -> L<<220.0,604.0>--<203.0,644.0>>
	* N (U+004E): L<<493.0,16.0>--<505.0,73.0>> -> L<<505.0,73.0>--<641.0,660.0>>
	* Ntilde (U+00D1): L<<203.0,644.0>--<191.0,587.0>> -> L<<191.0,587.0>--<55.0,0.0>>
	* Ntilde (U+00D1): L<<213.0,660.0>--<476.0,56.0>> -> L<<476.0,56.0>--<493.0,16.0>> and 41 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:
	* B (U+0042): B<<487.0,360.5>-<450.0,335.0>-<400.0,330.0>>/B<<400.0,330.0>-<465.0,322.0>-<498.0,285.5>> = 12.72709488222251
	* G (U+0047): L<<525.0,0.0>--<559.0,142.0>>/B<<559.0,142.0>-<536.0,86.0>-<500.0,53.0>> = 8.863448283207358
	* OE (U+0152): B<<588.5,538.0>-<610.0,476.0>-<607.0,394.0>>/L<<607.0,394.0>--<668.0,660.0>> = 10.820682898678625
	* a (U+0061): B<<426.5,456.0>-<474.0,402.0>-<472.0,316.0>>/L<<472.0,316.0>--<515.0,500.0>> = 11.821488340607257
	* a (U+0061): L<<399.0,0.0>--<428.0,126.0>>/B<<428.0,126.0>-<402.0,69.0>-<355.0,29.5>> = 11.55824083719876
	* aacute (U+00E1): B<<426.5,456.0>-<474.0,402.0>-<472.0,316.0>>/L<<472.0,316.0>--<515.0,500.0>> = 11.821488340607257
	* aacute (U+00E1): L<<399.0,0.0>--<428.0,126.0>>/B<<428.0,126.0>-<402.0,69.0>-<355.0,29.5>> = 11.55824083719876
	* acircumflex (U+00E2): B<<426.5,456.0>-<474.0,402.0>-<472.0,316.0>>/L<<472.0,316.0>--<515.0,500.0>> = 11.821488340607257
	* acircumflex (U+00E2): L<<399.0,0.0>--<428.0,126.0>>/B<<428.0,126.0>-<402.0,69.0>-<355.0,29.5>> = 11.55824083719876
	* adieresis (U+00E4): B<<426.5,456.0>-<474.0,402.0>-<472.0,316.0>>/L<<472.0,316.0>--<515.0,500.0>> = 11.821488340607257 and 37 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[10] KantumruyPro-MediumItalic.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'ANGT' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* H
	* Oslash
	* uni17D2179E
	* uni17DB
	* uni179E17B6
	* uni17A217B6
	* uni178917C5
	* Euro
	* uni17A2
	* uni179E17B6.post_ and 47 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uni17D2179A.narrow.BRACKET.108
	- eight.dnom
	- seven.dnom
	- one.numr
	- zero.numr
	- eight.numr
	- acutecomb.asc
	- gravecomb.asc
	- six.dnom
	- nine.dnom 
	- And 17 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12 
	- And Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+17BE [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* dollar (U+0024): X=292.0,Y=1.0 (should be at baseline 0?)
	* comma (U+002C): X=97.0,Y=1.0 (should be at baseline 0?)
	* semicolon (U+003B): X=108.0,Y=1.0 (should be at baseline 0?)
	* Q (U+0051): X=267.0,Y=1.0 (should be at baseline 0?)
	* y (U+0079): X=151.0,Y=-2.0 (should be at baseline 0?)
	* uni00B5 (U+00B5): X=172.5,Y=-2.0 (should be at baseline 0?)
	* questiondown (U+00BF): X=-18.0,Y=2.0 (should be at baseline 0?)
	* Adieresis (U+00C4): X=582.0,Y=751.5 (should be at cap-height 750?)
	* Adieresis (U+00C4): X=378.0,Y=751.5 (should be at cap-height 750?)
	* Edieresis (U+00CB): X=588.0,Y=751.5 (should be at cap-height 750?) and 30 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* M (U+004D): L<<255.0,558.0>--<222.0,387.0>> -> L<<222.0,387.0>--<134.0,0.0>>
	* M (U+004D): L<<332.0,660.0>--<376.0,267.0>> -> L<<376.0,267.0>--<387.0,120.0>>
	* M (U+004D): L<<388.0,120.0>--<463.0,266.0>> -> L<<463.0,266.0>--<685.0,660.0>>
	* M (U+004D): L<<597.0,0.0>--<686.0,387.0>> -> L<<686.0,387.0>--<729.0,559.0>>
	* N (U+004E): L<<253.0,538.0>--<231.0,427.0>> -> L<<231.0,427.0>--<134.0,0.0>>
	* N (U+004E): L<<310.0,660.0>--<458.0,236.0>> -> L<<458.0,236.0>--<493.0,119.0>>
	* N (U+004E): L<<440.0,0.0>--<289.0,423.0>> -> L<<289.0,423.0>--<254.0,538.0>>
	* N (U+004E): L<<494.0,119.0>--<517.0,233.0>> -> L<<517.0,233.0>--<616.0,660.0>>
	* Ntilde (U+00D1): L<<253.0,538.0>--<231.0,427.0>> -> L<<231.0,427.0>--<134.0,0.0>>
	* Ntilde (U+00D1): L<<310.0,660.0>--<458.0,236.0>> -> L<<458.0,236.0>--<493.0,119.0>> and 37 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:
	* nine (U+0039): B<<423.5,217.5>-<446.0,279.0>-<453.0,350.0>>/B<<453.0,350.0>-<436.0,301.0>-<391.0,275.0>> = 13.502960448270217 and six (U+0036): B<<194.0,402.0>-<180.0,353.0>-<174.0,304.0>>/B<<174.0,304.0>-<193.0,354.0>-<241.0,381.5>> = 13.825733605881428 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[10] KantumruyPro-Medium.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'ANGT' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* H
	* Oslash
	* uni17D2179E
	* uni17DB
	* uni178C17C5
	* uni179E17B6
	* uni17A217B6
	* uni178917C5
	* K
	* Euro and 49 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uni17D2179A.narrow.BRACKET.108
	- eight.dnom
	- seven.dnom
	- one.numr
	- zero.numr
	- eight.numr
	- acutecomb.asc
	- gravecomb.asc
	- six.dnom
	- nine.dnom 
	- And 17 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12 
	- And Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+17BE [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* dollar (U+0024): X=348.0,Y=2.0 (should be at baseline 0?)
	* comma (U+002C): X=149.0,Y=-1.0 (should be at baseline 0?)
	* semicolon (U+003B): X=160.0,Y=-1.0 (should be at baseline 0?)
	* t (U+0074): X=337.0,Y=1.0 (should be at baseline 0?)
	* Adieresis (U+00C4): X=267.5,Y=750.5 (should be at cap-height 750?)
	* Adieresis (U+00C4): X=173.5,Y=750.5 (should be at cap-height 750?)
	* Adieresis (U+00C4): X=470.5,Y=750.5 (should be at cap-height 750?)
	* Adieresis (U+00C4): X=376.0,Y=750.5 (should be at cap-height 750?)
	* Edieresis (U+00CB): X=272.5,Y=750.5 (should be at cap-height 750?)
	* Edieresis (U+00CB): X=178.5,Y=750.5 (should be at cap-height 750?) and 34 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* M (U+004D): L<<187.0,562.0>--<194.0,387.0>> -> L<<194.0,387.0>--<194.0,0.0>>
	* M (U+004D): L<<254.0,660.0>--<387.0,266.0>> -> L<<387.0,266.0>--<428.0,121.0>>
	* M (U+004D): L<<430.0,121.0>--<471.0,265.0>> -> L<<471.0,265.0>--<603.0,660.0>>
	* M (U+004D): L<<660.0,0.0>--<660.0,387.0>> -> L<<660.0,387.0>--<667.0,562.0>>
	* N (U+004E): L<<190.0,532.0>--<193.0,427.0>> -> L<<193.0,427.0>--<193.0,0.0>>
	* N (U+004E): L<<220.0,660.0>--<469.0,237.0>> -> L<<469.0,237.0>--<527.0,128.0>>
	* N (U+004E): L<<497.0,0.0>--<248.0,423.0>> -> L<<248.0,423.0>--<191.0,532.0>>
	* N (U+004E): L<<528.0,128.0>--<524.0,233.0>> -> L<<524.0,233.0>--<524.0,660.0>>
	* Ntilde (U+00D1): L<<190.0,532.0>--<193.0,427.0>> -> L<<193.0,427.0>--<193.0,0.0>>
	* Ntilde (U+00D1): L<<220.0,660.0>--<469.0,237.0>> -> L<<469.0,237.0>--<527.0,128.0>> and 37 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
 * asterisk (U+002A): L<<246.0,602.0>--<245.0,730.0>> and asterisk (U+002A): L<<327.0,730.0>--<326.0,602.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[10] KantumruyPro-Bold.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'ANGT' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* H
	* uni179017B6
	* Oslash
	* uni17D2179D
	* uni179917C5.post2_
	* uni179117B6
	* uni178A17C5
	* uni179B17C5
	* uni17D2179E
	* uni2197 and 103 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uni17D2179A.narrow.BRACKET.108
	- eight.dnom
	- seven.dnom
	- one.numr
	- zero.numr
	- eight.numr
	- acutecomb.asc
	- gravecomb.asc
	- six.dnom
	- nine.dnom 
	- And 17 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12 
	- And Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+17BE [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* dollar (U+0024): X=269.0,Y=748.0 (should be at cap-height 750?)
	* dollar (U+0024): X=373.0,Y=748.0 (should be at cap-height 750?)
	* parenleft (U+0028): X=126.5,Y=1.5 (should be at baseline 0?)
	* parenright (U+0029): X=264.5,Y=2.0 (should be at baseline 0?)
	* comma (U+002C): X=161.0,Y=-1.0 (should be at baseline 0?)
	* comma (U+002C): X=156.0,Y=2.0 (should be at baseline 0?)
	* semicolon (U+003B): X=167.0,Y=-1.0 (should be at baseline 0?)
	* semicolon (U+003B): X=162.0,Y=2.0 (should be at baseline 0?)
	* g (U+0067): X=116.0,Y=2.0 (should be at baseline 0?)
	* t (U+0074): X=359.5,Y=0.5 (should be at baseline 0?) and 34 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* M (U+004D): L<<221.0,506.0>--<226.0,303.0>> -> L<<226.0,303.0>--<226.0,0.0>>
	* M (U+004D): L<<318.0,660.0>--<417.0,324.0>> -> L<<417.0,324.0>--<453.0,184.0>>
	* M (U+004D): L<<455.0,184.0>--<492.0,323.0>> -> L<<492.0,323.0>--<590.0,660.0>>
	* M (U+004D): L<<673.0,0.0>--<673.0,303.0>> -> L<<673.0,303.0>--<678.0,506.0>>
	* N (U+004E): L<<221.0,455.0>--<225.0,333.0>> -> L<<225.0,333.0>--<225.0,0.0>>
	* N (U+004E): L<<264.0,660.0>--<458.0,303.0>> -> L<<458.0,303.0>--<507.0,205.0>>
	* N (U+004E): L<<465.0,0.0>--<271.0,357.0>> -> L<<271.0,357.0>--<222.0,455.0>>
	* N (U+004E): L<<508.0,205.0>--<504.0,327.0>> -> L<<504.0,327.0>--<504.0,660.0>>
	* Ntilde (U+00D1): L<<221.0,455.0>--<225.0,333.0>> -> L<<225.0,333.0>--<225.0,0.0>>
	* Ntilde (U+00D1): L<<264.0,660.0>--<458.0,303.0>> -> L<<458.0,303.0>--<507.0,205.0>> and 37 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
 * question (U+003F): L<<209.0,214.0>--<210.0,366.0>> and questiondown (U+00BF): L<<386.0,287.0>--<385.0,135.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[10] KantumruyPro-BoldItalic.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'ANGT' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* H
	* uni179017B6
	* Oslash
	* uni17D2179D
	* uni179917C5.post2_
	* uni179117B6
	* uni178A17C5
	* registered
	* uni179B17C5
	* uni17D2179E and 103 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uni17D2179A.narrow.BRACKET.108
	- eight.dnom
	- seven.dnom
	- one.numr
	- zero.numr
	- eight.numr
	- acutecomb.asc
	- gravecomb.asc
	- six.dnom
	- nine.dnom 
	- And 17 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12 
	- And Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+17BE [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* dollar (U+0024): X=381.0,Y=748.0 (should be at cap-height 750?)
	* dollar (U+0024): X=485.0,Y=748.0 (should be at cap-height 750?)
	* dollar (U+0024): X=322.0,Y=-1.0 (should be at baseline 0?)
	* dollar (U+0024): X=312.0,Y=-1.0 (should be at baseline 0?)
	* comma (U+002C): X=107.0,Y=2.0 (should be at baseline 0?)
	* comma (U+002C): X=92.0,Y=-0.5 (should be at baseline 0?)
	* comma (U+002C): X=75.0,Y=-2.0 (should be at baseline 0?)
	* semicolon (U+003B): X=113.0,Y=2.0 (should be at baseline 0?)
	* semicolon (U+003B): X=98.0,Y=-0.5 (should be at baseline 0?)
	* semicolon (U+003B): X=81.0,Y=-2.0 (should be at baseline 0?) and 42 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* M (U+004D): L<<271.0,494.0>--<235.0,303.0>> -> L<<235.0,303.0>--<166.0,0.0>>
	* M (U+004D): L<<384.0,660.0>--<414.0,340.0>> -> L<<414.0,340.0>--<422.0,177.0>>
	* M (U+004D): L<<423.0,177.0>--<502.0,340.0>> -> L<<502.0,340.0>--<674.0,660.0>>
	* M (U+004D): L<<614.0,0.0>--<684.0,303.0>> -> L<<684.0,303.0>--<731.0,498.0>>
	* N (U+004E): L<<267.0,465.0>--<242.0,333.0>> -> L<<242.0,333.0>--<166.0,0.0>>
	* N (U+004E): L<<351.0,660.0>--<465.0,297.0>> -> L<<465.0,297.0>--<494.0,189.0>>
	* N (U+004E): L<<417.0,0.0>--<299.0,357.0>> -> L<<299.0,357.0>--<269.0,465.0>>
	* N (U+004E): L<<495.0,189.0>--<523.0,327.0>> -> L<<523.0,327.0>--<600.0,660.0>>
	* Ntilde (U+00D1): L<<267.0,465.0>--<242.0,333.0>> -> L<<242.0,333.0>--<166.0,0.0>>
	* Ntilde (U+00D1): L<<351.0,660.0>--<465.0,297.0>> -> L<<465.0,297.0>--<494.0,189.0>> and 36 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:
	* m (U+006D): B<<589.5,351.5>-<564.0,323.0>-<552.0,270.0>>/L<<552.0,270.0>--<552.0,271.0>> = 12.757532160876671 and m (U+006D): L<<552.0,270.0>--<552.0,271.0>>/L<<552.0,271.0>--<489.0,0.0>> = 13.087228423836661 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[10] KantumruyPro-LightItalic.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'ANGT' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* numbersign
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uni17D2179A.narrow.BRACKET.108
	- eight.dnom
	- seven.dnom
	- one.numr
	- zero.numr
	- eight.numr
	- acutecomb.asc
	- gravecomb.asc
	- six.dnom
	- nine.dnom 
	- And 17 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12 
	- And Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+17BE [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* dollar (U+0024): X=302.0,Y=1.0 (should be at baseline 0?)
	* dollar (U+0024): X=268.0,Y=2.0 (should be at baseline 0?)
	* parenleft (U+0028): X=132.5,Y=-1.0 (should be at baseline 0?)
	* comma (U+002C): X=81.0,Y=1.0 (should be at baseline 0?)
	* comma (U+002C): X=80.0,Y=2.0 (should be at baseline 0?)
	* semicolon (U+003B): X=94.0,Y=1.0 (should be at baseline 0?)
	* semicolon (U+003B): X=93.0,Y=2.0 (should be at baseline 0?)
	* at (U+0040): X=667.0,Y=-2.0 (should be at baseline 0?)
	* Q (U+0051): X=277.0,Y=-2.0 (should be at baseline 0?)
	* l (U+006C): X=186.0,Y=2.0 (should be at baseline 0?) and 69 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* M (U+004D): L<<232.0,607.0>--<207.0,478.0>> -> L<<207.0,478.0>--<98.0,0.0>>
	* M (U+004D): L<<277.0,660.0>--<343.0,175.0>> -> L<<343.0,175.0>--<353.0,67.0>>
	* M (U+004D): L<<353.0,67.0>--<411.0,173.0>> -> L<<411.0,173.0>--<700.0,660.0>>
	* M (U+004D): L<<584.0,0.0>--<694.0,478.0>> -> L<<694.0,478.0>--<727.0,607.0>>
	* N (U+004E): L<<233.0,599.0>--<215.0,511.0>> -> L<<215.0,511.0>--<98.0,0.0>>
	* N (U+004E): L<<265.0,660.0>--<460.0,159.0>> -> L<<460.0,159.0>--<492.0,61.0>>
	* N (U+004E): L<<462.0,0.0>--<265.0,503.0>> -> L<<265.0,503.0>--<234.0,599.0>>
	* N (U+004E): L<<493.0,61.0>--<511.0,149.0>> -> L<<511.0,149.0>--<630.0,660.0>>
	* Ntilde (U+00D1): L<<233.0,599.0>--<215.0,511.0>> -> L<<215.0,511.0>--<98.0,0.0>>
	* Ntilde (U+00D1): L<<265.0,660.0>--<460.0,159.0>> -> L<<460.0,159.0>--<492.0,61.0>> and 41 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:
	* B (U+0042): B<<546.0,391.5>-<506.0,341.0>-<439.0,328.0>>/L<<439.0,328.0>--<439.0,328.0>> = 10.980650010173553
	* d (U+0064): L<<392.0,0.0>--<414.0,105.0>>/B<<414.0,105.0>-<390.0,55.0>-<345.0,23.0>> = 13.807360518144613
	* nine (U+0039): B<<455.5,254.5>-<472.0,316.0>-<476.0,384.0>>/B<<476.0,384.0>-<460.0,322.0>-<409.0,288.5>> = 11.103833436636105
	* q (U+0071): L<<337.0,-210.0>--<409.0,98.0>>/B<<409.0,98.0>-<385.0,50.0>-<342.0,20.5>> = 13.407508437063171
	* six (U+0036): B<<149.5,403.0>-<132.0,342.0>-<127.0,277.0>>/B<<127.0,277.0>-<145.0,338.0>-<197.0,372.0>> = 12.041674166684633 and uni2079 (U+2079): B<<321.5,459.5>-<337.0,501.0>-<340.0,552.0>>/B<<340.0,552.0>-<330.0,520.0>-<301.0,502.0>> = 13.987563972831547 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[10] KantumruyPro-Italic.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'ANGT' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Oslash
	* Euro
	* numbersign
	* daggerdbl
	* currency
	* ampersand
	* uni17A217C5
	* emptyset and dollar
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uni17D2179A.narrow.BRACKET.108
	- eight.dnom
	- seven.dnom
	- one.numr
	- zero.numr
	- eight.numr
	- acutecomb.asc
	- gravecomb.asc
	- six.dnom
	- nine.dnom 
	- And 17 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12 
	- And Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+17BE [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* dollar (U+0024): X=309.0,Y=1.0 (should be at baseline 0?)
	* dollar (U+0024): X=281.0,Y=2.0 (should be at baseline 0?)
	* parenleft (U+0028): X=151.0,Y=-1.0 (should be at baseline 0?)
	* parenright (U+0029): X=79.0,Y=1.0 (should be at baseline 0?)
	* comma (U+002C): X=94.0,Y=-1.0 (should be at baseline 0?)
	* semicolon (U+003B): X=108.0,Y=-1.0 (should be at baseline 0?)
	* Q (U+0051): X=277.0,Y=-1.0 (should be at baseline 0?)
	* grave (U+0060): X=362.0,Y=748.0 (should be at cap-height 750?)
	* grave (U+0060): X=290.0,Y=748.0 (should be at cap-height 750?)
	* g (U+0067): X=450.0,Y=-1.0 (should be at baseline 0?) and 60 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* M (U+004D): L<<245.0,595.0>--<214.0,436.0>> -> L<<214.0,436.0>--<115.0,0.0>>
	* M (U+004D): L<<302.0,660.0>--<354.0,225.0>> -> L<<354.0,225.0>--<366.0,87.0>>
	* M (U+004D): L<<367.0,87.0>--<441.0,223.0>> -> L<<441.0,223.0>--<691.0,660.0>>
	* M (U+004D): L<<587.0,0.0>--<687.0,436.0>> -> L<<687.0,436.0>--<728.0,595.0>>
	* N (U+004E): L<<245.0,581.0>--<225.0,481.0>> -> L<<225.0,481.0>--<115.0,0.0>>
	* N (U+004E): L<<286.0,660.0>--<454.0,200.0>> -> L<<454.0,200.0>--<492.0,79.0>>
	* N (U+004E): L<<454.0,0.0>--<283.0,462.0>> -> L<<283.0,462.0>--<246.0,581.0>>
	* N (U+004E): L<<493.0,79.0>--<514.0,179.0>> -> L<<514.0,179.0>--<625.0,660.0>>
	* Ntilde (U+00D1): L<<245.0,581.0>--<225.0,481.0>> -> L<<225.0,481.0>--<115.0,0.0>>
	* Ntilde (U+00D1): L<<286.0,660.0>--<454.0,200.0>> -> L<<454.0,200.0>--<492.0,79.0>> and 34 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:
	* nine (U+0039): B<<456.0,251.0>-<472.0,307.0>-<477.0,368.0>>/B<<477.0,368.0>-<466.0,330.0>-<439.5,303.5>> = 11.45843894078077
	* q (U+0071): L<<331.0,-210.0>--<402.0,93.0>>/B<<402.0,93.0>-<378.0,46.0>-<336.0,19.0>> = 13.86278708578053
	* six (U+0036): B<<168.0,405.0>-<152.0,350.0>-<146.0,293.0>>/B<<146.0,293.0>-<163.0,350.0>-<214.5,381.0>> = 10.597974621122468 and uni2079 (U+2079): B<<318.5,461.0>-<333.0,499.0>-<337.0,543.0>>/B<<337.0,543.0>-<327.0,514.0>-<298.5,498.0>> = 13.831177129833868 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[11] KantumruyPro-ExtraLight.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'ANGT' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* multiply
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Kantumruy Pro ExtraLight' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uni17D2179A.narrow.BRACKET.108
	- eight.dnom
	- seven.dnom
	- one.numr
	- zero.numr
	- eight.numr
	- acutecomb.asc
	- gravecomb.asc
	- six.dnom
	- nine.dnom 
	- And 17 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12 
	- And Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+17BE [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* dollar (U+0024): X=275.0,Y=1.0 (should be at baseline 0?)
	* dollar (U+0024): X=306.0,Y=1.0 (should be at baseline 0?)
	* at (U+0040): X=657.0,Y=-1.0 (should be at baseline 0?)
	* a (U+0061): X=497.0,Y=1.0 (should be at baseline 0?)
	* a (U+0061): X=421.0,Y=0.5 (should be at baseline 0?)
	* h (U+0068): X=482.0,Y=1.0 (should be at baseline 0?)
	* h (U+0068): X=446.0,Y=1.0 (should be at baseline 0?)
	* m (U+006D): X=857.0,Y=1.0 (should be at baseline 0?)
	* m (U+006D): X=821.0,Y=1.0 (should be at baseline 0?)
	* t (U+0074): X=284.0,Y=1.5 (should be at baseline 0?) and 46 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* M (U+004D): L<<133.0,622.0>--<136.0,529.0>> -> L<<136.0,529.0>--<136.0,0.0>>
	* M (U+004D): L<<155.0,660.0>--<368.0,114.0>> -> L<<368.0,114.0>--<391.0,43.0>>
	* M (U+004D): L<<392.0,43.0>--<415.0,113.0>> -> L<<415.0,113.0>--<628.0,660.0>>
	* M (U+004D): L<<646.0,0.0>--<646.0,529.0>> -> L<<646.0,529.0>--<650.0,622.0>>
	* N (U+004E): L<<135.0,620.0>--<136.0,549.0>> -> L<<136.0,549.0>--<136.0,0.0>>
	* N (U+004E): L<<147.0,660.0>--<509.0,106.0>> -> L<<509.0,106.0>--<547.0,40.0>>
	* N (U+004E): L<<535.0,0.0>--<173.0,554.0>> -> L<<173.0,554.0>--<135.0,620.0>>
	* N (U+004E): L<<547.0,40.0>--<546.0,111.0>> -> L<<546.0,111.0>--<546.0,660.0>>
	* Ntilde (U+00D1): L<<135.0,620.0>--<136.0,549.0>> -> L<<136.0,549.0>--<136.0,0.0>>
	* Ntilde (U+00D1): L<<147.0,660.0>--<509.0,106.0>> -> L<<509.0,106.0>--<547.0,40.0>> and 48 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
 * G (U+0047): L<<566.0,0.0>--<565.0,133.0>>
 * u (U+0075): L<<435.0,0.0>--<434.0,115.0>>
 * uacute (U+00FA): L<<435.0,0.0>--<434.0,115.0>>
 * ucircumflex (U+00FB): L<<435.0,0.0>--<434.0,115.0>>
 * udieresis (U+00FC): L<<435.0,0.0>--<434.0,115.0>> and ugrave (U+00F9): L<<435.0,0.0>--<434.0,115.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[10] KantumruyPro-ExtraLightItalic.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'ANGT' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Kantumruy Pro ExtraLight' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uni17D2179A.narrow.BRACKET.108
	- eight.dnom
	- seven.dnom
	- one.numr
	- zero.numr
	- eight.numr
	- acutecomb.asc
	- gravecomb.asc
	- six.dnom
	- nine.dnom 
	- And 17 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12 
	- And Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+17BE [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* at (U+0040): X=116.5,Y=-1.5 (should be at baseline 0?)
	* g (U+0067): X=394.0,Y=-2.0 (should be at baseline 0?)
	* l (U+006C): X=163.0,Y=1.0 (should be at baseline 0?)
	* y (U+0079): X=158.0,Y=1.0 (should be at baseline 0?)
	* cent (U+00A2): X=201.0,Y=-1.0 (should be at baseline 0?)
	* cedilla (U+00B8): X=248.0,Y=2.0 (should be at baseline 0?)
	* cedilla (U+00B8): X=248.0,Y=2.0 (should be at baseline 0?)
	* Ccedilla (U+00C7): X=299.0,Y=2.0 (should be at baseline 0?)
	* Ccedilla (U+00C7): X=299.0,Y=2.0 (should be at baseline 0?)
	* Udieresis (U+00DC): X=498.0,Y=748.0 (should be at cap-height 750?) and 57 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* M (U+004D): L<<217.0,622.0>--<199.0,530.0>> -> L<<199.0,530.0>--<76.0,0.0>>
	* M (U+004D): L<<245.0,660.0>--<329.0,112.0>> -> L<<329.0,112.0>--<336.0,42.0>>
	* M (U+004D): L<<336.0,42.0>--<374.0,110.0>> -> L<<374.0,110.0>--<712.0,660.0>>
	* M (U+004D): L<<581.0,0.0>--<703.0,530.0>> -> L<<703.0,530.0>--<727.0,622.0>>
	* N (U+004E): L<<218.0,622.0>--<203.0,549.0>> -> L<<203.0,549.0>--<76.0,0.0>>
	* N (U+004E): L<<239.0,660.0>--<468.0,107.0>> -> L<<468.0,107.0>--<493.0,39.0>>
	* N (U+004E): L<<473.0,0.0>--<243.0,553.0>> -> L<<243.0,553.0>--<218.0,622.0>>
	* N (U+004E): L<<493.0,39.0>--<508.0,111.0>> -> L<<508.0,111.0>--<635.0,660.0>>
	* Ntilde (U+00D1): L<<218.0,622.0>--<203.0,549.0>> -> L<<203.0,549.0>--<76.0,0.0>>
	* Ntilde (U+00D1): L<<239.0,660.0>--<468.0,107.0>> -> L<<468.0,107.0>--<493.0,39.0>> and 44 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:
	* G (U+0047): L<<517.0,0.0>--<545.0,125.0>>/B<<545.0,125.0>-<513.0,53.0>-<455.5,22.0>> = 11.33665209567083
	* a (U+0061): L<<395.0,0.0>--<421.0,116.0>>/B<<421.0,116.0>-<395.0,62.0>-<349.0,26.5>> = 13.07659184553623
	* aacute (U+00E1): L<<395.0,0.0>--<421.0,116.0>>/B<<421.0,116.0>-<395.0,62.0>-<349.0,26.5>> = 13.07659184553623
	* acircumflex (U+00E2): L<<395.0,0.0>--<421.0,116.0>>/B<<421.0,116.0>-<395.0,62.0>-<349.0,26.5>> = 13.07659184553623
	* adieresis (U+00E4): L<<395.0,0.0>--<421.0,116.0>>/B<<421.0,116.0>-<395.0,62.0>-<349.0,26.5>> = 13.07659184553623
	* agrave (U+00E0): L<<395.0,0.0>--<421.0,116.0>>/B<<421.0,116.0>-<395.0,62.0>-<349.0,26.5>> = 13.07659184553623
	* aring (U+00E5): L<<395.0,0.0>--<421.0,116.0>>/B<<421.0,116.0>-<395.0,62.0>-<349.0,26.5>> = 13.07659184553623
	* atilde (U+00E3): L<<395.0,0.0>--<421.0,116.0>>/B<<421.0,116.0>-<395.0,62.0>-<349.0,26.5>> = 13.07659184553623
	* b (U+0062): L<<231.0,730.0>--<154.0,396.0>>/B<<154.0,396.0>-<181.0,449.0>-<230.0,479.0>> = 14.013750746845336
	* d (U+0064): B<<422.5,463.0>-<470.0,416.0>-<472.0,335.0>>/L<<472.0,335.0>--<562.0,730.0>> = 14.25003269780357 and 12 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[11] KantumruyPro-SemiBold.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'ANGT' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* H
	* uni179017B6
	* Oslash
	* uni179917C5.post2_
	* uni178A17C5
	* uni179B17C5
	* uni17D2179E
	* uni2197
	* uni17DB
	* uni178C17C5 and 84 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Kantumruy Pro SemiBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uni17D2179A.narrow.BRACKET.108
	- eight.dnom
	- seven.dnom
	- one.numr
	- zero.numr
	- eight.numr
	- acutecomb.asc
	- gravecomb.asc
	- six.dnom
	- nine.dnom 
	- And 17 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12 
	- And Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+17BE [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* dollar (U+0024): X=270.0,Y=752.0 (should be at cap-height 750?)
	* dollar (U+0024): X=360.0,Y=752.0 (should be at cap-height 750?)
	* comma (U+002C): X=157.0,Y=-2.0 (should be at baseline 0?)
	* comma (U+002C): X=152.0,Y=1.0 (should be at baseline 0?)
	* semicolon (U+003B): X=165.0,Y=-2.0 (should be at baseline 0?)
	* semicolon (U+003B): X=161.0,Y=1.0 (should be at baseline 0?)
	* f (U+0066): X=234.0,Y=549.0 (should be at x-height 550?)
	* t (U+0074): X=348.0,Y=0.5 (should be at baseline 0?)
	* plusminus (U+00B1): X=550.0,Y=1.0 (should be at baseline 0?)
	* plusminus (U+00B1): X=54.0,Y=1.0 (should be at baseline 0?) and 32 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* M (U+004D): L<<203.0,535.0>--<209.0,346.0>> -> L<<209.0,346.0>--<209.0,0.0>>
	* M (U+004D): L<<285.0,660.0>--<402.0,294.0>> -> L<<402.0,294.0>--<440.0,152.0>>
	* M (U+004D): L<<442.0,152.0>--<481.0,293.0>> -> L<<481.0,293.0>--<597.0,660.0>>
	* M (U+004D): L<<666.0,0.0>--<666.0,346.0>> -> L<<666.0,346.0>--<672.0,535.0>>
	* N (U+004E): L<<205.0,495.0>--<209.0,381.0>> -> L<<209.0,381.0>--<209.0,0.0>>
	* N (U+004E): L<<241.0,660.0>--<464.0,269.0>> -> L<<464.0,269.0>--<517.0,165.0>>
	* N (U+004E): L<<482.0,0.0>--<259.0,391.0>> -> L<<259.0,391.0>--<206.0,495.0>>
	* N (U+004E): L<<518.0,165.0>--<514.0,279.0>> -> L<<514.0,279.0>--<514.0,660.0>>
	* Ntilde (U+00D1): L<<205.0,495.0>--<209.0,381.0>> -> L<<209.0,381.0>--<209.0,0.0>>
	* Ntilde (U+00D1): L<<241.0,660.0>--<464.0,269.0>> -> L<<464.0,269.0>--<517.0,165.0>> and 36 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
 * question (U+003F): L<<210.0,210.0>--<211.0,361.0>> and questiondown (U+00BF): L<<359.0,291.0>--<358.0,140.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[10] KantumruyPro-SemiBoldItalic.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'ANGT' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* H
	* uni179017B6
	* Oslash
	* uni179917C5.post2_
	* uni178A17C5
	* uni179B17C5
	* uni17D2179E
	* uni17DB
	* uni178C17C5
	* uni179917C5 and 81 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Kantumruy Pro SemiBold' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uni17D2179A.narrow.BRACKET.108
	- eight.dnom
	- seven.dnom
	- one.numr
	- zero.numr
	- eight.numr
	- acutecomb.asc
	- gravecomb.asc
	- six.dnom
	- nine.dnom 
	- And 17 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12 
	- And Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+17BE [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* dollar (U+0024): X=385.0,Y=752.0 (should be at cap-height 750?)
	* dollar (U+0024): X=476.0,Y=752.0 (should be at cap-height 750?)
	* comma (U+002C): X=103.0,Y=1.0 (should be at baseline 0?)
	* semicolon (U+003B): X=111.0,Y=1.0 (should be at baseline 0?)
	* Q (U+0051): X=258.0,Y=2.0 (should be at baseline 0?)
	* f (U+0066): X=310.0,Y=549.0 (should be at x-height 550?)
	* section (U+00A7): X=346.5,Y=-1.5 (should be at baseline 0?)
	* plusminus (U+00B1): X=482.0,Y=1.0 (should be at baseline 0?)
	* plusminus (U+00B1): X=-4.0,Y=1.0 (should be at baseline 0?)
	* germandbls (U+00DF): X=264.5,Y=-1.0 (should be at baseline 0?) and 28 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* M (U+004D): L<<263.0,527.0>--<228.0,346.0>> -> L<<228.0,346.0>--<149.0,0.0>>
	* M (U+004D): L<<357.0,660.0>--<394.0,302.0>> -> L<<394.0,302.0>--<404.0,148.0>>
	* M (U+004D): L<<405.0,148.0>--<482.0,302.0>> -> L<<482.0,302.0>--<680.0,660.0>>
	* M (U+004D): L<<605.0,0.0>--<685.0,346.0>> -> L<<685.0,346.0>--<730.0,530.0>>
	* N (U+004E): L<<260.0,503.0>--<236.0,381.0>> -> L<<236.0,381.0>--<149.0,0.0>>
	* N (U+004E): L<<330.0,660.0>--<461.0,265.0>> -> L<<461.0,265.0>--<493.0,153.0>>
	* N (U+004E): L<<429.0,0.0>--<294.0,391.0>> -> L<<294.0,391.0>--<261.0,503.0>>
	* N (U+004E): L<<494.0,153.0>--<520.0,279.0>> -> L<<520.0,279.0>--<608.0,660.0>>
	* Ntilde (U+00D1): L<<260.0,503.0>--<236.0,381.0>> -> L<<236.0,381.0>--<149.0,0.0>>
	* Ntilde (U+00D1): L<<330.0,660.0>--<461.0,265.0>> -> L<<461.0,265.0>--<493.0,153.0>> and 37 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><br></div></details><details><summary><b>[9] KantumruyPro-Light.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'ANGT' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* numbersign
	* multiply and dollar
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uni17D2179A.narrow.BRACKET.108
	- eight.dnom
	- seven.dnom
	- one.numr
	- zero.numr
	- eight.numr
	- acutecomb.asc
	- gravecomb.asc
	- six.dnom
	- nine.dnom 
	- And 17 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12 
	- And Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+17BE [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* dollar (U+0024): X=273.0,Y=2.0 (should be at baseline 0?)
	* dollar (U+0024): X=321.0,Y=1.0 (should be at baseline 0?)
	* comma (U+002C): X=135.0,Y=-1.0 (should be at baseline 0?)
	* comma (U+002C): X=132.0,Y=1.0 (should be at baseline 0?)
	* semicolon (U+003B): X=148.0,Y=-1.0 (should be at baseline 0?)
	* semicolon (U+003B): X=145.0,Y=1.0 (should be at baseline 0?)
	* a (U+0061): X=507.0,Y=2.0 (should be at baseline 0?)
	* m (U+006D): X=853.0,Y=1.0 (should be at baseline 0?)
	* m (U+006D): X=797.0,Y=1.0 (should be at baseline 0?)
	* t (U+0074): X=306.0,Y=1.5 (should be at baseline 0?) and 60 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* M (U+004D): L<<152.0,607.0>--<158.0,477.0>> -> L<<158.0,477.0>--<158.0,0.0>>
	* M (U+004D): L<<189.0,660.0>--<369.0,180.0>> -> L<<369.0,180.0>--<403.0,66.0>>
	* M (U+004D): L<<405.0,66.0>--<440.0,179.0>> -> L<<440.0,179.0>--<619.0,660.0>>
	* M (U+004D): L<<649.0,0.0>--<649.0,477.0>> -> L<<649.0,477.0>--<655.0,607.0>>
	* N (U+004E): L<<155.0,595.0>--<158.0,511.0>> -> L<<158.0,511.0>--<158.0,0.0>>
	* N (U+004E): L<<174.0,660.0>--<491.0,158.0>> -> L<<491.0,158.0>--<542.0,64.0>>
	* N (U+004E): L<<524.0,0.0>--<207.0,503.0>> -> L<<207.0,503.0>--<156.0,595.0>>
	* N (U+004E): L<<543.0,64.0>--<540.0,149.0>> -> L<<540.0,149.0>--<540.0,660.0>>
	* Ntilde (U+00D1): L<<155.0,595.0>--<158.0,511.0>> -> L<<158.0,511.0>--<158.0,0.0>>
	* Ntilde (U+00D1): L<<174.0,660.0>--<491.0,158.0>> -> L<<491.0,158.0>--<542.0,64.0>> and 41 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><br></div></details><details><summary><b>[11] KantumruyPro-Thin.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'ANGT' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* multiply
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uni17D2179A.narrow.BRACKET.108
	- eight.dnom
	- seven.dnom
	- one.numr
	- zero.numr
	- eight.numr
	- acutecomb.asc
	- gravecomb.asc
	- six.dnom
	- nine.dnom 
	- And 17 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12 
	- And Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+17BE [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* comma (U+002C): X=68.0,Y=1.5 (should be at baseline 0?)
	* semicolon (U+003B): X=78.0,Y=1.5 (should be at baseline 0?)
	* at (U+0040): X=649.0,Y=2.0 (should be at baseline 0?)
	* a (U+0061): X=423.0,Y=-1.0 (should be at baseline 0?)
	* g (U+0067): X=396.5,Y=548.5 (should be at x-height 550?)
	* h (U+0068): X=467.0,Y=1.0 (should be at baseline 0?)
	* h (U+0068): X=451.0,Y=1.0 (should be at baseline 0?)
	* l (U+006C): X=199.0,Y=2.0 (should be at baseline 0?)
	* m (U+006D): X=861.0,Y=2.0 (should be at baseline 0?)
	* m (U+006D): X=845.0,Y=2.0 (should be at baseline 0?) and 45 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* M (U+004D): L<<114.0,637.0>--<115.0,580.0>> -> L<<115.0,580.0>--<115.0,0.0>>
	* M (U+004D): L<<120.0,660.0>--<367.0,48.0>> -> L<<367.0,48.0>--<379.0,19.0>>
	* M (U+004D): L<<379.0,19.0>--<391.0,47.0>> -> L<<391.0,47.0>--<638.0,660.0>>
	* M (U+004D): L<<643.0,0.0>--<643.0,580.0>> -> L<<643.0,580.0>--<644.0,637.0>>
	* N (U+004E): L<<114.0,644.0>--<115.0,587.0>> -> L<<115.0,587.0>--<115.0,0.0>>
	* N (U+004E): L<<121.0,660.0>--<527.0,55.0>> -> L<<527.0,55.0>--<552.0,16.0>>
	* N (U+004E): L<<545.0,0.0>--<139.0,605.0>> -> L<<139.0,605.0>--<114.0,644.0>>
	* N (U+004E): L<<552.0,16.0>--<551.0,73.0>> -> L<<551.0,73.0>--<551.0,660.0>>
	* Ntilde (U+00D1): L<<114.0,644.0>--<115.0,587.0>> -> L<<115.0,587.0>--<115.0,0.0>>
	* Ntilde (U+00D1): L<<121.0,660.0>--<527.0,55.0>> -> L<<527.0,55.0>--<552.0,16.0>> and 41 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:
	* OE (U+0152): B<<329.0,670.0>-<533.0,670.0>-<576.0,473.0>>/L<<576.0,473.0>--<576.0,660.0>> = 12.313063458989452
	* OE (U+0152): L<<576.0,0.0>--<576.0,187.0>>/B<<576.0,187.0>-<533.0,-10.0>-<329.0,-10.0>> = 12.313063458989452
	* at (U+0040): B<<565.5,426.0>-<609.0,376.0>-<608.0,289.0>>/L<<608.0,289.0>--<647.0,466.0>> = 11.767399687863861
	* b (U+0062): B<<169.0,33.0>-<116.0,76.0>-<101.0,152.0>>/L<<101.0,152.0>--<101.0,0.0>> = 11.164880177548593
	* b (U+0062): L<<101.0,730.0>--<101.0,349.0>>/B<<101.0,349.0>-<119.0,426.0>-<171.5,468.0>> = 13.157542740014811
	* d (U+0064): B<<388.5,467.5>-<440.0,425.0>-<456.0,349.0>>/L<<456.0,349.0>--<456.0,730.0>> = 11.888658039627968
	* d (U+0064): L<<456.0,0.0>--<456.0,152.0>>/B<<456.0,152.0>-<439.0,75.0>-<387.5,32.5>> = 12.449996507806594
	* eth (U+00F0): B<<397.5,445.0>-<450.0,405.0>-<468.0,337.0>>/B<<468.0,337.0>-<463.0,424.0>-<439.5,492.0>> = 11.53723729186378
	* n (U+006E): L<<101.0,500.0>--<101.0,367.0>>/B<<101.0,367.0>-<117.0,430.0>-<169.5,470.0>> = 14.250032697803595
	* ntilde (U+00F1): L<<101.0,500.0>--<101.0,367.0>>/B<<101.0,367.0>-<117.0,430.0>-<169.5,470.0>> = 14.250032697803595 and 7 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
 * uni17A7 (U+17A7): L<<444.0,0.0>--<443.0,120.0>>
 * uni17A8 (U+17A8): L<<444.0,0.0>--<443.0,120.0>>
 * uni17A9 (U+17A9): L<<384.0,0.0>--<383.0,120.0>>
 * uni17AA (U+17AA): L<<444.0,0.0>--<443.0,120.0>>
 * uni17B1 (U+17B1): L<<444.0,0.0>--<443.0,120.0>> and uni17B3 (U+17B3): L<<444.0,0.0>--<443.0,120.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[9] KantumruyPro-Regular.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'ANGT' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Oslash
	* Euro
	* numbersign
	* daggerdbl
	* currency
	* uni17A217C5
	* multiply
	* emptyset and dollar
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uni17D2179A.narrow.BRACKET.108
	- eight.dnom
	- seven.dnom
	- one.numr
	- zero.numr
	- eight.numr
	- acutecomb.asc
	- gravecomb.asc
	- six.dnom
	- nine.dnom 
	- And 17 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12 
	- And Glyph name: uni25CC	Contours detected: 13	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure no GSUB5/GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/gsub5_gpos7">com.google.fonts/check/gsub5_gpos7</a>)</summary><div>


* ⚠ **WARN** Font contains a GSUB5 lookup which is not processed by macOS [code: has-gsub5]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+17BE [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* dollar (U+0024): X=272.0,Y=2.0 (should be at baseline 0?)
	* dollar (U+0024): X=333.0,Y=2.0 (should be at baseline 0?)
	* comma (U+002C): X=145.0,Y=-2.0 (should be at baseline 0?)
	* semicolon (U+003B): X=159.0,Y=-2.0 (should be at baseline 0?)
	* at (U+0040): X=422.0,Y=1.0 (should be at baseline 0?)
	* grave (U+0060): X=254.0,Y=748.0 (should be at cap-height 750?)
	* grave (U+0060): X=176.0,Y=748.0 (should be at cap-height 750?)
	* g (U+0067): X=327.0,Y=-1.0 (should be at baseline 0?)
	* g (U+0067): X=182.0,Y=-1.0 (should be at baseline 0?)
	* t (U+0074): X=324.0,Y=1.5 (should be at baseline 0?) and 63 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* M (U+004D): L<<167.0,595.0>--<175.0,436.0>> -> L<<175.0,436.0>--<175.0,0.0>>
	* M (U+004D): L<<217.0,660.0>--<370.0,233.0>> -> L<<370.0,233.0>--<413.0,85.0>>
	* M (U+004D): L<<415.0,85.0>--<459.0,232.0>> -> L<<459.0,232.0>--<611.0,660.0>>
	* M (U+004D): L<<652.0,0.0>--<652.0,436.0>> -> L<<652.0,436.0>--<660.0,595.0>>
	* N (U+004E): L<<172.0,576.0>--<175.0,481.0>> -> L<<175.0,481.0>--<175.0,0.0>>
	* N (U+004E): L<<195.0,660.0>--<476.0,199.0>> -> L<<476.0,199.0>--<538.0,83.0>>
	* N (U+004E): L<<516.0,0.0>--<234.0,462.0>> -> L<<234.0,462.0>--<173.0,576.0>>
	* N (U+004E): L<<539.0,83.0>--<536.0,179.0>> -> L<<536.0,179.0>--<536.0,660.0>>
	* Ntilde (U+00D1): L<<172.0,576.0>--<175.0,481.0>> -> L<<175.0,481.0>--<175.0,0.0>>
	* Ntilde (U+00D1): L<<195.0,660.0>--<476.0,199.0>> -> L<<476.0,199.0>--<538.0,83.0>> and 37 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><br></div></details>
### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 0 | 140 | 1466 | 85 | 1251 | 0 |
| 0% | 0% | 5% | 50% | 3% | 43% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
