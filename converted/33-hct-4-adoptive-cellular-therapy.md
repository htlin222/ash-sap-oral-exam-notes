# Chapter 33: HCT and Cellular Therapy 4 — Adoptive Cellular Therapy

造血細胞移植與細胞治療 4——過繼性細胞治療(Adoptive Cellular Therapy)

作者:Melody Smith

## Key Points(重點摘要)

- Cellular therapy 大幅擴展了血液腫瘤與實體瘤病人的治療選擇。
- 目前有多款 targeting CD19 或 BCMA 的 CAR T 產品獲得 FDA 核准,用於復發/難治(relapsed/refractory)血液腫瘤。
- CAR T 可用 autologous 或 allogeneic 細胞來源製備。
- CAR T 以 MHC-independent 方式辨識抗原;TCR T 則需經由 MHC 呈現抗原才能辨識。
- Cytokine release syndrome(CRS)、immune effector cell-associated neurotoxicity syndrome(ICANS),以及 immune effector cell-associated hemophagocytic lymphohistiocytosis-like syndrome(IEC-HS),都是 CAR T 治療後可能出現的「on-target, off-tumor」副作用。

## Introduction(前言)

1. 「Adoptive cellular therapy」這個名詞涵蓋哪些治療型態?
   - 涵蓋範圍從 hematopoietic cell transplantation(HCT)到各種工程化細胞治療(engineered cell therapies),核心概念是轉輸(transfer)免疫細胞來治療感染或癌症。
   - 目前臨床進展主要奠基於數十年來對 tumor-infiltrating lymphocytes(TILs)、chimeric antigen receptor(CAR)T 細胞,以及 allogeneic HCT 的研究累積。
   - Allogeneic HCT 已於前一章討論,故本章聚焦於其他型態的細胞治療:CAR T、TCR-engineered cells、NK cells、TILs。

## Cancer therapy with CAR T cells(CAR T 細胞治療)

2. CAR(chimeric antigen receptor)的分子結構包含哪些組成?
   - 細胞外(extracellular)的 antibody single-chain variable fragment(scFv)
   - Spacer/hinge region
   - T-cell receptor(TCR)的 CD3ζ chain
   - Costimulatory domain

3. CAR 的世代演進(generation)如何區分?各世代差異為何?
   - **第一代(first generation)**:缺乏 costimulatory domain。體外(in vitro)有活性,但體內(in vivo)expansion、persistence 與抗腫瘤活性皆有限。
   - **第二代(second generation)**:加入 1 個 costimulatory domain(如 CD28、4-1BB、OX40),in vivo 活性明顯改善,是目前臨床應用的主流架構。
   - **第三代(third generation)**:加入 2 個 costimulatory domains。
   - **Armored CAR**:進一步加入 cytokine signaling 元件。

4. CAR T 辨識抗原的方式與內生性 T 細胞(endogenous T cells)有何不同?
   - CAR 一旦辨識到標的抗原,即以 **human leukocyte antigen(HLA)/MHC-independent** 的方式與抗原結合並活化。
   - 這與內生性 T 細胞需要透過 MHC 呈現抗原才能活化的機制,是重要區別。

5. CAR T 細胞如何製備與輸注給病人?
   - 以 retroviral 或 lentiviral transduction,或以 mRNA electroporation 方式,將 CAR 基因導入 autologous 或 allogeneic T 細胞。
   - 病人先接受 **lymphodepleting chemotherapy**(通常為 fludarabine + cyclophosphamide),之後才輸注經體外(ex vivo)擴增的 CAR T 細胞。
   - Lymphodepletion 的作用:清除 regulatory T cells,並營造有利的 cytokine milieu,以促進 CAR T 在體內的擴增。

