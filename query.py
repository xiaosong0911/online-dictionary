import requests
import json
import bs4

def getSuggestion(word):
    url = 'https://www.bing.com/qsonhs.aspx?type=json&q=%s&ds=bingdict' % (word,)
    content = requests.get(url).content.decode('utf-8')
    jo = json.loads(content)
    if 'Results' not in jo['AS']: return []
    suggests = jo['AS']['Results'][0]['Suggests']
    return [s['Txt'] for s in suggests]

def getEntry(word):
    url = "https://cn.bing.com/dict/search?q=%s" % (word,)
    html = requests.get(url).content.decode('utf-8')

    soup = bs4.BeautifulSoup(html, 'html.parser')
    word = soup.find(id='sb_form_q')['value']

    soup.find(id='b_header').extract()
    soup.find(class_='sidebar').extract()
    soup.find(id='b_footer').extract()
    soup.find('style').string = css

    return word, str(soup)

css = '''
.sw_ddbl:after,
.sw_ddbk:after,
.sw_ddw:after,
.sw_ddgy:after,
.sw_ddgn:after,
.sw_poi:after,
.sw_poia:after,
.sw_play:after,
.sw_playh:after,
.sw_playa:after,
.sw_playd:after,
.sw_playp:after,
.sw_st:after,
.sw_sth:after,
.sw_ste:after,
.sw_st2:after,
.sw_sth2:after,
.sw_plus:after,
.sw_minus:after,
.sw_tpcg:after,
.sw_tpcbl:after,
.sw_tpcw:after,
.sw_tpcbk:after,
.sw_arw:after,
.sw_arwh:after,
.sb_pagN:after,
.sb_pagP:after,
.sw_up:after,
.sw_down:after,
.b_expandToggle:after,
.sw_calc:after,
.sw_fbi:after,
.sw_twi:after,
.sw_fbarw:after,
.sw_fbtmb:after,
.sw_twr:after,
.sw_twrt:after,
.sw_twf:after,
.b_fLogo:after,
.b_cm:after,
.sw_rmore:after,
.sw_tpo:after,
.sw_tpoa:after,
.sw_tpoh:after,
.sw_lpoi:after,
.sw_skp:after {
    position: relative;
    content: url(/sa/simg/SharedSpriteDesktopTwoToneLogoTealSpy_0817.png)
}

.sw_ddbl,
.sw_ddbk,
.sw_ddw,
.sw_ddgy,
.sw_ddgn,
.sw_poi,
.sw_poia,
.sw_play,
.sw_playh,
.sw_playa,
.sw_playd,
.sw_playp,
.sw_st,
.sw_sth,
.sw_ste,
.sw_st2,
.sw_sth2,
.sw_plus,
.sw_minus,
.sw_tpcg,
.sw_tpcbl,
.sw_tpcw,
.sw_tpcbk,
.sw_arw,
.sw_arwh,
.sb_pagN,
.sb_pagP,
.sw_up,
.sw_down,
.b_expandToggle,
.sw_calc,
.sw_fbi,
.sw_twi,
.sw_fbarw,
.sw_fbtmb,
.sw_twr,
.sw_twrt,
.sw_twf,
.b_fLogo,
.b_cm,
.sw_rmore,
.sw_tpo,
.sw_tpoa,
.sw_tpoh,
.sw_lpoi,
.sw_skp {
    position: relative;
    display: inline-block;
    overflow: hidden;
    direction: ltr
}

.sw_tpcbk,
.sw_tpcg,
.b_expandToggle,
.b_fLogo {
    display: block
}

.sw_play,
.sw_playh,
.sw_playa,
.sw_playd,
.sw_playp,
.sw_skp,
.sw_fbi,
.sw_twi,
.sw_fbarw,
.sw_fbtmb {
    height: 16px;
    width: 16px
}

.sw_play:after {
    top: -22px;
    left: -315px
}

.sw_playh:after,
.sw_playa:after {
    top: -22px;
    left: -333px
}

.sw_playd:after {
    top: -22px;
    left: -351px
}

.sw_playp:after {
    top: -22px;
    left: -369px
}

.sw_skp:after {
    left: -645px;
    top: -18px
}

.sw_fbi:after {
    left: -297px;
    top: -22px
}

.sw_twi:after {
    left: -645px
}

.sw_fbarw:after {
    left: -169px;
    top: -32px
}

.sw_fbtmb:after {
    left: -151px;
    top: -22px
}

.sw_st,
.sw_sth,
.sw_ste,
.sw_st2,
.sw_sth2,
.sw_twf,
.sw_pifa,
.sw_pipp {
    height: 12px;
    width: 12px
}

.sw_st:after {
    left: -535px;
    top: -31px
}

.sw_st2:after {
    left: -563px;
    top: -31px
}

.sw_sth:after {
    left: -577px;
    top: -31px
}

.sw_sth2:after {
    left: -591px;
    top: -31px
}

.sw_ste:after {
    left: -549px;
    top: -31px
}

.sw_twf:after,
.sw_pipp:hover:after,
.sw_pipp:active:after,
.sw_pipp:focus:after {
    left: -507px;
    top: -18px
}

.sw_pipp:after {
    left: -493px;
    top: -18px
}

.sw_twf:hover:after,
.sw_twf:active:after,
.sw_twf:focus:after {
    left: -521px
}

.sw_pifa:after {
    left: -433px;
    top: -18px
}

.sw_pifa:hover:after,
.sw_pifa:active:after,
.sw_pifa:focus:after {
    left: -447px
}

.sw_arw,
.sw_arwh,
.ccmc:hover .sw_arwh,
.sw_pit,
.sw_twr {
    height: 11px;
    width: 14px
}

.sw_arw:after,
a:hover .sw_arwh.b_invert:after {
    left: -463px;
    top: -32px
}

.sw_arwh:after,
a:hover .sw_arw.b_invert:after,
.ccmc:active .sw_arwh:after {
    left: -447px;
    top: -32px
}

.sw_pit:after {
    left: -461px;
    top: -18px
}

.sw_pit:hover:after,
.sw_pit:active:after,
.sw_pit:focus:after {
    left: -477px
}

.sw_twr:after {
    left: -571px;
    top: -18px
}

.sw_twr:hover:after,
.sw_twr:active:after,
.sw_twr:focus:after {
    left: -587px
}

.sw_ddbl,
.sw_ddbk,
.sw_ddw,
.sw_ddgy,
.sw_ddgn {
    height: 4px;
    width: 7px
}

.sw_ddbl:after,
.sw_ddbk:after,
.sw_ddw:after,
.sw_ddgy:after {
    left: -266px;
    top: -32px
}

.sw_ddgn:after {
    left: -256px;
    top: -32px
}

.sw_tpcg,
.sw_tpcbl,
.sw_tpcw,
.sw_tpcbk {
    height: 10px;
    width: 10px
}

.sw_tpcg:after,
.sw_tpcbl:after,
.sw_tpcw:after,
.sw_tpcbk:after {
    left: -176px;
    top: -32px
}

.sw_tpcg:hover:after,
.sw_tpcg:active:after,
.sw_tpcg:focus:after,
.sw_tpcbl:after {
    left: -188px;
    top: -32px
}

.sw_plus {
    height: 8px;
    width: 8px
}

.sw_plus:after {
    left: -276px;
    top: -32px
}

.sw_plus:hover:after,
.sw_plus:active:after,
.sw_plus:focus:after {
    left: -286px;
    top: -32px
}

.sw_minus {
    height: 2px;
    width: 8px
}

.sw_minus:after {
    left: -256px;
    top: -38px
}

.sw_minus:hover:after,
.sw_minus:active:after,
.sw_minus:focus:after {
    left: -266px;
    top: -38px
}

.sb_pagP,
.sb_pagN {
    height: 30px;
    width: 30px
}

.sb_pagP:after {
    left: -233px
}

.sb_pagP:hover:after,
.sb_pagP:active:after,
.sb_pagP:focus:after {
    left: -265px
}

.sb_pagN:after {
    left: -169px
}

.sb_pagN:hover:after,
.sb_pagN:active:after,
.sb_pagN:focus:after {
    left: -201px
}

.sb_inactP:after,
.sb_inactP:hover:after {
    left: -781px
}

.b_expandToggle,
.sw_up,
.sw_down {
    height: 8px;
    width: 12px
}

.b_expandToggle:after,
.sw_up:after,
.sw_down:after {
    left: -228px;
    top: -32px
}

.b_active .b_expandToggle:after,
.sw_up:after {
    left: -200px
}

*:active>.b_active .b_expandToggle:after,
*:hover>.sw_up:after,
*:active>.sw_up:after,
*:focus>.sw_up:after {
    left: -214px
}

*:active>.b_expandToggle:after,
*:hover>.sw_down:after,
*:active>.sw_down:after,
*:focus>.sw_down:after {
    left: -242px
}

.b_icon,
.sw_poi,
.sw_poia {
    width: 20px;
    height: 20px;
    z-index: 0
}

.sw_poi:after,
.sw_poia:after {
    left: -297px;
    position: absolute;
    z-index: -1
}

.sw_poia:after {
    left: -319px
}

.b_fLogo {
    height: 16px;
    width: 81px
}

.b_fLogo:after {
    left: -402px
}

.b_cm {
    height: 10px;
    width: 12px
}

.b_cm:after {
    left: -433px;
    top: -32px
}

.sw_calc {
    height: 19px;
    width: 19px
}

.sw_calc:after {
    left: -363px
}

.sw_twrt {
    height: 10px;
    width: 16px
}

.sw_twrt:after {
    left: -535px;
    top: -18px
}

.sw_twrt:hover:after,
.sw_twrt:active:after,
.sw_twrt:focus:after {
    left: -553px;
    top: -18px
}

.sw_pil {
    height: 16px;
    width: 12px
}

.sw_pil:after {
    left: -405px;
    top: -18px
}

.sw_pil:hover:after,
.sw_pil:active:after,
.sw_pil:focus:after {
    left: -419px
}

.sw_tpo,
.sw_tpoh,
.sw_tpoa,
.sw_rmore {
    height: 12px;
    width: 8px;
    display: block
}

.sw_tpo:after,
.sw_tpoh:after,
.sw_tpoa:after {
    left: -131px;
    top: -25px
}

.exp_th .sw_tpoh:after {
    left: -141px
}

.exp_ta .sw_tpoh:after {
    left: -131px
}

.sw_rmore:after {
    left: -121px;
    top: -25px
}

.sw_lpoi {
    height: 16px;
    width: 10px
}

.sw_lpoi:after {
    left: -633px;
    top: -18px
}

html,
body #b_results .b_no {
    background-color: #fff
}

.b_footer {
    background-color: #ececec
}

#b_results>li a {
    color: #001ba0
}

#b_results>li a:visited {
    color: #600090
}

#b_results>li {
    background-color: #fff
}

#b_results>.b_ad,
#b_results>.b_adrnd {
    color: #666;
    background-color: #f9fcf7
}

#b_results>.b_ad a,
#b_results>.b_adrnd a {
    color: #001ba0
}

#b_results>.b_ad a:visited,
#b_results>.b_adrnd a:visited {
    color: #600090
}

#b_results>.b_pag {
    background-color: transparent
}

#b_results>.b_pag a:hover {
    background-color: #f4f4f4
}

#b_results>.b_pag .sb_pagS:hover {
    background-color: #f4f4f4
}

#b_results>.b_pag a.sb_pagP:hover,
#b_results>.b_pag a.sb_pagN:hover {
    background-color: inherit
}

#b_context .b_ans,
#b_context #wpc_ag {
    background-color: #fff
}

#b_context>li.b_ad,
#b_context>li.b_adrnd {
    color: #666;
    background-color: #fff
}

#b_context>li.b_ad a,
#b_context>li.b_adrnd a {
    color: #001ba0
}

#b_context>li.b_ad a:visited,
#b_context>li.b_adrnd a:visited {
    color: #600090
}

.ccmc {
    background-color: #ccc
}

.ccmc:active {
    background-color: #36b
}

#b_tween .b_selected,
div.b_dropdown .b_selected,
#b_tween a.ftrH.b_selected:hover {
    background: #e1e0df
}

#b_tween .b_toggle:hover,
#b_tween .ftrH:hover {
    background: #f2f2f2
}

.b_scroll {
    background: #999;
    border-color: #999
}

.b_scroll:hover {
    background: #4d4d4d
}

.b_dropdown {
    background-color: #fff;
    border-color: #e5e5e5
}

.ctxt,
.ctxtb,
.csel,
.sic,
.ccal .ccali {
    border: 1px solid #bbb
}

.ccal .ccali {
    background-color: #fff
}

.ctxtb {
    color: #ccc
}

a,
#b_tween a:visited,
#b_results .b_no a,
#sw_footL>li a#sb_feedback {
    color: #001ba0
}

a:visited,
#b_results>li a:visited,
#sb_feedback:visited {
    color: #600090
}

cite,
#b_results cite.sb_crmb a,
#b_results cite a.sb_metalink,
#bk_wr_container cite a {
    color: #006d21
}

.b_posText {
    color: #006d21
}

.b_negText {
    color: #c80000
}

#b_context cite,
#b_context cite a,
.b_expando cite,
.b_expando cite a {
    color: #006d21
}

#b_context .b_posText,
.b_expando .b_posText {
    color: #006d21
}

#b_context .b_negText,
.b_expando .b_negText {
    color: #c80000
}

.b_ad cite,
.b_adrnd cite {
    color: #006d21
}

#b_context .b_entityTitle,
#b_results .b_entityTitle {
    color: #444
}

#b_context .b_entitySubTitle,
#b_results .b_entitySubTitle {
    color: #767676
}

#b_context,
#b_context #wpc_eif,
#b_context .b_defaultText {
    color: #666
}

body,
.b_promoteText,
#b_tween a.ftrH,
#b_tween a.ftrH:hover,
.b_expando,
.b_expando h2,
.b_expando h3,
.b_expando h4,
.b_expando .b_defaultText,
.b_active a,
.b_active a:visited,
.b_active a:hover,
#b_results>.b_pag a,
#b_results .b_no,
#b_content a.cbl:visited,
#b_content a.cbl {
    color: #666
}

#b_results>.b_pag .sb_pagS {
    color: #666
}

#b_results,
#b_results .b_defaultText,
#b_results>.b_pag a:hover,
#b_tween .b_selected,
#b_tween a.ftrH.b_selected,
#b_tween a.ftrH.b_selected:hover,
#b_tween .b_toggle:hover,
#b_tween .b_highlighted,
#hlcchcxmn label {
    color: #666
}

.b_top,
.b_top .b_promoteText {
    color: #444
}

.b_alert,
.sb_alert,
.b_pAlt,
#b_results .b_no .b_alert,
#b_results .b_no .sb_alert,
#b_results .b_no .b_pAlt {
    color: #d90026
}

#b_results .b_alert,
#b_results .sb_alert,
#b_results .b_pAlt {
    color: #d90026
}

#b_context .b_alert,
#b_context .sb_alert,
#b_context .b_pAlt {
    color: #d90026
}

.b_demoteText,
.b_secondaryText,
.b_attribution,
.b_factrow,
.b_focusLabel,
.b_footnote,
.b_ad .b_adlabel,
.b_adrnd .b_adlabel,
#b_tween .b_dropdown a,
.b_expando .b_subModule,
.b_expando .b_suppModule,
.b_algo .b_vList td {
    color: #767676
}

.b_algo .b_factrow {
    color: #666
}

.b_footer {
    color: #666
}

.b_footer a,
.b_footer a:visited,
.b_footer span {
    color: #666
}

#sb_feedback {
    color: #666
}

#b_content .b_lowFocusLink a,
#b_context .b_secondaryText,
#b_context .b_attribution,
#b_context .b_factrow,
#b_context .b_footnote,
#b_context .b_ad .b_adlabel,
#b_context .b_adrnd .b_adlabel,
.b_expando .b_secondaryText,
.b_expando .b_attribution,
.b_expando .b_factrow,
.b_expando .b_footnote,
#b_tween .b_nonselectable {
    color: #767676
}

#b_context .b_pointer.b_mhdr:hover .b_secondaryText {
    color: #36b
}

.b_button:hover,
.b_button:visited,
.b_hlButton,
.b_hlButton:hover,
.b_hlButton:visited,
.b_foregroundText,
.ciot {
    color: #fff
}

.ciot {
    background-color: #000
}

.b_button:hover,
.b_hlButton {
    background-color: #0072c5
}

.b_button:active,
.b_hlButton:active {
    background-color: #333
}

.b_hlButton:hover {
    background-color: #006887
}

.b_border,
.b_button,
.b_hlButton {
    border-color: #ccc
}

.b_pag a {
    border: 3px solid transparent;
    border-bottom: 3px solid transparent
}

.b_pag .sb_pagS {
    border-color: #ededed
}

#b_context .b_subModule,
#b_results .b_subModule,
.overlay-container .b_subModule {
    border-bottom: 1px solid #ebebeb
}

#b_context .b_subModule:last-child,
#b_results .b_subModule:last-child .overlay-container .b_subModule:last-child {
    border-bottom: 0
}

.c_tlbx,
.c_tlbxIS {
    border-color: #999;
    background: #fff
}

.sw_poi {
    color: #fff
}

.sw_poia {
    color: #fff
}

.sc_errorArea>.sc_error,
.sc_errorArea>.sc_error h1,
.sc_errorArea>.sc_error h3 {
    color: #666
}

.sc_errorArea font[color=red] {
    color: #d90026 !important
}

html,
body,
h1,
h2,
h3,
h4,
h5,
h6,
p,
img,
ol,
ul,
li,
form,
table,
tr,
th,
td,
blockquote {
    border: 0;
    border-collapse: collapse;
    border-spacing: 0;
    list-style: none;
    margin: 0;
    padding: 0
}

html {
    overflow-y: scroll
}

#b_content {
    clear: both;
    min-height: 344px;
    padding: 13px 0 20px 10px
}

#b_pole {
    margin: 3px 0 15px -100px;
    padding-left: 12px
}

#b_context {
    margin: 0 0 0 40px;
    padding: 0 20px
}

#b_context .b_ans,
.b_expando .b_ans,
#b_context .b_ad,
#b_context .b_adrnd,
.b_card {
    margin: 0 -20px
}

#b_context .b_ans,
.b_expando .b_ans {
    padding: 10px 20px 0
}

#b_context .b_ad,
#b_context .b_adrnd {
    padding: 10px 20px
}

.b_card {
    padding: 15px 20px
}

#b_results,
#b_context {
    margin-top: 28px
}

#b_tween~#b_results,
#b_tween~#b_context,
#b_tween~.b_twoColOnly #b_context,
#b_pole~#b_results,
#b_pole~#b_context,
#b_results:only-child {
    margin-top: 0
}

#b_results,
#b_context,
#b_tween>span,
.b_hList>li,
.c_tlbxTrg,
.b_hPanel>span,
.ccal .ccali,
.b_footerRight,
.b_hPanel .b_xlText,
.b_hPanel .cico,
.b_moreLink,
.b_label+.b_hList,
.lc_bks,
.lc_bkl,
.fiw,
.csrc,
.b_footnote .cico,
.b_algo .b_title H2,
.b_algo .b_title div,
h3 {
    display: inline-block
}

.b_pointer {
    cursor: pointer
}

label,
.b_ad .b_adlabel,
.b_adrnd .b_adlabel,
.c_tlbxTrgIcn {
    display: block
}

#b_tween {
    margin-top: 0
}

.b_underSearchbox~#b_tween {
    margin-top: -2px
}

#b_tween,
#b_tween .ftrH {
    height: 30px
}

#b_tween>span {
    padding-right: 25px
}

#b_results>li {
    padding: 10px 20px;
    margin: 0 0 2px
}

#b_results>.b_ans {
    padding: 17px 20px 0
}

#b_results>.b_algo {
    padding: 12px 20px 0
}

#b_results>li .b_fullb {
    margin-left: -20px;
    margin-right: -20px
}

#b_results>.b_ad,
#b_results>.b_adrnd {
    padding-right: 18px;
    border-right: 2px solid #e5e5e5
}

#b_results>li:first-child {
    padding-top: 10px
}

#b_results>.b_pag {
    padding: 18px 0 40px 20px
}

#b_results>.si_pp,
.sb_hbop,
.b_hide,
.ttl,
#sw_tfbb,
.sw_next,
.sw_prev,
#id_d,
.b_hidden img {
    display: none
}

.b_hidden {
    visibility: hidden
}

#b_context .b_ans,
.b_expando .b_ans {
    margin-bottom: 5px
}

#b_context .b_ad,
#b_context .b_adrnd {
    margin-bottom: 5px
}

.b_inlineList li,
.b_inlineList div,
.b_factrow li {
    display: inline
}

.b_footerRight,
td,
th,
#b_context,
.b_hList>li {
    vertical-align: top
}

.b_footer {
    width: 100%;
    padding: 12px 0
}

.c_tlbxTrg {
    width: 15px;
    height: 14px;
    margin: -1px 6px -3px 2px
}

.c_tlbxTrgIcn {
    margin: 4px 0 2px 3px
}

.c_tlbx {
    position: absolute;
    z-index: 6;
    border: 1px solid;
    padding: 10px
}

.c_tlbxIS {
    border-bottom: 1px solid
}

.b_deep ul {
    width: 230px
}

#b_results .b_gridList ul {
    width: 250px
}

.b_gridList ul:first-child,
.b_vlist2col ul:first-child {
    margin: 0 20px 0 0
}

.b_gridList li,
.b_vlist2col li {
    padding: 0 0 10px
}

.b_vlist2col.b_deep li {
    padding: 0 0 10px
}

.b_overhangR .b_vlist2col ul:first-child {
    margin: 0 15px 0 0
}

.b_overhangR .b_vlist2col ul {
    width: 180px
}

.b_deep p {
    height: 33px
}

#b_context .b_ad .b_adlabel,
#b_context .b_adrnd .b_adlabel,
#b_content .b_expanderControl .sw_plus,
.sc_rf form,
form.sc_rf,
.b_lBMargin {
    margin-bottom: 10px
}

.b_ad li,
.b_adrnd li,
#b_results .b_ad .b_adlabel,
#b_results .b_adrnd .b_adlabel {
    margin-bottom: 8px
}

.b_ad li:last-child,
.b_adrnd li:last-child {
    margin-bottom: 0
}

.b_ad li li,
.b_adrnd li li,
.b_ad li li:last-child,
.b_adrnd li li:last-child {
    margin: 0
}

#b_results .b_ad .b_vlist2col,
#b_results .b_adrnd .b_vlist2col,
#b_results .b_ad .b_factrow,
#b_results .b_adrnd .b_factrow {
    margin-top: -6px
}

#b_results .b_ad .sb_adRA .b_vlist2col,
#b_results .b_adrnd .sb_adRA .b_vlist2col {
    padding-left: 0
}

.sx_ci {
    border: 1px solid #e5e5e5;
    margin-top: 3px;
    width: 80px;
    height: 60px
}

.b_favicon {
    margin: 0 .5em 0 0
}

.b_imagePair:after,
.b_vlist2col:after,
.b_gridList:after {
    clear: left
}

.b_imagePair.reverse:after,
.b_overhangR:after {
    clear: right
}

.b_clear,
#b_results>li:after,
.b_clearfix:after {
    clear: both
}

#b_results>li:after,
.b_clearfix:after,
.b_imagePair:after,
.b_vlist2col:after,
.b_gridList:after,
.b_overhangR:after {
    content: '.';
    display: block;
    height: 0;
    visibility: hidden
}

.b_vlist2col ul,
.b_gridList ul,
.b_float,
.b_footer,
.b_float_img,
.b_pag li,
.b_mhdr h2 {
    float: left
}

.b_floatR_img,
.b_floatR,
.wr_tc {
    float: right
}

.b_overflow,
.b_hList li,
.b_1linetrunc,
.b_deep p,
.b_imageOverlayWrapper {
    overflow: hidden
}

.b_ansImage {
    padding: 2px 10px 0 0
}

.b_creditedImg img,
.b_creditedImg .cico {
    padding-bottom: 1px
}

h4,
.sa_uc>.b_vList>li>table td,
.b_smBottom,
#b_context .b_ad h2,
#b_context .b_adrnd h2,
.b_attribution,
.b_secondaryFocus,
.b_focusTextLarge,
.b_focusTextMedium,
.b_focusTextSmall,
.b_focusTextExtraSmall,
.b_snippet {
    padding-bottom: 2px
}

.b_factrow {
    padding-bottom: 2px
}

h2,
.b_focusLabel,
label {
    padding-bottom: 3px
}

.b_vPanel .b_vPanel>div,
.b_vList .b_vPanel>div {
    padding-bottom: 5px
}

.b_dataList li,
.b_mBottom {
    padding-bottom: 5px
}

.b_lBottom,
#b_results #sp_recourse.b_lBottom,
.b_caption,
.b_moreLink,
.b_footnote,
.b_hList>li,
#b_context h2,
#b_results .b_subModule h2,
#b_results .b_ad .b_factrow,
#b_results .b_adrnd .b_factrow,
.overlay-container .b_subModule h2,
.b_expando h2,
.b_no h1,
.b_no h4,
.b_no li,
.b_prominentFocusLabel,
.ht_module,
.b_locStr,
.b_entitySubTitle {
    padding-bottom: 10px
}

.b_vPanel>div,
.b_vList>li {
    padding-bottom: 10px
}

#b_results .b_ans>.b_factrow:last-child {
    padding-bottom: 10px
}

.b_vList .b_hList>li,
.b_vPanel .b_hList>li,
#b_content .ht_module h2,
.b_vList .b_float_img,
.b_creditedImg .b_footnote,
.b_creditedImg .cico img,
#b_results>.b_ad,
#b_results>.b_adrnd,
.b_suppModule .b_mhdr,
.b_vList>li>.tab-container,
.b_vPanel>div>.tab-container,
.b_ad .b_deep h3,
.b_adrnd .b_deep h3,
#b_content .b_float_img_nbp {
    padding-bottom: 0
}

.b_caption .b_factrow:last-child,
#b_results .b_caption .b_factrow:last-child,
.b_caption>.b_dataList:last-child li:last-child,
.b_caption .b_moreLink:last-child,
.b_vList .b_moreLink:last-child,
.b_vList .b_factrow:last-child,
.b_hList .b_factrow:last-child,
.b_vPanel .b_factrow:last-child,
.b_caption .b_attribution:last-child,
.b_vList .b_attribution:last-child,
.b_hList .b_attribution:last-child,
.b_vPanel .b_attribution:last-child,
.b_vList>li>table:last-child tr:last-child td,
.b_vPanel>div>table:last-child tr:last-child td,
.b_vList .b_focusLabel:last-child,
.b_vPanel .b_focusLabel:last-child,
.b_vList .b_prominentFocusLabel:last-child,
.b_vPanel .b_prominentFocusLabel:last-child,
.b_vList .b_secondaryFocus:last-child,
.b_vPanel .b_secondaryFocus:last-child,
.b_vList .b_focusTextExtraSmall:last-child,
.b_vPanel .b_focusTextExtraSmall:last-child,
.b_vList .b_focusTextSmall:last-child,
.b_vPanel .b_focusTextSmall:last-child,
.b_vList .b_focusTextMedium:last-child,
.b_vPanel .b_focusTextMedium:last-child,
.b_vList .b_focusTextLarge:last-child,
.b_vPanel .b_focusTextLarge:last-child,
.b_vList h4:last-child,
.b_vPanel h4:last-child,
.b_vPanel .b_caption:last-child,
.b_vPanel .b_vList:last-child>li:last-child,
.b_vPanel .b_footnote:last-child {
    padding-bottom: 0
}

.b_vList .b_vPanel,
.b_vPanel .b_vPanel {
    margin-bottom: -5px
}

.b_hList .b_vList,
.b_hList .b_vPanel {
    margin-bottom: -10px
}

.ht_module .sc_rf form.lc_bk,
.b_mBMargin,
.wpcbcc {
    margin-bottom: 5px
}

#b_results .b_no {
    margin: 0 0 80px
}

.b_rich {
    padding-top: 3px
}

h2+.b_rich {
    padding-top: 2px
}

.b_algo .b_attribution img {
    vertical-align: text-bottom
}

.b_smLeft {
    padding-left: 2px
}

.b_lLeft,
.b_floatR_img,
.b_suffix,
.b_footnote .cico {
    padding-left: 10px
}

.wr_tc,
.b_xlLeft,
.b_deep,
#b_results .b_ad .b_vlist2col,
#b_results .b_adrnd .b_vlist2col,
#b_tween {
    padding-left: 20px
}

h2 .b_secondaryText {
    margin-left: 5px
}

.b_hList.b_imgStrip>li {
    padding-right: 1px
}

.b_smRight {
    padding-right: 2px
}

.fiw,
.lc_bkl,
.b_mRight,
.b_label,
.csrc {
    padding-right: 5px
}

.b_lRight,
.b_imgStrip .imgData,
.b_underSearchbox .b_label {
    padding-right: 10px
}

.b_hPanel>span,
.b_hList>li {
    padding-right: 10px
}

.b_hPanel.wide>span,
.b_xlRight {
    padding-right: 20px
}

.b_hList.b_imgStrip>li:last-child,
.b_hList>li:last-child,
.b_hPanel>span:last-child,
td:last-child,
th:last-child,
#b_tween>span:last-child {
    padding-right: 0
}

.b_twoColumn>div:first-child {
    padding-right: 30px
}

.b_overhangR {
    margin-right: -30px;
    padding-right: 15px
}

.wr_tc {
    margin-right: -150px
}

.wr_et {
    margin-right: -120px
}

.b_tbl {
    margin-right: -10px
}

.b_border,
.b_button,
.b_hlButton,
.b_scroll,
.b_dropdown {
    border-width: 1px;
    border-style: solid
}

.b_button,
.b_hlButton {
    line-height: 30px;
    text-decoration: none;
    text-align: center;
    cursor: pointer;
    padding: 0 15px;
    min-width: 50px
}

.lc_bks .cbtn {
    margin-top: 15px
}

#b_context .b_subModule,
#b_results .b_subModule,
.b_expando .b_subModule,
.overlay-container .b_subModule {
    padding-bottom: 0;
    margin-bottom: 10px
}

#b_context .b_subModule:last-child,
#b_results .b_subModule:last-child,
.b_subModule .b_subModule:last-child {
    margin-bottom: 0
}

.b_dropdown {
    position: absolute;
    z-index: 6
}

.b_scroll {
    position: relative;
    top: 0;
    width: 5px;
    height: 20px
}

.b_pag a {
    display: block;
    min-width: 34px;
    margin-right: 10px;
    text-align: center;
    height: 34px;
    line-height: 34px
}

.b_pag .b_widePag {
    margin-right: 28px
}

.b_pag a.sb_pagN,
.b_pag a.sb_pagP {
    min-width: 0;
    height: 30px;
    width: 30px;
    border: 0;
    margin-top: 5px
}

.b_pag a.b_roths {
    transform: rotate(180deg);
    -webkit-transform: rotate(180deg);
    -moz-transform: rotate(180deg);
    -ms-transform: rotate(180deg);
    -o-transform: rotate(180deg)
}

.b_pag .sw_prev,
.b_pag .sw_next {
    margin: 2px
}

.b_mhdr {
    margin: -15px 0 -5px;
    padding: 15px 0 5px
}

.b_mhdr .sw_up,
.b_mhdr .sw_down {
    margin-top: 10px
}

.b_mhdr .b_moreLink,
.b_mhdr .b_secondaryText {
    margin-top: 8px
}

.b_vPanel .sc_rf form,
.b_suppModule .b_mhdr {
    margin-bottom: 0
}

.b_rTxt {
    text-align: right
}

.b_cTxt {
    text-align: center
}

.b_jTxt {
    text-align: justify
}

table {
    width: 100%;
    word-wrap: break-word
}

td,
th,
.b_float_img {
    padding: 0 10px 10px 0
}

th {
    text-align: left
}

.sw_poi,
.sw_poia {
    float: left;
    margin: -3px 5px 0 0;
    line-height: 20px;
    text-align: center
}

.ctxt,
.ctxtb {
    padding: 5px 15px;
    height: 20px
}

.ctxt.b_focusTextMedium,
.ctxtb.b_focusTextMedium {
    height: 58px
}

input.ctxt,
input.ctxtb,
.ccal input,
.ccal .ccali,
.b_favicon,
.b_footnote .cico {
    vertical-align: middle
}

.ccal .ccali {
    height: 30px;
    border-left: 0
}

.ccal .ccalp {
    padding: 5px 5px 0 5px
}

form.b_externalSearch {
    margin: 0 20px 10px
}

.b_externalSearch input {
    outline: none;
    padding: 0
}

.ccal .ctxt {
    border-right: 0
}

.b_underSearchbox {
    margin: -7px 20px 14px
}

.b_underSearchbox .b_hList>li {
    padding: 0 8px 0 0
}

.b_compactSearch label {
    float: left;
    margin: 7px 10px 0 0
}

.b_compactSearch input {
    margin-right: 0;
    float: left
}

.b_compactSearch .cbtn {
    border-left: 0
}

.b_footer table {
    width: 520px;
    margin: 15px 20px 0 120px
}

#b_footerItems ul {
    display: block
}

#b_footerItems li {
    display: inline;
    float: left
}

#b_footerItems span {
    margin-right: 24px;
    margin-left: 48px;
    float: right
}

#b_footerItems a {
    margin-right: 24px
}

#b_footerItems {
    height: 24px;
    line-height: 24px;
    padding: 0 20px
}

.b_footerRight {
    margin: 13px 0 0 50px
}

.b_1linetrunc {
    text-overflow: ellipsis;
    white-space: nowrap
}

div.cico.b_capImg {
    padding-bottom: 4px
}

.b_imageOverlayWrapper {
    margin: -20px 0 0;
    height: 20px
}

.b_imageOverlay {
    color: #fff;
    background-color: #000;
    padding: 5px
}

.ansP,
.ansPF {
    padding-left: 30px
}

.ansP .wpc_pin,
.ansPF .wpc_pin {
    margin-left: -30px
}

select {
    padding: 5px 10px 5px 5px;
    margin: 0;
    height: 32px
}

#b_context .rssmgrp .b_subModule,
.overlay-container .rssmgrp .b_subModule {
    border-bottom: 0
}

#b_context .b_entitySubTitle,
#b_results .b_entityTP .b_entitySubTitle {
    margin-top: -9px
}

.b_entityTP .b_infocardTopR .b_floatR_img {
    padding-bottom: 10px
}

.b_vmparent {
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flexbox;
    display: -webkit-box;
    display: flex;
    align-items: center
}

input,
textarea,
h4,
h5 {
    font: inherit;
    font-size: 100%
}

body,
.b_no h4,
h2 .b_secondaryText,
h2 .b_alert {
    font: 13px/normal Arial, Helvetica
}

h1,
h2,
h3 {
    font: 13px/1.2em 'Microsoft YaHei', Arial, Helvetica, sans-serif
}

h2 {
    font-size: 20px;
    line-height: 24px
}

h3,
.b_no h1 {
    font-size: 18px
}

cite {
    font-style: normal
}

th {
    font-weight: normal
}

.sb_alert a {
    font-style: italic
}

#sp_requery {
    font-size: 16px;
    line-height: 1.2em
}

#b_content,
#b_context,
.b_expando {
    line-height: 1.2em
}

cite,
#b_context,
.b_expando,
#vidans2 {
    word-wrap: break-word
}

#sa_ul li,
.nowrap {
    white-space: nowrap
}

.b_footer {
    line-height: 18px
}

.b_smText,
.b_footnote,
.b_imageOverlay,
.ciot {
    font-family: Arial, Helvetica;
    font-size: 11px;
    line-height: normal
}

.b_ad .b_adlabel,
.b_adrnd .b_adlabel,
.b_ad .b_adlabel strong,
.b_adrnd .b_adlabel strong {
    font: 12px/normal Arial, Helvetica
}

.b_mText {
    font: 16px/20px Arial, Helvetica
}

.b_focusLabel,
.b_secondaryFocus,
.b_focusTextExtraSmall {
    font: 18px/1.2em 'Microsoft YaHei', Arial, Helvetica, sans-serif
}

.b_focusTextExtraSmall {
    line-height: 1.3em
}

.b_entityTitle,
.b_prominentFocusLabel,
.b_xlText {
    font: 24px/1.2em 'Microsoft YaHei', Arial, Helvetica, sans-serif
}

.b_entityTitle {
    line-height: normal
}

.b_entitySubTitle {
    font: 14px/1.2em 'Microsoft YaHei', Arial, Helvetica, sans-serif
}

.b_focusTextSmall,
.b_focusTextMedium,
.b_focusTextLarge {
    font: 200 32px/1.2em 'Microsoft YaHei', Arial, Helvetica, sans-serif
}

.b_focusTextMedium {
    font-size: 40px
}

.b_focusTextLarge {
    font-size: 60px
}

strong,
.b_active a,
.b_no h4,
.b_strong,
.b_ad .b_adlabel strong,
.b_adrnd .b_adlabel strong,
.cbl {
    font-weight: 700
}

h1 strong,
h2 strong,
h3 strong,
.b_xlText strong,
.b_focusTextSmall strong {
    font-family: 'Microsoft YaHei', Arial, Helvetica, sans-serif;
    font-weight: normal
}

#b_tween {
    font-size: 12px
}

#b_tween>span,
#b_tween .ftrH {
    line-height: 30px
}

.sb_count {
    text-transform: capitalize
}

a,
.b_topbar a:hover,
.b_pag a:hover,
.cbtn:hover,
.cbtn a:hover,
.b_hlButton:hover,
.ftrB a:hover,
.b_algo:hover .b_vList h2 a,
.b_algo:first-child:hover .b_vList h2 a,
#b_results>.b_ans:hover .ent_cnt h2>a,
#b_results>.b_ans:hover #sp_requery h2>a,
#b_results>.b_ans .b_rich>.b_vList>li:hover h5.b_lBMargin>a {
    text-decoration: none
}

a:hover,
.b_algo:first-child:hover h2 a,
.b_algo .b_underline a,
.sb_add .b_underline a,
#b_results>.b_ad li:first-child .sb_adTA:hover h2 a,
#b_results>.b_adrnd li:first-child .sb_adTA:hover h2 a {
    text-decoration: underline
}

#b_results>li.b_ans.b_topborder {
    padding: 15px 19px 10px 19px;
    margin-bottom: 12px;
    box-shadow: 0 0 0 1px rgba(0, 0, 0, .05), 0 2px 3px 0 rgba(0, 0, 0, .1)
}

#b_results>li.b_ans.b_topborder.b_tophb {
    border: 1px solid #ddd;
    box-shadow: none;
    padding: 0
}

.b_tophb .b_tophbh {
    padding: 15px 19px 16px 19px
}

.b_tophb .b_tophbb {
    border-top: 1px solid #ddd;
    padding: 15px 19px 19px 19px
}

.b_tophb .bgtopwh {
    background-color: #fff
}

.b_tophb .bgtopgr {
    background-color: #f9f9f9
}

.b_tophb .b_tophbb.bgbtopnone {
    border-top: none
}

#b_results>.b_ad+.b_top,
#b_results>.b_adrnd+.b_top {
    margin-top: 20px
}

.b_top .b_attribution+.b_rich,
.b_top .b_factrow+.b_rich {
    padding-top: 8px
}

.b_top .b_topTitle+.b_rich {
    padding-top: 12px
}

.b_tHeader,
.b_demoteText,
.b_secondaryText,
.b_attribution,
.b_factrow,
.b_focusLabel,
.b_footnote,
.b_ad .b_adlabel,
.b_adrnd .b_adlabel,
#b_tween .b_dropdown a,
.b_expando .b_subModule,
.b_expando .b_suppModule,
.b_algo .b_vList td,
#b_content .b_lowFocusLink a,
#b_context .b_secondaryText,
#b_context .b_attribution,
#b_context .b_factrow,
#b_context .b_footnote,
#b_context .b_ad .b_adlabel,
#b_context .b_adrnd .b_adlabel,
.b_expando .b_secondaryText,
.b_expando .b_attribution,
.b_expando .b_factrow,
.b_expando .b_footnote,
#b_tween .b_nonselectable,
.ctxtb {
    color: #767676
}

#b_context .b_mhdr:hover .b_secondaryText,
.b_expando .b_mhdr:hover .b_secondaryText {
    color: #001ba0
}

h2.b_topTitle {
    font-size: 24px;
    line-height: 1.2em
}

#b_results>.b_top .b_prominentFocusLabel,
#b_results>.b_top .b_topTitle,
#b_results>.b_top .b_focusTextExtraSmall,
#b_results>.b_top .b_focusTextExtraSmall a,
#b_results>.b_top .b_focusTextSmall,
#b_results>.b_top .b_focusTextSmall a,
#b_results>.b_top .b_focusTextMedium,
#b_results>.b_top .b_focusTextMedium a,
#b_results>.b_top .b_focusTextLarge,
#b_results>.b_top .b_focusTextLarge a,
.ctxt {
    color: #111
}

span.b_negText.b_focusTextExtraSmall {
    color: #c80000 !important
}

span.b_posText.b_focusTextExtraSmall {
    color: #006d21 !important
}

.b_top .b_focusTextExtraSmall a,
.b_top .b_focusTextSmall a,
.b_top .b_focusTextMedium a,
.b_top .b_focusTextLarge a {
    text-decoration: none
}

#b_results>.b_top:hover .b_focusTextExtraSmall a,
#b_results>.b_top:hover .b_focusTextSmall a,
#b_results>.b_top:hover .b_focusTextMedium a,
#b_results>.b_top:hover .b_focusTextLarge a {
    color: #001ba0
}

#b_results>.b_top .b_focusTextExtraSmall a:hover,
#b_results>.b_top .b_focusTextSmall a:hover,
#b_results>.b_top .b_focusTextMedium a:hover,
#b_results>.b_top .b_focusTextLarge a:hover {
    text-decoration: underline
}

select,
.ctxt,
.ctxtb {
    outline: none
}

select,
.sic {
    border: 1px solid #bfdcf0;
    padding: 0 0 0 5px
}

select:hover,
.sic:hover {
    border-color: #0072c5
}

.ctxt,
.ctxtb {
    background-color: #f2f8fc
}

.ctxt,
.ctxtb,
.ccal {
    border: 1px solid #bfdcf0
}

.ctxt.b_focusTextMedium,
.ctxtb.b_focusTextMedium {
    padding: 3px 15px 8px 15px;
    height: 57px
}

.ctxt.b_outTextBox,
.ctxtb.b_outTextBox {
    border-top: 4px solid #0072c5;
    padding: 0 15px 8px 15px
}

.ctxt.b_outTextBox:focus,
.ctxtb.b_outTextBox:focus {
    border-top: 1px solid #0072c5;
    padding-top: 3px
}

.ctxt:hover,
.ctxtb:hover,
.ccal:hover {
    border-color: #0072c5
}

.ctxt:focus,
.ctxtb:focus {
    border-color: #0072c5;
    background-color: #fff
}

.ccal .ctxt,
.ccal .ctxtb,
.ccal .ctxt:hover,
.ccal .ctxtb:hover,
.ccal .ctxt:focus,
.ccal .ctxtb:focus,
.ccal .ccali {
    background: none;
    border: none
}

#b_results>.b_ans :-ms-input-placeholder {
    color: #767676
}

#b_results>.b_ans::-moz-placeholder {
    color: #767676
}

#b_results>.b_ans::-webkit-input-placeholder {
    color: #767676
}

.fc_cal_holder table {
    font-size: 11px
}

body .fc_cal_holder {
    border: 1px solid #0072c5
}

body .fc_cal_holder .fc_cal_disabled {
    color: #767676
}

body .fc_cal_holder a:link,
body .fc_cal_holder a:visited {
    color: #666
}

body .fc_cal_holder td,
body .fc_cal_holder .fc_cal_disabled,
body .fc_cal_holder .fc_cal_days td {
    width: 20px;
    line-height: 20px;
    padding: 0 10px 10px 0
}

.fc_cal_holder tr td:first-child {
    padding-left: 10px
}

.fc_cal_holder tr:last-child td {
    padding-bottom: 15px
}

body .fc_cal_holder .fc_cal_days td {
    line-height: 15px;
    color: #767676;
    background-color: #fff
}

body .fc_cal_holder a {
    padding: 0
}

body .fc_cal_holder td a:hover,
body .fc_cal_holder td a:active,
body .fc_cal_holder td.fc_cal_current a:hover,
body .fc_cal_holder td.fc_cal_current a:active {
    background-color: #eee;
    color: #666
}

body .fc_cal_holder .fc_cal_monthHolder+.fc_cal_monthHolder {
    border-left: 1px solid #bfdcf0
}

body .fc_cal_holder .fc_cal_monthHolder {
    background-color: #fff;
    border: 0;
    padding: 15px 15px 10em 15px
}

body .fc_cal_holder th div {
    background-color: #fff;
    border: 0;
    padding: 0 0 15px;
    color: #666;
    text-align: center;
    font-size: 13px
}

body .fc_cal_holder .fc_cal_current a {
    background-color: #001ba0
}

body .fc_cal_monthDec.fc_cal_monthChange,
body .fc_cal_monthInc.fc_cal_monthChange {
    background: url(/sa/simg/navchevrons_topRefresh.png) no-repeat;
    width: 8px;
    height: 12px;
    background-position: 0 -110px;
    font-size: 0
}

body .fc_cal_monthDec.fc_cal_monthChange {
    background-position: 0 -44px
}

body .fc_cal_holder .fc_cal_month_first .fc_cal_monthDec {
    margin: 1px 0 0 15px
}

body .fc_cal_holder .fc_cal_month_last .fc_cal_monthInc {
    margin: 1px 15px 0 0
}

strong {
    color: #c00;
    font-weight: normal
}

.sa_as li.pp_tile strong {
    color: #111;
    font-weight: 700
}

cite strong {
    font-weight: 700
}

.b_attribution,
cite strong {
    color: #006d21
}

#b_results p {
    word-wrap: break-word
}

.b_algo .b_attribution .c_tlbx,
#b_context .b_ans h2 {
    color: #767676
}

.b_hPanel>span,
input.ctxt,
input.ctxtb {
    vertical-align: middle
}

.b_deep h3,
.b_ans h5,
.b_attribution,
.b_vList>li,
.b_hList>li,
.b_caption,
.b_moreLink,
.b_xlText {
    padding-bottom: 3px
}

.b_factrow {
    padding-bottom: 3px
}

.b_vPanel {
    margin-bottom: -10px
}

#b_results>.b_pag {
    padding-bottom: 10px
}

.b_ans .b_imagePair>.inner {
    padding-top: 1px;
    padding-bottom: 7px
}

#b_results .b_imagePair.square_mi {
    padding-left: 21px
}

#b_results .b_imagePair.square_mi>.inner {
    margin-left: -21px
}

#dict_ans .b_imagePair.square_mi>.inner {
    margin-top: 2px
}

.knwp:hover .knbx {
    display: block
}

.knwp .knic {
    padding-top: 2px
}

.b_inlineList div,
.knbx.c_tlbx img,
.b_ans .b_title H2,
.b_ans .b_title div {
    display: inline-block
}

.ctxt,
.ctxtb {
    padding: 6px 0 6px 10px;
    height: 18px
}

.b_hList .image_wrapper>.cico {
    position: static;
    padding-bottom: 0
}

.fiw {
    padding-right: 0;
    padding-bottom: 0
}

.fiw>select {
    vertical-align: middle;
    line-height: 26px
}

.b_ans .b_rs>h2 {
    padding-bottom: 7px
}

#b_context .b_ad h2,
#b_context .b_adrnd h2,
.b_ad h2,
.b_adrnd h2,
.b_ad .b_attribution,
.b_adrnd .b_attribution,
.b_ans .b_caption,
.b_vPanel .b_lBottom {
    padding-bottom: 0
}

.b_ad .b_adlabel,
.b_adrnd .b_adlabel {
    font-size: 13px
}

#b_context .b_ad .b_adlabel,
#b_context .b_adrnd .b_adlabel {
    margin-bottom: 8px
}

.b_ad .b_caption,
.b_adrnd .b_caption {
    padding-bottom: 10px
}

.b_hList .b_vList,
.b_hList .b_vPanel,
.b_ad li,
.b_adrnd li {
    margin-bottom: 0
}

#b_results .b_ad .b_vlist2col,
#b_results .b_adrnd .b_vlist2col,
#b_results .b_ad .b_factrow,
#b_results .b_adrnd .b_factrow {
    margin-top: -10px
}

.b_vlist2col {
    overflow: hidden
}

.b_vlist2col ul:first-child {
    margin: 0 40px 0 0
}

.b_rs .b_vlist2col li,
#b_context .b_ans .b_vList li {
    padding: 0 0 6px
}

#sp_requery .b_pAlt {
    color: #666
}

.b_safe {
    color: #008000
}

.cipt,
.cipl,
.ciptr,
.ciplr {
    vertical-align: text-top
}

.b_suffix div.nc_os {
    background-color: #2196ff;
    color: #fff;
    padding: 0 3px
}

.b_underSearchbox {
    margin: 13px 20px 14px
}

.b_underSearchbox~#b_tween {
    margin-top: -22px
}

.ghosttext {
    color: #777
}

.b_hxlText {
    font-size: 18px;
    line-height: 23px;
    padding-bottom: 3px;
    color: #c00
}

.cf_space {
    padding: 3px 0 7px 0
}

#b_tween .ftrB {
    margin-left: -14px
}

nobr {
    white-space: inherit
}

.b_vList>li {
    word-wrap: break-word
}

.b_hList .sml img {
    display: inherit
}

.bm_component .b_hList>li>.sml {
    line-height: 0
}

.bm_component .b_hList .cico {
    padding-bottom: 0
}

#b_context .b_ans h2 {
    font-size: 16px;
    color: #666;
    line-height: 22px
}

h2 {
    font-size: 18px;
    line-height: 23px
}

.b_xlText {
    font-size: 24px;
    line-height: 30px
}

h3 {
    font-family: Arial, Helvetica
}

.b_deep h3 {
    font-size: 16px;
    line-height: 21px
}

#b_content,
#b_context,
.b_expando {
    line-height: 18px
}

.b_ad li,
.b_adrnd li,
#b_context>.b_ad>ul>li,
#b_context>.b_adrnd>ul>li {
    margin-bottom: 7px
}

#b_context .b_entityTP {
    padding: 9px 19px 4px 19px;
    margin: -10px -20px -6px -20px;
    width: 100%;
    box-shadow: 0 0 0 1px rgba(0, 0, 0, .05), 0 2px 3px 0 rgba(0, 0, 0, .1)
}

.overlay-container .b_entityTP {
    padding: 10px 20px 5px 20px
}

#b_context .b_ans:not(:first-child)>.b_entityTP {
    margin-top: -16px
}

#b_context .b_ad:not(:last-child),
#b_context .b_adrnd:not(:last-child) {
    padding-bottom: 15px;
    border-bottom: 1px solid #ebebeb
}

.b_expando .b_ans {
    padding-bottom: 15px;
    border-bottom: 1px solid #ebebeb
}

#b_context .b_ans:not(:last-child) {
    padding-bottom: 5px;
    border-bottom: 1px solid #ebebeb
}

h2 {
    font-size: 20px;
    line-height: 24px
}

.b_mhdr .b_moreLink,
.b_mhdr .b_secondaryText {
    margin-top: 8px
}

.sw_meIc:after,
.sw_spd:after,
.idp_ham:after,
.idp_wlid:after,
.idp_tw:after {
    position: relative;
    content: url(/sa/simg/SharedSpriteDesktopTwoToneLogoTealSpy_0817.png)
}

.sw_meIc,
.sw_spd,
.idp_ham,
.idp_wlid,
.idp_tw {
    position: relative;
    overflow: hidden;
    direction: ltr
}

.idp_ham {
    height: 14px;
    width: 20px
}

.idp_ham:after {
    left: -99px;
    top: 0
}

.idp_ham:hover:after,
.idp_ham:active:after,
.idp_ham:focus:after {
    top: -16px
}

.idp_wlid,
.idp_tw,
.sw_meIc {
    height: 16px;
    width: 16px
}

.idp_wlid:after {
    left: -384px
}

.idp_tw:after {
    left: -645px
}

.sw_meIc:after {
    left: -341px;
    top: 0
}

.sw_spd:after {
    left: -663px
}

::-webkit-search-decoration,
::-webkit-search-cancel-button,
.b_searchbox {
    -webkit-appearance: none
}

z {
    a: 1
}

z {
    a: 1
}

.b_searchboxForm,
.sa_as {
    background-color: #fff
}

.b_searchboxForm .b_searchboxSubmit {
    background-color: #fff;
    border-color: #fff
}

.b_scopebar,
.b_scopebar a,
.b_scopebar a:visited,
.id_button,
.id_button:visited {
    color: #666
}

.b_scopebar .b_active a,
.b_scopebar a:hover,
.id_button:hover {
    color: #111
}

.b_idOpen a#id_l,
a#id_rh.openfo {
    color: #333;
    background-color: #fff
}

#bepfo,
#id_d {
    color: #333;
    background-color: #fff
}

.wpc_bub a {
    color: #001ba0
}

#sw_as {
    color: #666
}

.sa_tm strong {
    color: #111
}

.sa_hv {
    background: #f5f5f5
}

.sa_hd {
    color: #111
}

#b_header {
    padding: 14px 0 0 0;
    margin: 0 0 0 0;
    background-color: #fff
}

#b_header #sb_form,
.b_logoArea,
.b_logo,
.b_searchboxForm,
.id_button,
.id_avatar,
.idp_ham,
.b_scopebar li,
.b_scopebar a {
    display: inline-block
}

#b_header #sb_form {
    margin-right: 10px
}

.b_logoArea {
    text-align: right;
    width: 86px;
    height: 40px;
    margin: 0 14px 0 0;
    vertical-align: top
}

.b_logo {
    text-indent: -999px;
    text-align: left;
    margin-top: 2px;
    vertical-align: top
}

.b_searchbox {
    width: 490px;
    margin: 5px 0 1px 20px;
    padding: 0 10px 0 0;
    border: 0;
    max-height: 30px;
    outline: none;
    box-sizing: content-box;
    height: 35px;
    vertical-align: top
}

#b_header .b_searchbox.b_softkey {
    width: 435px
}

.b_searchboxSubmit {
    height: 20px;
    width: 20px;
    text-indent: -99em;
    border-width: 0;
    border-style: solid;
    margin: 10px;
    background-position: -121px 0;
    outline: 0
}

#sw_as {
    width: auto;
    position: relative;
    z-index: 6
}

.sa_as {
    position: absolute;
    width: 100%;
    display: none
}

#sa_ul div.sa_tm,
#sa_ul .sa_hd {
    margin-left: 20px
}

#sw_as #sa_ul li.pp_tile {
    padding-left: 20px
}

.sa_hd {
    padding-top: 5px
}

.b_searchboxSubmit,
.sa_sg {
    cursor: pointer
}

z {
    a: 1
}

.b_searchboxForm {
    box-shadow: 0 0 0 1px rgba(0, 0, 0, .1), 0 2px 4px 0 rgba(0, 0, 0, .16)
}

.b_idOpen #id_d,
.b_focus .b_searchboxForm,
.b_searchboxForm:hover,
#bepfo,
#id_hbfo.slide_down,
#sw_as #sa_ul:not(:empty) {
    box-shadow: 0 0 0 1px rgba(0, 0, 0, .1), 0 2px 4px 1px rgba(0, 0, 0, .18)
}

#id_h {
    display: none;
    position: relative;
    float: right;
    text-align: right;
    margin: -4px 40px 0 0;
    line-height: 50px
}

.id_button {
    margin: 0 8px
}

#id_l {
    vertical-align: top
}

#id_rh {
    padding: 0 8px 0 16px
}

.sw_spd {
    vertical-align: top;
    margin-left: 8px;
    height: 32px;
    width: 32px;
    border-radius: 16px;
    top: 9px
}

.sw_meIc {
    vertical-align: top;
    margin: 17px 0 0 8px
}

#bepfo,
#bepfm,
#bepfl {
    width: 372px
}

#bepfm {
    display: block
}

#bepfl {
    text-align: center;
    margin: 50px 0
}

#bepfo {
    position: absolute;
    right: 0;
    z-index: 6;
    text-align: left
}

.idp_ham {
    top: 1px;
    margin: 0 20px 0 16px;
    height: 14px;
    width: 20px
}

.b_scopebar {
    padding: 0;
    margin: 25px 0 0 100px;
    border-bottom: 1px solid #ddd
}

#b_header {
    border-bottom: none
}

.blue2#miniheader .b_scopebar ul {
    height: 33px;
    overflow-y: hidden
}

.b_scopebar ul {
    height: 39px;
    overflow-y: hidden
}

.b_scopebar li {
    padding: 3px 0;
    margin: 0 12px;
    line-height: 25px
}

.b_scopebar a {
    padding: 0 8px
}

.b_scopebar .b_active {
    border-bottom: 3px solid #de3700
}

#b_header .b_topbar,
#b_header .b_scopebar {
    background: none;
    margin-bottom: 0;
    overflow-y: inherit
}

.b_logo {
    font-family: Arial, Helvetica
}

a,
#b_header a,
#b_header a:hover,
.b_toggle,
.b_toggle:hover {
    text-decoration: none
}

.sa_hv {
    text-decoration: underline
}

input {
    font: inherit;
    font-size: 100%
}

.b_searchboxForm {
    font: 18px/normal 'Microsoft YaHei', Arial, Helvetica, sans-serif
}

.b_searchbox {
    font-size: 16px
}

.id_button {
    line-height: 50px
}

.b_scopebar .b_active a {
    font-weight: 600
}

.b_scopebar,
.b_scopebar li,
.sa_tm {
    line-height: 30px
}

#sa_ul,
.pp_title {
    font: 16px/normal 'Microsoft YaHei', Arial, Helvetica, sans-serif
}

#sa_ul .sa_hd {
    font: 14px/20px 'Segoe UI Semibold', 'Arial', 'Helvetica', 'Sans-Serif';
    cursor: default
}

#sw_as strong {
    font-family: 'Microsoft YaHei', Arial, Helvetica, sans-serif
}

z {
    a: 1
}

#sb_form .b_logo {
    vertical-align: top;
    float: right;
    margin-top: 2px
}

#b_pole,
#b_content #b_pole {
    margin-top: 3px;
    margin-bottom: 5px
}

#sa_ul,
.pp_title {
    font-family: 'Segoe UI', Arial, Helvetica, Sans-Serif
}

#b_header #sb_form {
    min-width: 70px
}

@media all and (max-width:1100px) {
    #id_s,
    #id_n {
        display: none
    }
}

#sb_form .b_logo {
    height: 36px;
    width: 28px
}

#sb_form .b_searchboxForm,
#sb_form .sa_as,
#sb_form #sw_as li.pp_tile {
    border-color: #eee
}

z {
    a: 1
}

.b_logo {
    display: inline-block;
    width: 83px;
    height: 34px;
    text-indent: 0;
    overflow: hidden;
    direction: ltr
}

.b_logo div {
    text-indent: -999px
}

.b_logo {
    background: none
}

.b_logo:after {
    content: none
}

.b_searchboxSubmit {
    background-image: url(/sa/simg/SharedSpriteDesktopTwoToneLogoTealSpy_0817.png);
    background-repeat: no-repeat
}

.blue2#miniheader #sb_form_go {
    height: 32px;
    width: 32px;
    background-position: -76px 0;
    border-width: 5px 6px 4px 5px;
    margin: 3px 4px 4px
}

.blue2#miniheader .b_searchboxForm .b_searchboxSubmit {
    background-color: #fff;
    border-color: #fff
}

z {
    a: 1
}

.de_title,
.de_title1,
.de_title2 {
    font-size: 16px;
    color: #c00;
    font-weight: 500;
    padding-top: 2px;
    float: left
}

.de_title {
    width: 40px
}

.de_title1 {
    width: 40px;
    margin-bottom: 5px
}

.de_title2 {
    width: 70px;
    margin-bottom: 5px
}

.de_ti2 {
    float: left;
    font-weight: bold;
    padding-bottom: 2px;
    font-size: 13px;
    color: #000
}

.de_li,
.de_li1,
.de_li2,
.sb_li {
    margin-top: 0;
    font-size: 14px;
    color: #777;
    padding-left: 0
}

.de_li {
    clear: both
}

.de_li1 {
    width: 492px
}

.de_li3 {
    padding-left: 15px
}

.de_li4 {
    padding-bottom: 11px
}

.de_li2 {
    float: left;
    margin-bottom: 0
}

.sb_li {
    float: left;
    width: 436px;
    margin-bottom: 5px;
    margin-top: 3px;
    clear: both
}

.web_div,
.web_div1 {
    display: block;
    zoom: 1
}

.st_div {
    font-size: 18px;
    margin-bottom: 14px
}

.rt_div {
    padding-top: 10px;
    margin-bottom: 19px;
    float: left;
    clear: both
}

.clear {
    clear: both;
    *height: 0
}

.hd_div {
    float: left;
    margin-right: 20px;
    font-size: 22px;
    font-weight: bold
}

.hd_div1 {
    float: left;
    width: 100%;
    padding-top: 14px;
    padding-bottom: 2px
}

.hd-p1-2 {
    font-size: 13px;
    line-height: 20px;
    color: #777;
    float: left;
    margin-right: 3px
}

.df_div {
    margin-bottom: 0;
    padding-bottom: 0;
    clear: both;
    overflow: hidden
}

.hi_div {
    float: left;
    padding-left: 10px
}

.wd_div {
    float: left;
    width: 100%
}

.dm_div {
    width: 100%
}

.dym_div {
    margin-bottom: 14px
}

.dym_sp {
    margin-right: 10px;
    font-size: 13px;
    line-height: 20px;
    display: inline-block;
    color: #001ba0
}

.dym_sp:visited {
    color: #600090
}

.dym_p {
    padding-bottom: 30px;
    clear: both
}

.mm_div {
    clear: both;
    padding: 0 0 34px 24px
}

.df_div1,
.df_div2 {
    clear: both;
    zoom: 1
}

.df_cr_w,
.df_hm_w,
.df_hm_w1 {
    margin-bottom: 2px;
    max-width: 456px;
    overflow: hidden
}

.df_wb_a {
    color: #000;
    font-size: 13px;
    font-weight: bold;
    padding-bottom: 15px;
    margin-top: 10px;
    clear: both
}

.df_wb_i,
.df_wb_i1 {
    float: left;
    margin: 4px 8px 2px 0
}

.df_wb_i1 {
    clear: both
}

.df_wb_i {
    cursor: pointer
}

.dym_area {
    padding-top: 10px
}

.df_wb_c {
    line-height: 23px;
    font-size: 13px;
    clear: both
}

.df_wb_s {
    float: left;
    margin-bottom: 14px
}

.de_wf_d {
    margin-bottom: 3px;
    font-size: 14px;
    line-height: 25px;
    font-weight: bold
}

.sc_lf,
.hd_if,
.sc_df,
.gl_fl,
.col_fl,
.hd_pr,
.hd_prUS,
.hd_tf,
.gra,
.infor,
.ex_label {
    float: left
}

.col_fl {
    max-width: 462px
}

.sc_lf {
    max-width: 532px
}

.def_fl {
    padding-bottom: 0;
    overflow: hidden
}

.hd_prUS {
    color: #000
}

.hd_tf {
    margin-left: 5px;
    width: 39px;
    _margin-top: 0
}

.hd_tf_lh {
    line-height: 22px
}

.sc_df {
    padding-top: 15px;
    padding-left: 10px;
    color: #04c
}

.sc_df a,
.hd_if a {
    color: #001ba0
}

.sc_df a:visited,
.hd_if a:visited {
    color: #600090
}

.pl_bd {
    padding-left: 20px;
    padding-top: 20px
}

.sb_tb {
    margin-bottom: 20px;
    zoom: 1
}

.sb_def {
    float: left;
    margin-bottom: 8px;
    width: 170px
}

.sb_rv {
    width: 477px;
    float: left
}

.dymp_wd_snt {
    font-size: 13px;
    float: left;
    margin-top: 5px
}

.dymp_sm_top {
    clear: both;
    margin: 30px 0
}

.dymp_sm {
    background-image: url('/s/a/sw13.png');
    width: 75px;
    height: 26px;
    float: left;
    margin-right: 20px
}

.dymp_link {
    margin-bottom: 30px;
    margin-top: 4px;
    float: left
}

.dymp_img_snt,
.dymp_img_shnt {
    float: left;
    margin-bottom: 10px
}

.dymp_img_snt {
    margin-right: 10px
}

.dm_ul {
    list-style-type: none;
    margin-left: 0;
    margin-bottom: 20px;
    padding-left: 0;
    overflow: hidden
}

.no_sh {
    color: #777;
    margin-left: 0;
    margin-bottom: 20px;
    padding-left: 0;
    display: none
}

.sen_bar {
    margin-bottom: 16px;
    background-color: #eee;
    height: 26px
}

.smt_hw {
    font-size: 14px;
    margin-bottom: 18px;
    font-weight: bold
}

.gl_blk {
    display: block
}

.gl_none {
    display: none
}

.in_tip {
    margin: 0 0 10px 0;
    padding: 10px 0 10px 10px;
    font-size: 13px;
    background-color: #f9f5dd
}

#colid {
    margin-top: 3px
}

.ads_ifm {
    border: 0
}

.ads_dwn {
    margin-bottom: 10px
}

.no_results {
    font-size: 15px
}

.search_hint {
    margin: 10px 0 5px 0;
    font-weight: bold
}

i {
    font-style: normal
}

#crossid,
#homoid,
#webid {
    padding-top: 13px
}

#crossid .p1-1 {
    font-weight: normal
}

.qdef {
    overflow: hidden
}

.qdef .hd_div {
    float: none;
    font-size: 250%;
    left: -1px;
    position: relative;
    font-weight: 500;
    line-height: 100%
}

.qdef .hd_div strong {
    font-weight: 500
}

.hd_pro {
    padding-right: 30px
}

.hd_pron {
    color: #777;
    font-size: 14px;
    float: left
}

.au_df {
    margin-bottom: 7px
}

.comple,
.bil,
.val,
.se_d,
.gra,
.infor,
.se_def_nu {
    line-height: 22px
}

.bil,
.val {
    color: #333
}

.li_exs {
    color: #777;
    margin-bottom: 11px;
    font-size: 14px;
    padding-left: 20px;
    display: none;
    line-height: 24px
}

.li_ex {
    margin-bottom: 3px;
    overflow: hidden
}

.hd_ca {
    margin-right: 5px;
    color: #777;
    font-size: 14px;
    float: left
}

.infor,
.gra {
    color: #c00;
    font-size: 14px
}

.hd_div2 {
    float: left;
    margin-right: 20px;
    font-size: 14px;
    font-weight: bold
}

.hw_area2 {
    padding-top: 12px;
    padding-bottom: 15px;
    float: left
}

.hd_div {
    float: left;
    margin-right: 20px;
    font-size: 22px;
    font-weight: bold
}

.disp {
    float: right;
    display: block;
    border-style: solid;
    border-width: 1px;
    border-color: #0072c6;
    margin-top: 10px
}

.pos {
    float: left;
    font-weight: bold
}

.def_row {
    vertical-align: top
}

#authid td:first-child {
    width: 20px;
    padding-right: 10px
}

#authid td {
    padding-right: initial
}

.idm_s {
    float: left
}

.dis,
.idm_s {
    font-size: 14px;
    color: #001ba0;
    font-weight: bold;
    padding: 4px 0 9px 20px
}

.ex_pa {
    margin-left: 24px
}

.idm_lin {
    width: 100%;
    margin-bottom: 18px
}

.de_nu {
    width: 15px
}

.showEx {
    display: block
}

.hideEx {
    display: none
}

.se_d {
    width: 20px;
    float: left
}

.se_lis,
.idmdef_li {
    margin-left: 20px
}

.idmdef_li {
    clear: both
}

.se_buf {
    margin-left: 24px;
    float: left;
    margin-top: 4px
}

.se_d,
.def_pa,
.idmdef_li {
    color: #000;
    font-size: 14px
}

.idm_ti {
    color: #fff;
    font-weight: bold;
    font-size: 12px;
    background-color: #000;
    line-height: 18px;
    text-align: center;
    vertical-align: middle;
    width: 35px
}

.infor,
.sen_com,
.com_sep,
.bil,
.gra {
    padding-right: .25em
}

.infor,
.label {
    padding-left: .25em
}

.sen_com {
    float: left;
    font-size: 14px;
    font-weight: bold
}

.bil_ex,
.val_ex {
    line-height: 24px;
    color: #777
}

.bil_dis,
.val_dis {
    color: #001ba0;
    font-weight: bold;
    font-size: 14px;
    padding-right: .25em;
    line-height: 19px
}

.sepr,
.wsepr {
    padding-left: .25em;
    padding-right: .25em;
    font-size: 16px
}

.sepr {
    color: #001ba0
}

.wsepr {
    color: #a1a1a1
}

.sensep,
.fillink {
    font-size: 14px;
    color: #001ba0;
    line-height: 22px;
    float: left
}

.fillink:visited {
    color: #600090
}

.filswitch {
    padding-bottom: 11px;
    font-size: 14px;
    color: #001ba0;
    line-height: 22px;
    float: left;
    cursor: pointer
}

.sensep {
    padding: 0 .25em
}

.filtext {
    font-size: 14px;
    color: #000;
    font-weight: bold;
    line-height: 22px;
    float: left;
    display: none
}

.cate,
.src,
.diff {
    float: left;
    clear: both
}

.senDef {
    padding-top: 11px
}

.cate {
    padding-top: 2px
}

.src {
    padding: 2px 0
}

.diff {
    padding-bottom: 7px
}

.filter {
    overflow: hidden;
    clear: both
}

#sde_all,
#sc_all,
#ss_all,
#sd_all {
    display: none
}

#sde_all_te,
#sc_all_te,
#ss_all_te,
#sd_all_te {
    display: block
}

.each_seg {
    width: 100%
}

.de_co,
.idm_def {
    overflow: hidden
}

.de_seg_c {
    float: left
}

.de_seg {
    margin-top: 6px;
    width: 100%;
    display: none
}

.li_pos {
    clear: both
}

.def_pa {
    line-height: 22px
}

.pos_lin {
    width: 100%;
    padding-bottom: 7px;
    overflow: hidden
}

.idm_seg {
    margin: 7px 20px 17px 0
}

.li_id {
    border: 1px solid #ebebeb;
    margin: 2px 0 20px 20px;
    display: none;
    width: 510px;
    clear: both
}

.hw_ti {
    width: 100%
}

.buf_hw {
    width: 100%;
    padding-bottom: 15px
}

.sh_s {
    font-size: 12px;
    color: #0072c6;
    display: block;
    float: right;
    border: 1px solid #0072c6;
    padding: 5px;
    margin-top: 10px;
    margin-bottom: 9px;
    cursor: pointer;
    line-height: 12px
}

.sh_s:hover {
    color: #3888cc;
    border: 1px solid #3888cc
}

.point {
    padding: 8px;
    float: left
}

.pp {
    background-image: url("/s/a/point.png");
    _filter: progid:DXImageTransform.Microsoft.AlphaImageLoader(src="/s/a/point.png");
    background-repeat: no-repeat;
    display: block;
    height: 3px;
    width: 3px;
    _background: none
}

.key {
    background-image: url("/s/a/key.png");
    _filter: progid:DXImageTransform.Microsoft.AlphaImageLoader(src="/s/a/key.png");
    background-repeat: no-repeat;
    display: block;
    height: 10px;
    width: 20px;
    _background: none;
    float: left;
    margin: 3px 0 0 3px
}

.pos_close,
.pos_open {
    background-image: url("/s/a/pos.png?v=2");
    background-repeat: no-repeat;
    display: block;
    height: 18px;
    width: 18px;
    margin-left: 5px;
    cursor: pointer;
    float: left
}

.pos_open {
    background-position: -64px 0
}

.pos_close {
    background-position: 0 0
}

.pos_open:hover {
    background-position: -85px 0
}

.pos_close:hover {
    background-position: -21px 0
}

.hw {
    float: left
}

.infle {
    float: left;
    font-size: 14px;
    color: #001ba0;
    padding-left: 20px
}

.infle a:hover {
    text-decoration: underline
}

.posref {
    padding-left: 20px
}

.infle_pro {
    float: left;
    font-size: 14px;
    padding-left: 5px;
    color: #777
}

#pos_0,
#idiom_0 {
    display: block
}

.synon {
    width: 100%;
    clear: both
}

.sy_la {
    font-size: 14px;
    color: #333;
    float: left;
    line-height: 24px
}

.au_ref {
    font-size: 14px;
    color: #001ba0;
    line-height: 24px;
    display: block;
    float: left;
    padding-left: .25em
}

.sim {
    float: left;
    padding: .25em
}

.qdef .hd_prUS,
.qdef .hd_pr {
    color: #777;
    font-size: 14px
}

.qdef .pos {
    width: 35px;
    font-size: 93%;
    background-color: #aaa;
    color: #fff;
    line-height: 18px;
    vertical-align: middle;
    text-align: center
}

.qdef .pos1 {
    margin-top: 2px
}

.qdef .web {
    background-color: #333
}

.qdef ul {
    padding-top: 10px
}

.qdef li {
    padding-top: 4px;
    font-weight: bold
}

.qdef .def {
    padding-left: 15px;
    line-height: 20px;
    vertical-align: top;
    font-size: 14px;
    width: 90%
}

.qdef .def a {
    color: #000
}

.qdef .def a:hover {
    color: #04c
}

.qdef .hd_div1 .p2-1 {
    font-weight: bold;
    color: #777
}

.qdef .hd_div1 {
    color: #777;
    padding-top: 9px
}

.qdef:after {
    clear: both
}

.qdef .hd_if a {
    margin: 0 6px 0 0;
    font-size: 14px
}

.qdef div.simg,
.qdef div.simgmore {
    margin-top: 10px
}

.qdef .simg {
    left: 1px
}

.qdef df_div {
    margin-top: 60px
}

.qdef .hd_tf_lh {
    line-height: 19px;
    padding-top: 3px
}

.qdef .wd_div {
    margin-top: 10px
}

.qdef .df_div {
    padding-top: 10px
}

.qdef .hd_area {
    float: none;
    overflow: hidden;
    margin-bottom: 0
}

.qdef a:active {
    background-color: transparent
}

.XDF {
    display: inline-block;
    padding-top: 10px
}

.XDFDefault:hover {
    background-position: -161px 0
}

.qdef h1 {
    font-size: 100%
}

.content h2 {
    font-size: 100%
}

a {
    text-decoration: none
}

BODY {
    color: #000;
    line-height: normal;
    font-family: Arial, Arial, Helvetica, Sans-Serif;
    font-size: small;
    font-style: normal;
    font-variant: normal;
    font-weight: normal;
    min-width: 98px;
    margin: 0
}

.def {
    color: #333
}

.content {
    margin: 41px 0 0 10px;
    max-width: 987px
}

.contentPadding {
    padding-left: 10px
}

.hd_area {
    float: left;
    width: 100%;
    margin-bottom: 14px
}

.rs_area {
    WIDTH: 100%;
    FLOAT: left
}

.lf_area {
    float: left;
    width: 532px
}

.sidebar {
    PADDING-BOTTOM: 0;
    MARGIN: 42px -271px 0 50px;
    WIDTH: 240px;
    WORD-WRAP: break-word;
    FLOAT: left
}

.st_div2 {
    padding-bottom: 30px;
    padding-left: 30px;
    float: left
}

.st_div2 a {
    color: #04c
}

.ads_div {
    width: 240px;
    margin-left: -10px;
    margin-top: 28px
}

.hd_p1_1,
.p1-2 {
    font-size: 13px;
    color: #777
}

.hd_p1_1 {
    _font-family: Lucida Sans Unicode, sans-serif;
    float: left;
    margin-top: 4px
}

.p1-2 {
    line-height: 20px
}

.p1-1 {
    font-size: 14px;
    line-height: 22px;
    color: #333;
    font-weight: bold
}

.p1-3,
.p1-3:visited,
.p1-3:hover,
.p1-3-1,
.p1-3-1:hover,
a.p1-3-1:visited {
    font-size: 13px;
    text-decoration: none
}

.p1-3,
.p1-3:visited,
.p1-3:hover {
    color: #a1a1a1
}

.p1-3-1,
a.p1-3-1:visited,
.p1-3-1:hover,
.p1-3-1_dymp,
a.p1-3-1_dymp:visited,
.p1-3-1_dymp:hover {
    color: #001ba0;
    float: left;
    margin-right: 10px
}

.p1-3-1_dymp,
a.p1-3-1_dymp:visited,
.p1-3-1_dymp:hover {
    float: left;
    margin-right: 10px
}

.p1-4 {
    font-size: 14px;
    color: #001ba0;
    line-height: 24px
}

.p1-5,
.p1-5-1-blk,
.p1-5-1-none {
    font-size: 13px;
    color: #001ba0;
    margin-top: 2px
}

.p1-5-1-blk {
    float: left;
    display: block
}

.p1-5-1-none {
    float: left;
    display: none
}

.p1-6 {
    font-size: 13px;
    color: #000;
    font-weight: bold
}

.sen_en>span,
.p1-7,
.p1-7:visited,
.p1-7:active,
.p1-7:hover,
.p1-8,
.p1-8:visited,
p1-8:active,
.p1-8:hover,
.p1-9,
.p1-9:visited,
p1-9:active,
.p1-9:hover {
    font-size: 14px;
    text-decoration: none;
    outline: medium none
}

.p1-7,
.p1-7:visited,
.p1-7:active,
.p1-7:hover {
    line-height: 20px;
    color: #c00;
    font-weight: normal
}

.p1-8,
.p1-8:visited,
p1-8:active,
.p1-8:hover {
    line-height: 21px;
    color: #000
}

.p1-9,
.p1-9:visited,
p1-9:active,
.p1-9:hover {
    line-height: 23px;
    color: #777
}

.p1-10 {
    font-weight: normal;
    margin-bottom: 8px;
    font-size: 14px
}

.p1-11 {
    font-weight: normal;
    color: #777;
    font-size: 14px
}

.p1-12 {
    font-size: 14px;
    color: #000;
    line-height: 22px
}

.p1-12:hover {
    color: #001ba0
}

.p2-1 {
    font-size: 13px;
    color: #333;
    float: left
}

.p2-2 {
    font-size: 14px;
    color: #000;
    font-weight: bold
}

.p3-1 {
    font-size: 16px;
    color: #c00
}

.p4,
.p4_dymp {
    font-size: 22px;
    color: #000;
    font-weight: bold
}

.li_num {
    color: #fff;
    padding-left: 4px;
    font-size: 11px;
    font-family: Arial
}

.lq_top {
    clear: both;
    margin: 50px 0
}

.lq_sm {
    background-image: url('/s/a/bingtranslate.png');
    width: 30px;
    height: 31px;
    float: left;
    margin-right: 10px
}

.lq_ms {
    font-size: 13px
}

.lq_ms1 {
    margin-bottom: 6px
}

.aud,
.aud_f,
.bigaud,
.bigaud_f,
.ktv,
.ktv_f,
.clsktv,
.rtdef,
.rtdef_f,
.clp,
.clp_f,
.ilist,
.ilist1,
.bigktv,
.bigktv_f,
.fil_c,
.fil_o {
    background-image: url("/s/live/icon.png?v=2");
    background-repeat: no-repeat
}

.aud,
.aud_f,
.ktv,
.ktv_f,
.clsktv,
.rtdef,
.rtdef_f {
    height: 24px;
    width: 24px;
    cursor: pointer
}

.bigktv,
.bigktv_f {
    height: 18px;
    width: 20px;
    cursor: pointer
}

.bigaud,
.bigaud_f {
    height: 19px;
    width: 19px;
    cursor: pointer
}

.fil_o,
.fil_c,
.clp,
.clp_f {
    height: 16px;
    width: 16px;
    margin-right: 7px;
    margin-top: 1px;
    float: left
}

.fil_o,
.fil_c {
    margin-top: 4px;
    cursor: pointer
}

#confil,
#filhide {
    display: none
}

#filhide,
#filshow {
    overflow: hidden;
    clear: both
}

.ilist {
    height: 15px;
    width: 5px;
    margin-left: 10px;
    margin-right: 10px
}

.ilist {
    background-position: -319px 7px
}

.aud {
    background-position: -56px 0;
    display: block
}

.aud_f {
    display: block;
    background-position: -84px 0
}

.bigktv {
    display: block;
    background-position: -460px 0
}

.bigktv_f {
    display: block;
    background-position: -480px 0
}

.bigaud {
    background-position: -358px 0;
    display: block
}

.bigaud_f {
    display: block;
    background-position: -377px 0
}

.ktv {
    background-position: -112px 0
}

.ktv_f {
    background-position: -140px 0
}

.fil_o,
.clp {
    background-position: -280px 0
}

.fil_c,
.clp_f {
    background-position: -299px 0
}

.clsktv {
    background-position: -168px 0
}

.rtdef {
    background-position: 0 0
}

.rtdef_f {
    background-position: -28px 0
}

.sentLoad {
    position: absolute;
    display: none
}

.ilist1 {
    background-position: -326px 0;
    height: 15px;
    width: 15px;
    margin-top: 5px;
    margin-right: 9px;
    float: left
}

.simg {
    width: 80px;
    height: 80px;
    float: left;
    border: 1px solid #ccc;
    margin-left: -1px;
    position: relative
}

.simg:hover {
    border-color: #36b;
    z-index: 100
}

.img_area div {
    margin-top: 20px
}

.img_area {
    clear: both;
    overflow: hidden
}

.simgmore {
    float: left
}

.simgmore .morelnk {
    cursor: pointer;
    background-color: #ccc;
    display: block;
    width: 25px;
    height: 80px;
    position: relative;
    border: 1px solid #ccc
}

.simgmore .sw_arwh {
    position: absolute;
    left: 6px;
    bottom: 35px
}

.simgmore .sw_up {
    margin-top: 33px;
    margin-left: 5px;
    -webkit-transform: rotate(90deg);
    -moz-transform: rotate(90deg);
    -ms-transform: rotate(90deg);
    -o-transform: rotate(90deg);
    transform: rotate(90deg)
}

.sa_cptic {
    font-size: 1%;
    background-color: #fff
}

.sa_cpti,
.sa_cpti_a {
    display: none;
    float: right;
    height: 9px;
    margin-right: 4px;
    width: 6px;
    background: url("/s/se2.png") no-repeat scroll 0 -18px transparent
}

.sa_cp {
    word-wrap: break-word;
    display: block;
    background-color: #333
}

.sa_video,
.vt_vp,
.vt_vph,
.sa_cpoc {
    position: absolute
}

.sa_cpoc {
    -moz-border-bottom-colors: 0;
    -moz-border-image: 0;
    -moz-border-left-colors: 0;
    -moz-border-right-colors: 0;
    -moz-border-top-colors: 0;
    border-color: #e6e6e6 #e6e6e6 #d9d9d9;
    border-style: solid;
    border-width: 1px;
    display: none;
    padding: 5px;
    width: 100%;
    z-index: 1004
}

.vt_vph {
    background: url("/s/a/video/vld.gif") no-repeat scroll center center #000
}

.vt_vp,
.vt_vph {
    cursor: pointer;
    height: 227px;
    width: 300px;
    z-index: 1
}

.bi_pag {
    float: left;
    padding: 20px 0 30px 24px;
    width: 100%
}

.bi_pag ul,
.bi_pag li {
    list-style: none outside none;
    margin: 0;
    padding: 0;
    float: left
}

.bi_pag a {
    color: #001ba0;
    text-decoration: none;
    display: block;
    margin: 0 .38em 0 0;
    padding: .3em .7em;
    text-align: center
}

a.bi_pagS {
    color: #000
}

.bi_pag a:hover,
a.bi_pagS {
    background: none repeat scroll 0 0 #ededed;
    text-decoration: none
}

.se_div {
    margin-top: 10px;
    padding-bottom: 0;
    overflow: hidden
}

.se_li {
    list-style-type: none;
    padding-top: 0;
    padding-left: 0;
    clear: both
}

.se_li1 {
    margin-bottom: 5px;
    margin-left: 0;
    padding-left: 0;
    overflow: hidden;
    float: left;
    max-width: 508px
}

.se_n_d {
    float: left;
    width: 24px;
    padding-top: 3px
}

.sen_en,
.sen_cn,
.sen_ime {
    width: 100%;
    font-size: 14px;
    padding-left: 0;
    margin-left: 0
}

.sen_en {
    line-height: 14px;
    margin-bottom: 2px;
    color: #000
}

.sen_cn {
    line-height: 22px;
    margin-bottom: 2px;
    color: #777
}

.sen_ime {
    line-height: 17.5px;
    color: #777;
    margin-bottom: 2px
}

.sc_hd_ads {
    float: left;
    margin-left: 30px
}

.sc_hd_ads1 {
    margin-left: -10px
}

.sen_li {
    margin: 5px 0 2px 0;
    width: 100%
}

.sen_con {
    color: #333;
    padding: 2px 0;
    font-size: 14px;
    line-height: 22px
}

.sen_con strong {
    color: #c00
}

.sen_count {
    font-size: 14px
}

.sen_count a {
    color: #a1a1a1
}

.sen_count a:hover {
    color: #04c
}

.sen_count a:visited {
    color: #639
}

.senDefLink {
    overflow: hidden
}

.tb_div {
    color: #36b;
    padding-top: 0;
    z-index: 0;
    border-bottom: #ccc solid 1px;
    overflow: hidden;
    height: 100%
}

.tbs_b {
    font-size: 14px;
    z-index: 1;
    color: #000;
    float: left;
    height: 100%;
    line-height: 24px;
    clear: both;
    padding-right: 5px
}

.tb_a,
.tb_a:visited,
.tb_a:active,
.tb_b,
.tb_b:visited,
.tb_b:active {
    font-size: 14px;
    margin: 0 34px 0 0;
    padding: 0 8px;
    outline: none;
    z-index: 1;
    display: block;
    float: left;
    height: 100%;
    line-height: 22px;
    position: relative;
    color: #000
}

.tb_a,
.tb_a:visited,
.tb_a:active {
    color: #333;
    font-weight: bold;
    border-bottom: #0072c6 solid 3px
}

.tb_b:hover {
    color: #000;
    border-bottom: #ccc solid 3px
}

.tb_a:hover,
.tb_b:hover {
    text-decoration: none
}

.tb_c {
    font-weight: bold;
    background-color: #eee;
    margin-right: 0
}

.selCat,
.selSrc,
.selDiff {
    margin-top: 3px
}

.tb_ft_a,
.tb_ft_b {
    font-size: 13px;
    margin: 5px 5px 0 5px
}

.tb_ft_a {
    color: #000;
    font-weight: bold
}

.tb_ft_b {
    color: #04c
}

.tg_open,
.tg_close {
    float: right;
    width: 12px;
    height: 8px;
    cursor: pointer;
    background-image: url("/s/live/arrow.png");
    background-repeat: no-repeat;
    position: relative;
    bottom: -10px
}

.tg_open {
    background-position: -45px 0
}

.tg_close {
    background-position: 0 0
}

#b_header {
    height: 100px
}

.qdef .hd_div strong {
    color: #000
}

.ads_dwn.top_ad {
    width: 160px;
    height: 176px;
    background-image: url(/th?id=OJ.hhcqaPAuQWj60w&pid=MSNJVFeeds);
    background-repeat: no-repeat;
    margin-bottom: 0
}

.ads_dwn .dict_title {
    display: block;
    text-align: center;
    height: 14px;
    padding-top: 86px;
    font-size: 14px;
    line-height: 14px;
    color: #fff;
    margin-bottom: 8px
}

.ads_dwn .dict_description {
    display: block;
    height: 12px;
    text-align: center;
    font-size: 12px;
    line-height: 12px;
    color: #babfc7;
    margin: 0 auto;
    margin-bottom: 12px
}

.ads_dwn .button {
    display: block;
    width: 126px;
    height: 26px;
    margin: 0 auto;
    border: solid 1px #fff;
    -ms-border-radius: 4px;
    border-radius: 4px;
    color: #fff;
    font-size: 12px;
    line-height: 28px;
    text-align: center;
    padding: 2px 0
}

.ads_dwn .button:hover {
    text-decoration: none
}

.ads_dwn.center_ad,
.ads_dwn.bottom_ad {
    background: #f0f0f0;
    width: 160px;
    margin-bottom: 1px
}

.ads_dwn .dict_ad_title {
    font-size: 12px;
    line-height: 12px;
    padding: 16px 0 14px 0;
    text-align: center
}

.center_ad span {
    display: inline-block;
    vertical-align: top
}

.center_ad .app_center {
    width: 48px
}

.center_ad .app_left {
    margin-left: 12px
}

.center_ad .app_right {
    margin-right: 12px
}

.center_ad .app_center_img {
    border-left: solid 1px #d1d1d1;
    border-right: solid 1px #d1d1d1
}

.dict_mobile_apps span a {
    letter-spacing: -1px;
    font-size: 10px;
    line-height: 10pt;
    color: #474747;
    display: block;
    text-align: center;
    margin: 0 auto;
    text-decoration: none
}

.dict_mobile_apps img {
    display: block
}

.center_ad .qrcode {
    width: 120px;
    margin: 0 auto;
    padding: 10px 0 18px 0
}

.bottom_ad .button {
    color: #000;
    margin-bottom: 10px;
    border-color: #444
}

.bottom_ad .button img {
    vertical-align: text-bottom;
    padding-right: 6px
}

.bottom_ad {
    padding-bottom: 28px
}
'''