6. 目前有多少款 CAR T 產品獲得 FDA 核准?分別 target 什麼抗原?這些核准有何共同特徵?
   - 共 **7 款** FDA 核准的 CAR T 產品:
     - **5 款 CD19-targeted**:tisagenlecleucel、axicabtagene ciloleucel、brexucabtagene autoleucel、lisocabtagene maraleucel、obecabtagene autoleucel
     - **2 款 BCMA(B-cell maturation antigen)-directed**:idecabtagene vicleucel、ciltacabtagene autoleucel
   - 共同特徵:
     - 目前 FDA 核准的 CAR T 產品**皆為 autologous**,尚無 allogeneic、TCR 或 NK 細胞產品獲批准。
     - 所有已核准的產品**皆用於 relapsed/refractory 情境**,尚無用於 frontline 治療的核准。

## Allogeneic CAR T-cell products(異體 CAR T 產品)

7. Autologous CAR T 製程有哪些限制,促使發展 allogeneic(「off-the-shelf」)CAR T?
   - Autologous 製程:以 leukapheresis 從病人本身取得細胞,基因改造後回輸給同一病人。
   - 免疫學上可避免 alloreactivity(如 CAR 排斥或 graft-versus-host disease〔GVHD〕介導的反應)。
   - 但限制包括:
     - 病人先前治療常已損害其 T 細胞族群,且疾病快速進展時可能來不及等待製程完成 → 並非所有病人皆可行。
     - 製程費時、成本高,且需將細胞運送至第三方製造場所往返。
   - Allogeneic(供者來源、「off-the-shelf」)產品可望克服上述限制。

8. Allogeneic CAR T 目前面臨的主要限制是什麼?如何因應?
   - 主要限制:**GVHD 風險**。
   - 因應策略(仍在積極研究中):
     - 對 αβ TCR 進行基因編輯(gene editing)
     - 改用 γδ T 細胞或 NK 細胞作為 CAR 製造來源
   - 基因編輯最常使用 **CRISPR** 或 **transcription activator-like effector nucleases(TALEN)**,以移除 TCRαβ 或 MHC class II 的表現。

## Cancer therapy with TCR-engineered cells(TCR 工程化細胞治療)

9. TCR-engineered T 細胞最適合 target 哪一類抗原?
   - 最適合 target 來自 **tumor-associated 細胞膜蛋白或細胞內/細胞核蛋白** 的胜肽(peptide),因為這些胜肽是經由 MHC 呈現在細胞表面。

10. TCR-engineered T 細胞的製備原理與基因轉殖方式為何?
    - 依賴產生能專一辨識目標腫瘤抗原的 TCR α 與 β chains,並在 autologous T 細胞中表現這些工程化 TCR 分子。
    - 基因轉殖方式:retroviral vector、lentiviral vector,或非病毒的 **sleeping beauty system**,各方式皆帶有 insertional mutagenesis 的風險。

11. TCR-engineered 細胞與後期世代 CAR 在結構設計上有何不同?
    - 與後期世代 CAR 不同,TCR 工程化細胞**不會**額外引入胞外 costimulatory domain。
    - 其功能依賴保留自身原有的 **natural TCR-signaling components**。

12. TCR T 細胞發揮效果的能力取決於哪些因素?為何需要優化以降低自體免疫風險?
    - 取決於:(1)細胞表面工程化 TCRαβ heterodimer 的表現量;(2)該受體對標的抗原的親和力(affinity)。
    - 需優化的原因:降低與**內生性 TCR chains 錯誤配對(mispairing)**的風險,此配對錯誤理論上可能產生非預期、自體反應性的 TCR specificity,導致 **on-target, off-tumor autoimmunity**。

13. CAR T 與 TCR T 兩者在辨識機轉、適應症與副作用型態上有何差異?

    | 比較項目 | CAR T | TCR T |
    |---|---|---|
    | 抗原辨識 | MHC-independent,直接辨識 cognate antigen | 需經 MHC 呈現於抗原呈現細胞(APC) |
    | 主要適應症 | Relapsed/refractory **血液腫瘤** | 主要用於**晚期實體瘤** |
    | 抗原選擇性 | 較高 | 較低,off-target 效應風險相對較高 |
    | 共同點 | 兩者皆可能造成 on-target, off-tumor 毒性 |

## Natural killer cells(自然殺手細胞)

14. NK 細胞作為 adoptive cellular therapy 來源的優勢為何?
    - NK 細胞屬先天免疫系統(innate immune system),可以 **抗原非依賴(antigen-independent)** 的方式發揮抗腫瘤與抗微生物活性。
    - 其活性受 activating 與 inhibitory receptors(包括 killer cell immunoglobulin-like receptors〔KIR〕)之間的平衡調控。
    - 與 T 細胞不同,NK 細胞**不需事先抗原致敏(sensitization)**,且在 allogeneic 情境下**不會造成 GVHD**——這是其作為細胞治療來源的重要優勢。

15. Allogeneic NK 細胞如何製備與擴增?
    - 常取自 peripheral blood 或 umbilical cord blood 產物,經 **T 細胞與 B 細胞 depletion**(可合併 CD56+ 細胞的 positive selection)以富集 NK 細胞。
    - 以 cyclophosphamide + fludarabine 進行 lymphodepleting chemotherapy,可促進 in vivo NK 細胞的 persistence 與 expansion,部分機轉與誘導高濃度 **IL-15** 有關。

16. NK 細胞治療目前觀察到的安全性特點與局限為何?
    - 目前 NK 細胞治療**未觀察到**與其他細胞治療相關的 CRS、neurotoxicity 或 GVHD。
    - 局限:NK 細胞的 persistence、cytotoxicity、homing 能力仍有待改善,相關研究持續進行中。
    - NK 細胞也可被工程改造成 **CAR NK cells**。

## Tumor-infiltrating lymphocytes(TILs)

17. TIL 治療的原理與流程為何?
    - 取自病人 **手術切除的腫瘤組織** 中的 autologous T 細胞,經體外擴增後回輸病人,並合併 **IL-2** 給予以加強抗腫瘤活性。
    - **高劑量 IL-2** 相較於低劑量 IL-2,可帶來更好的治療結果。
    - 與其他過繼性細胞治療相同,輸注前需先給予 lymphodepleting chemotherapy(preparative regimen),以提升輸注 T 細胞在體內的 persistence。

18. TIL 治療目前有哪些臨床實證與核准適應症?最大挑戰是什麼?
    - 已於難治性實體瘤(melanoma、cholangiocarcinoma、non–small cell lung cancer 等)中展現持久治療反應(durable responses)。
    - 轉移性黑色素瘤病人使用 TIL 治療的 overall response rate 約 **30%–50%**。
    - **Lifileucel** 是 FDA 核准的 TIL 產品,適應症為成人**無法切除或轉移性黑色素瘤(unresectable or metastatic melanoma)**。
    - 最大挑戰:每位病人皆須先接受**手術取得腫瘤組織**才能分離出 TILs,限制了此療法的可近性。

## Adoptive cellular therapy complications(過繼性細胞治療的併發症)

19. CRS(cytokine release syndrome)的病理生理機轉為何?
    - CRS 是 CAR T 細胞產品輸注後發生的**全身性發炎反應(systemic inflammatory response)**。
    - 機轉與活化的淋巴球及其他免疫細胞在抗腫瘤反應過程中釋放的 cytokines(如 **IFN-γ、TNF-α、IL-6**)有關,加上 CAR T 快速活化與擴增也參與其中。

20. CRS 的臨床表現範圍為何?如何治療?
    - 表現範圍極廣:多數病人為輕度、非特異性的體質性症狀(fever、flu-like symptoms);少數病人可進展為高階(high-grade)症候群,出現 hypotension、lung injury,甚至致命的多重器官功能障礙。
    - 治療原則以 **symptomatic/supportive care** 為主,可能需要:vasopressors、輸血/血品支持、mechanical ventilation。
    - 特異性藥物治療:
      - **Tocilizumab**(IL-6 receptor antagonist antibody):可緩解 CRS,且**不干擾**抗腫瘤療效。
      - **全身性 corticosteroids**:對 CRS 治療同樣有效,現有數據顯示也**不干擾**CAR T 的抗腫瘤活性。

21. ICANS 的臨床表現、發生時序與可能機轉為何?
    - ICANS(immune effector cell-associated neurotoxicity syndrome)是 CAR T 治療**第二常見**的副作用,可與 CRS **同時或先後**發生。
    - 表現範圍:輕者 delirium、dysphasia、akinetic mutism、headache、aphasia、tremor;重者可出現 seizure、somnolence,甚至危及生命的 cerebral edema。
    - 多數病例**可逆**,但也曾發生因 cerebral edema 致死的病例。
    - 機轉尚不明確,推測與 cytokine-mediated inflammation、myeloid cells 活化,以及 blood-brain barrier 破壞有關。
    - 危險因子:高腫瘤負荷(high tumor burden)、lymphodepletion 深度增加,皆與較高神經毒性發生率相關,但個別病人的風險仍難以準確預測。
    - **BCMA-targeted CAR T** 治療病人曾觀察到 **parkinsonism**,推測與 basal ganglia 細胞表現 BCMA 有關。

22. CRS 與 ICANS 的分級系統依據為何?由哪個學會制定?
    - 由於過去各臨床試驗使用不同的分級系統,**American Society of Transplantation and Cellular Therapy(ASTCT)**於 **2018 年**發布 CRS 與 neurotoxicity 的共識定義與分級標準。
    - **CRS 分級**主要依據 fever 的有無,以及 hypoxia 與 hypotension 的嚴重程度。
    - **ICANS 分級**依據神經學檢查發現,並將「回答問題的能力」(即 ICE score,Immune Effector Cell-Associated Encephalopathy score)納入評分。

    | ASTCT Grade | CRS(依 fever + hypotension/hypoxia) | ICANS(依 ICE score 及其他神經學表現) |
    |---|---|---|
    | 1 | Fever(≥38°C),無 hypotension、無 hypoxia | ICE score 7–9 |
    | 2 | Fever + hypotension(不需 vasopressor)及/或 hypoxia(需低流量鼻導管給氧) | ICE score 3–6 |
    | 3 | Fever + hypotension(需 1 種 vasopressor,±vasopressin)及/或 hypoxia(需高流量鼻導管、面罩等給氧) | ICE score 0–2,或癲癇發作(可緩解),或影像上局部腦水腫 |
    | 4 | Fever + hypotension(需多種 vasopressor,不含 vasopressin)及/或 hypoxia(需正壓通氣,如 CPAP/BiPAP/插管) | ICE score 0(無法喚醒),或危及生命的長時間癲癇,或瀰漫性腦水腫 |

23. 整體而言,CRS 與 ICANS 的預後與治療相關死亡率如何?
    - 兩者一般被認為是**可逆性毒性(reversible toxicities)**,治療相關死亡率(treatment-related mortality)風險低。
    - CAR T 治療的整體 treatment-related mortality,與另一項用於淋巴瘤或骨髓瘤的替代治療選項——autologous transplant——的死亡率範圍相近。

24. IEC-HS 是什麼?與 CRS、ICANS 有何區別?
    - **IEC-HS**(immune effector cell-associated hemophagocytic lymphohistiocytosis-like syndrome)是另一種 CAR T 相關毒性。
    - 因 macrophage 活化,表現類似 **hemophagocytic lymphohistiocytosis(HLH)** 的臨床症狀。
    - 雖與 CRS、ICANS **機轉不同**,但臨床表現可能重疊,包括 fever、hypotension、hypoxia。
    - **American Society of Transplantation and Cellular Therapy** 於 **2023 年**發布 IEC-HS 的共識定義與分級標準。

25. CAR T 治療有哪些中長期(mid- to long-term)副作用需要追蹤?
    - **Cytopenia**
    - **續發性惡性腫瘤(secondary malignancies)風險**,包括 **T-cell lymphomas**。
    - 這些長期副作用的發生率與機轉,仍待更多長期追蹤數據釐清。

## CD19-targeted CAR T-cell therapy for B-cell ALL(CD19 CAR T 用於 B 系急性淋巴性白血病)

26. CD19 CAR T 治療 relapsed/refractory B-ALL 的整體反應率如何?
    - 兒童與成人 R/R B-ALL 病人接受 CD19-directed CAR T 治療,反應率約 **80%–90%**。

27. 第一個獲 FDA 核准的 CAR T 產品是什麼?其核准依據為何?
    - **Tisagenlecleucel(tisa-cel,CTL019)**:一款 **4-1BB、CD3ζ** CAR T 產品,於 **2017 年 8 月**成為第一個獲 FDA 核准上市的 CAR T 療法。
    - 核准依據為 **ELIANA** 試驗(single-cohort、multicenter、global phase 2),納入 75 位年齡 3–23 歲、R/R CD19+ B-ALL 病人。
    - 結果:overall remission rate **81%**,所有緩解病人皆為 MRD 陰性;12 個月 event-free survival(EFS)**50%**,overall survival(OS)**76%**。
    - Grade 3–4 疑似 CAR T 相關事件發生於 75 位中的 55 位(**73%**);**77%** 病人出現 CRS,其中 **48%** 需要 tocilizumab;**40%** 出現神經學事件。

28. Anti-CD19 CAR T 用於成人 B-ALL 的核准過程有何波折?University of Pennsylvania 的早期經驗提供了什麼重要教訓?
    - 成人適應症的核准**曾因治療相關併發症而延遲**,早期臨床試驗中出現 **cerebral edema** 及 **refractory CRS** 導致死亡的病例。
    - University of Pennsylvania 團隊使用 CTL019(4-1BB、CD3ζ anti-CD19 construct):以 **fractionated dosing** 方式,20 位接受高劑量 CAR T 的病人中,CR rate **90%**,2 年 OS **73%**,2 年 EFS **49.5%**。
    - 相對地,接受**高劑量單次(high-dose single infusion)**輸注的病人,則出現高比例的 refractory CRS,6 位中有 3 位死於治療相關併發症,導致該治療組(arm)關閉——凸顯**劑量分次給予(fractionated dosing)可能有助於降低嚴重 CRS 風險**的概念。

29. 成人 R/R B-ALL 第一個獲 FDA 核准的 CAR T 產品是什麼?其關鍵試驗結果為何?
    - **Brexucabtagene autoleucel(brexu-cel)**:CD28、CD3ζ CD19 CAR T 細胞。
    - 核准依據 **ZUMA-3**(international phase 2 study),為成人(≥18 歲)R/R B-ALL 病人帶來 FDA 核准,並附有 **CRS 與 neurotoxicity 的黑框警語(black box warning)**。
    - 55 位可評估病人中:CR rate **71%**,中位反應持續時間 **12.8 個月**。
    - CRS 發生率 **89%**(n=49),grade 3–4 CRS **24%**(n=13)。
    - 2 例 grade 5 事件分別歸因於 **sepsis** 與 **brain herniation**,凸顯此治療的潛在致命風險。

30. B-ALL 患者接受 CAR T 治療後,目前臨床上尚未解決的關鍵問題是什麼?
    - 復發(relapse)與毒性管理(toxicity management)仍是 CAR T 廣泛應用的主要障礙。
    - 一項重要且尚未有定論的問題是:B-ALL 病人接受 CAR T 治療後,**allogeneic transplant 作為鞏固治療(consolidative procedure)的角色**應如何界定。

## CD19 CAR T in DLBCL(CD19 CAR T 用於瀰漫性大 B 細胞淋巴瘤)

31. 第二個獲核准的 CAR T 產品是什麼?其適應症與核准依據為何?
    - **Axicabtagene ciloleucel(axi-cel)**是第二個獲核准的 CAR T 產品。
    - 適應症:成人 relapsed/refractory large B-cell lymphoma(LBCL),需經 **≥2 線全身性治療**,涵蓋 DLBCL not otherwise specified、primary mediastinal LBCL、high-grade B-cell lymphoma,以及由 follicular lymphoma(FL)轉化而來的 DLBCL。
    - 核准依據為 **ZUMA-1**(single-cohort、multicenter phase 2 trial):101 位(共收案 111 位)、年齡 23–76 歲、經組織學確診之 R/R LBCL 病人,接受 lymphodepleting chemotherapy(cyclophosphamide + fludarabine)後,輸注目標劑量 **2×10⁶ CAR-T cells/kg**。

32. ZUMA-1 的療效與毒性結果為何?
    - ORR **82%**,CR rate **54%**,中位反應持續時間 **8.1 個月**;18 個月 OS 約 **52%**。
    - 最常見 grade 3+ 事件為 **neutropenia、anemia、thrombocytopenia**。
    - CRS 與神經學事件發生率分別為 **93%** 與 **64%**(grade 3+ 分別為 **13%** 與 **28%**)。

33. Axi-cel 如何進一步取得二線(second-line)適應症?
    - 2022 年 4 月,依據 **ZUMA-7**(randomized multicenter phase 2 study)結果,axi-cel 獲核准用於 **primary refractory LBCL**,或**一線治療完成後 12 個月內復發**的病人。
    - ZUMA-7 也發現:相較於標準治療(含 autologous HCT),接受 axi-cel 作為二線治療的 R/R LBCL 病人有**更佳的 OS**。

34. Tisa-cel 用於 LBCL 的核准依據與 CAR 結構特點為何?
    - Tisa-cel 也核准用於 LBCL(含 DLBCL、high-grade B-cell lymphoma、由 FL 轉化的 DLBCL),適用於接受 **≥2 線**全身性化學治療後的病人。
    - 與 axi-cel 不同,tisa-cel 的 CAR 使用 **4-1BB**(而非 CD28)作為 costimulatory domain。
    - 核准依據為 **JULIET** 試驗(phase 2、single-arm),納入 93 位年齡 ≥18 歲病人:best overall response rate **52%**,**40%** 達到 CR。
    - 毒性以 University of Pennsylvania grading scale 評估:grade 3–4 CRS 約 **22%**,無因毒性致死病例;grade 3–4 神經學事件 **12%**。

35. Liso-cel 有何獨特的產品設計?其核准依據與適應症為何?
    - **Lisocabtagene maraleucel(liso-cel)**是第三個獲核准用於 R/R LBCL 的產品,與 tisa-cel 同為 anti-CD19、4-1BB CAR T 產品。
    - **獨特之處**:以固定比例(fixed ratio)的 **CD4+ 與 CD8+ CAR T 細胞**,分成 **2 次劑量**給予。
    - 核准依據為 **TRANSCEND** 樞紐(pivotal)single-arm 臨床試驗,256 位可評估病人中:ORR **73%**,CR **53%**;grade 3–4 CRS 與神經學事件分別為 **2%** 與 **10%**。
    - 依 **TRANSFORM** 試驗結果,liso-cel 獲核准用於**二線**適應症:成人 LBCL 對一線 chemoimmunotherapy 難治、一線治療後 12 個月內復發,或因年齡/共病不適合接受 autologous HCT 者。

36. Axi-cel、liso-cel、tisa-cel 三者在核准治療線別(line of therapy)上有何異同?
    - Axi-cel 與 liso-cel **皆已獲核准用於二線(second-line)**治療。
    - Tisa-cel **僅核准用於三線(third-line)**適應症。

## CD19 CAR T in follicular lymphoma(CD19 CAR T 用於濾泡性淋巴瘤)

37. Axi-cel 用於濾泡性淋巴瘤(FL)的核准依據與結果為何?
    - CD19 CAR T 核准用於化學治療難治(chemorefractory)、且經 **≥2 線**前治療後仍進展的 FL 病人,依據為 **ZUMA-5**(phase 2)試驗中 axi-cel 的數據。
    - 結果:ORR **91%**,CR rate **61%**;**74%** 病人於 18 個月時仍維持緩解。
    - 惟這些優異結果伴隨不低的毒性:grade 3+ CRS 與 neurotoxicity 分別發生於 **8%** 與 **21%** 的病人。

38. Tisa-cel 用於 FL 的核准依據與結果為何?
    - 核准依據為 **ELARA** 試驗:overall response rate **86%**,CR rate **69%**。
    - 毒性:grade 3+ CRS 發生率 **48%**,grade 3+ ICANS 發生率 **4%**。

## CD19 CAR T in mantle cell lymphoma(CD19 CAR T 用於套細胞淋巴瘤)

39. Brexu-cel 用於套細胞淋巴瘤(MCL)的產品特性與試驗結果為何?
    - **Brexucabtagene autoleucel(brexu-cel)**與 axi-cel 為同一 CAR 構造,但以**不同製程**生產,目的在降低惡性 CD19+ B 細胞的干擾負擔並改善製造流程。
    - 測試族群:接受過**最多 5 線前治療**、疾病持續進展的 R/R MCL 病人。
    - Lymphodepletion 方案與細胞劑量與 axi-cel 相同(**2×10⁶ CAR+ cells/kg**)。
    - Phase 2 試驗:68 位病人接受治療,ORR **93%**,CR rate **67%**;12 個月 progression-free survival(PFS)**61%**,12 個月 OS **83%**。
    - 毒性:grade 3+ CRS **15%**,grade 3+ neurotoxicity **31%**;曾發生 2 例致命的感染相關不良事件。
    - 這些數據促成 brexu-cel 獲 FDA 核准用於 relapsed/refractory MCL。

## CAR T-cell therapy for multiple myeloma(CAR T 用於多發性骨髓瘤)

40. 多發性骨髓瘤(MM)CAR T 治療的標的抗原是什麼?為什麼選擇這個標的?
    - 標的為 **BCMA(B-cell maturation antigen)**,屬於 tumor necrosis factor superfamily 成員,同時表現於惡性與正常的 plasma cells。

41. 第一個獲 FDA 核准的 BCMA CAR T 產品是什麼?其結構與試驗結果如何?
    - **Idecabtagene vicleucel(ide-cel)**:第一個獲 FDA 核准的 BCMA CAR T 產品,結構為 **4-1BB、CD3ζ**、targeting BCMA。
    - 依據 multicenter phase 2 臨床試驗(**KarMMa-3**),128 位 R/R MM 病人接受治療:ORR **73%**,CR rate **33%**,MRD negativity 達成率 **26%**。
    - 毒性:CRS 發生率 **84%**(grade 3+ 僅 **5%**);神經毒性發生率 **18%**。

42. 第二個 BCMA CAR T 產品是什麼?其結構特點與試驗結果為何?
    - **Ciltacabtagene autoleucel(cilta-cel)**:targeting BCMA 上的 **2 個 epitopes**。
    - 依據 phase 2 臨床試驗(**CARTITUDE-1**),97 位 R/R MM 病人:ORR **94.8%**,stringent CR rate **56%**;6 個月 PFS **87.4%**,6 個月 OS **93.8%**。
    - 毒性:CRS 發生率 **95%**,neurotoxicity **21%**。
    - 依 **CARTITUDE-4** 試驗結果,cilta-cel 於 **2024 年 4 月**獲核准用於 MM 的**二線治療**。

43. 目前 MM 的 CAR T 治療存在哪些未解決的挑戰?
    - 是否有治癒(curative)潛力仍不明確,**復發(relapse)**仍是限制其更早線使用(up-front use)的主要障礙,反應率仍有進一步提升的空間。
    - 除 BCMA 外,**多個其他抗原標的**正在積極研究中,以期擴大 MM 細胞治療的選擇。

## 綜合小結

44. 展望未來,細胞治療領域的整體發展重點為何?
    - 持續致力於為血液腫瘤與實體瘤病人**尋找新的細胞治療標的抗原**。
    - 隨著治療創新持續推進,評估這些新療法相對於**現有已核准治療**的療效將是關鍵課題。
    - 由於這些新型治療手段的問世,血液科醫師也必須提高警覺,注意**先前未曾被辨識的潛在毒性**。

## Bibliography(參考文獻,原文列出,不逐條轉換為問答)

- Benjamin R, Graham C, Yallop D, et al. Genome-edited, donor-derived allogeneic anti-CD19 chimeric antigen receptor T cells in paediatric and adult B-cell acute lymphoblastic leukaemia: two phase 1 studies. *Lancet*. 2020;396:1885-1894.
- Depil S, Duchateau P, Grupp SA, et al. 'Off-the-shelf' allogeneic CAR T cells: development and challenges. *Nat Rev Drug Discov*. 2020;19:185-199.
- Fesnak AD, June CH, Levine BL. Engineered T cells: the promise and challenges of cancer immunotherapy. *Nat Rev Cancer*. 2016;16(9):566-581.
- Ghilardi G, Fraietta JA, Gerson JN, et al. T cell lymphoma and secondary primary malignancy risk after commercial CAR T therapy. *Nat Med*. 2024;30(4):984-989.
- Hamilton MP, Sugio T, Noordenbos T, et al. Risk of second tumors and T-cell lymphoma after CAR T-cell therapy. *N Engl J Med*. 2024;390(22):2047-2060.
- Hines MR, Knight TE, McNerney KO, et al. Immune effector cell-associated hemophagocytic lymphohistiocytosis-like syndrome. *Transplant Cell Ther*. 2023;29(7):438.e1-438.e16.
- June CH, Sadelain M. Chimeric antigen receptor therapy. *N Engl J Med*. 2018;379(1):64-73.
- Kumar A, Watkins R, Vilgelm AE. Cell therapy with TILs: training and taming T cells to fight cancer. *Front Immunol*. 2021;12:690499.
- Lee DW, Santomasso BD, Locke FL, et al. ASTCT consensus grading for cytokine release syndrome and neurologic toxicity associated with immune effector cells. *Biol Blood Marrow Transplant*. 2019;25(4):625-638.
- Maude SL, Laetsch TW, Buechner J, et al. Tisagenlecleucel in children and young adults with B-cell lymphoblastic leukemia. *N Engl J Med*. 2018;378(5):439-448.
- Mehta RS, Randolph B, Daher M, Rezvani K. NK cell therapy for hematologic malignancies. *Int J Hematol*. 2018;107(3):262-270.
- Park JH, Geyer MB, Brentjens RJ. CD19-targeted CAR T-cell therapeutics for hematologic malignancies: interpreting clinical outcomes to date. *Blood*. 2016;127(26):3312-3320.
- Rodriguez-Otero P, Ailawadhi S, Arnulf B, et al. Ide-cel or standard regimens in relapsed and refractory multiple myeloma. *N Engl J Med*. 2023;388(11):1002-1014.
- Rohaan MW, Borch TH, van den Berg JH, et al. Tumor-infiltrating lymphocyte therapy or ipilimumab in advanced melanoma. *N Engl J Med*. 2022;387(23):2113-2125.
- Shah NN, Johnson BD, Schneider D, et al. Bispecific anti-CD20, anti-CD19 CAR T cells for relapsed B cell malignancies: a phase 1 dose escalation and expansion trial. *Nat Med*. 2020;26:1569-1575.
- Shah NN, Maatman T, Hari P, Johnson B. Multi targeted CAR-T cell therapies for B-cell malignancies. *Front Oncol*. 2019;9:146.
- Smith M, Zakrzewski J, James S, Sadelain M. Posttransplant chimeric antigen receptor therapy. *Blood*. 2018;131(10):1045-1052.
- Westin JR, Oluwole OO, Kersten MJ, et al. Survival with axicabtagene ciloleucel in large B-cell lymphoma. *N Engl J Med*. 2023;389(2):148-157.
