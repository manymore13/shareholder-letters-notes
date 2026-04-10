# Operation Log

**Note**: This file is private and will not be published in the static site.

---

## Log Format

Each entry follows this format:
```
[YYYY-MM-DD HH:MM] Operation Type - Description
  - Created: [list of files created]
  - Updated: [list of files updated]
  - Notes: [additional notes]
```

---

## 2026-04-08

### [12:07] System Initialization
- **Created**: Wiki directory structure
- **Created**: CLAUDE.md schema configuration
- **Created**: wiki/index.md, wiki/log.md, wiki/about.md
- **Created**: templates/entity.md, templates/concept.md, templates/source.md
- **Notes**: MVP version initialized with basic structure

---

<!-- New log entries will be appended below -->

---

## 2026-04-08

### [19:50] Link Repair Operation
- **Operation**: Fixed 48 broken links in wiki/index.md
- **Created Entities (30 files)**:
  - entity-american-express.md, entity-benjamin-graham.md, entity-borsheims.md
  - entity-buffalo-news.md, entity-bnsf.md, entity-cap-cities-abc.md
  - entity-dexter-shoe.md, entity-fechheimer.md, entity-flightsafety.md
  - entity-geico.md, entity-gillette.md, entity-h-h-brown.md
  - entity-heinz.md, entity-helzbergs.md, entity-h-h-brown.md
  - entity-ibm.md, entity-iscar.md, entity-kansas-bankers-surety.md
  - entity-lowell-shoe.md, entity-lubrizol.md, entity-marmon-group.md
  - entity-midamerican-energy.md, entity-national-indemnity.md
  - entity-nebraska-furniture-mart.md, entity-rc-willey.md
  - entity-scott-fetzer.md, entity-sees-candies.md, entity-tti.md
  - entity-washington-post.md, entity-wells-fargo.md, entity-coca-cola.md
- **Created Concepts (16 files)**:
  - concept-intrinsic-value.md, concept-permanent-holdings.md
  - concept-owner-earnings.md, concept-economic-goodwill.md
  - concept-look-through-earnings.md, concept-margin-of-safety.md
  - concept-book-value.md, concept-capital-allocation.md
  - concept-yardsticks.md, concept-managerial-culture.md
  - concept-financial-strength.md, concept-normal-earning-power.md
  - concept-five-year-periods.md, concept-per-share-growth.md
  - concept-bolt-on-acquisitions.md, concept-inversion.md
- **Updated**: wiki/index.md (added American Express entry, updated statistics)
- **Notes**: All broken links have been fixed. Wiki now has 34 entity pages, 21 concept pages, and 48 source pages.


## 2026-04-08

### [13:10] Ingest - Buffett's Letters Collection
- **Operation**: Ingested Buffett's Letters to Shareholders (1977-2025)
- **Created**: wiki/sources/source-buffett-letters.md
- **Created**: wiki/sources/source-buffett-letters-1977.md
- **Created**: wiki/entities/entity-warren-buffett.md
- **Created**: wiki/entities/entity-berkshire-hathaway.md
- **Created**: wiki/concepts/concept-value-investing.md
- **Created**: wiki/concepts/concept-economic-moat.md
- **Created**: wiki/concepts/concept-float.md
- **Updated**: wiki/index.md
- **Notes**: 
  - Source files: raw/books/html/ (21 letters 1977-1997), raw/books/pdf/ (23 letters 2003-2025)
  - Created core entities: Warren Buffett, Berkshire Hathaway
  - Created core concepts: Value Investing, Economic Moat, Float
  - Analyzed 1977 letter in detail, established foundation for future letters

### [13:45] Batch 1 Processing - 1978-1987 Letters (HTML)
- **Operation**: Processed first batch of 10 Buffett letters (1978-1987)
- **Read**: 9 HTML files successfully (1978-1987, except 1985)
- **Issue**: 1985 HTML file appears to be binary format, unreadable
- **Created Source Pages**: 
  - source-buffett-letters-1978.md - ROE优先理念，浮存金概念
  - source-buffett-letters-1979.md - 通胀影响，承保周期
  - source-buffett-letters-1980.md - 非控股收益，GEICO投资
  - source-buffett-letters-1981.md - 收购原则，通胀影响
  - source-buffett-letters-1982.md - 未分配收益，股票发行
  - source-buffett-letters-1983.md - 家具城收购，经济商誉
  - source-buffett-letters-1984.md - WPPSS投资，股息政策
  - source-buffett-letters-1985.md - 占位符（待处理）
  - source-buffett-letters-1986.md - 永久持股，所有者收益
  - source-buffett-letters-1987.md - 市场先生理论
- **Created Entity Pages**:
  - entity-mrs-b.md - Rose Blumkin, 内布拉斯加家具城创始人
- **Created Concept Pages**:
  - concept-return-on-equity.md - 净资产收益率
  - concept-mr-market.md - 市场先生理论
- **Updated**: wiki/index.md
- **Notes**:
  - All source pages created in Chinese Simplified
  - File names use English for URL compatibility
  - Key concepts extracted: ROE, Mr. Market, Permanent Holdings, Owner Earnings
  - Key entities added: Mrs. B, GEICO, Washington Post, etc.
  - 1985 letter requires special handling (binary file issue)

### [14:00] Batch 2 Processing - 1988-1997 Letters (HTML)
- **Operation**: Processed second batch of 10 Buffett letters (1988-1997)
- **Read**: 10 HTML files successfully (1988-1997)
- **Created Source Pages**:
  - source-buffett-letters-1988.md - 市场先生深化，可口可乐投资，透视盈余
  - source-buffett-letters-1989.md - 透视盈余阐述，Borsheim's收购，零售业
  - source-buffett-letters-1990.md - 银行危机，富国银行投资，浮存金价值
  - source-buffett-letters-1991.md - 经济商誉，H.H. Brown收购，传媒业
  - source-buffett-letters-1992.md - 内在价值评估，安全边际，Lowell收购
  - source-buffett-letters-1993.md - Dexter收购，税务筹划，长期投资
  - source-buffett-letters-1994.md - 账面vs内在价值，Scott Fetzer案例
  - source-buffett-letters-1995.md - GEICO全资收购，Helzberg's与R.C. Willey
  - source-buffett-letters-1996.md - B类股票，FlightSafety收购，浮存金67亿
  - source-buffett-letters-1997.md - 市场波动理解，规模挑战，非传统投资
- **Created Entity Pages**:
  - （待补充：可口可乐、吉列、富国银行等entity页面）
- **Created Concept Pages**:
  - （待补充：透视盈余、经济商誉、安全边际等concept页面）
- **Updated**: wiki/index.md
- **Notes**:
  - All source pages created in Chinese Simplified
  - File names use English for URL compatibility
  - Key concepts: Look-Through Earnings, Economic Goodwill, Margin of Safety
  - Key entities: Coca-Cola, Gillette, Wells Fargo, GEICO全资收购
  - Important themes: 规模挑战、税务筹划、非传统投资
  - 1995年GEICO全资收购是里程碑事件

### [14:30] Batch 3 Processing - 2003-2012 Letters (PDF)
- **Operation**: Processed third batch of 10 Buffett letters (2003-2012)
- **PDF Extraction**: Successfully extracted text from 10 PDF files using Python script
  - 2003: 22 pages, 2004: 25 pages, 2005: 22 pages, 2006: 23 pages
  - 2007: 21 pages, 2008: 22 pages, 2009: 19 pages
  - 2010: 27 pages, 2011: 21 pages, 2012: 23 pages
- **Created Source Pages**:
  - source-buffett-letters-2003.md - Clayton收购，制造业住房
  - source-buffett-letters-2004.md - 锌项目失败，公用事业
  - source-buffett-letters-2005.md - 飓风损失，五项收购
  - source-buffett-letters-2006.md - 创记录年份，GEICO生产力
  - source-buffett-letters-2007.md - Marmon收购，双重价值衡量
  - source-buffett-letters-2008.md - 金融危机，投资错误
  - source-buffett-letters-2009.md - BNSF收购，逆向思维
  - source-buffett-letters-2010.md - BNSF成功，资本投资
  - source-buffett-letters-2011.md - Lubrizol收购，继任计划
  - source-buffett-letters-2012.md - Heinz收购，"五大"创纪录
- **Created Entity Pages**:
  - （待补充：Marmon、BNSF、Lubrizol、Heinz等entity页面）
- **Created Concept Pages**:
  - （待补充：双重价值衡量、财务实力、去中心化管理等concept页面）
- **Updated**: wiki/index.md
- **Notes**:
  - All source pages created in Chinese Simplified
  - File names use English for URL compatibility
  - Key concepts: Yardsticks, Financial Strength, Inversion, Per-Share Growth
  - Key entities: Marmon Group, BNSF, Lubrizol, Heinz, IBM
  - Important themes: 金融危机、继任计划、资本投资、美国乐观主义
  - 2009年BNSF收购是里程碑事件（最大现金收购）
  - 2008年是唯一净值减少年份

### [15:00] Batch 4 Processing - 2013-2022 Letters (PDF)
- **Operation**: Processed fourth batch of 10 Buffett letters (2013-2022)
- **PDF Extraction**: Successfully extracted text from 10 PDF files (2013-2022)
  - 2013: 23 pages, 2014: 42 pages, 2015: 30 pages, 2016: 28 pages
  - 2017: 16 pages, 2018: 14 pages, 2019: 13 pages
  - 2020: 14 pages, 2021: 11 pages, 2022: 10 pages
- **Created Source Pages**:
  - source-buffett-letters-2013.md - Heinz与3G合作，五大金刚，内在价值
  - source-buffett-letters-2014.md - 黄金周年，Duracell，BNSF改进
  - source-buffett-letters-2015.md - PCC收购，六大金刚，Kraft Heinz
  - source-buffett-letters-2016.md - 转型反思，Dexter Shoe错误，美国奇迹
  - source-buffett-letters-2017.md - 税改290亿，GAAP扭曲，Pilot Flying J
  - source-buffett-letters-2018.md - 告别账面价值，森林比喻，管理层改革
  - source-buffett-letters-2019.md - 留存收益力量，可口可乐美国运通
  - source-buffett-letters-2020.md - PCC错误坦承，企业集团差异
  - source-buffett-letters-2021.md - 基础设施资产，业务选择者
  - source-buffett-letters-2022.md - 秘密武器，市场愚蠢价格
- **Created Entity Pages**:
  - （待补充：3G Capital、PCC、Pilot Flying J等entity页面）
- **Created Concept Pages**:
  - （待补充：留存收益、森林林分、秘密武器等concept页面）
- **Updated**: wiki/index.md
- **Notes**:
  - All source pages created in Chinese Simplified
  - File names use English for URL compatibility
  - Key concepts: Retained Earnings, Secret Sauce, Business-Pickers
  - Key entities: 3G Capital, Precision Castparts, Pilot Flying J, HomeServices
  - Important themes: 税制改革、管理层继任、GAAP扭曲、留存收益
  - 2015年PCC收购（320亿美元）是里程碑事件
  - 2017年税改带来290亿美元一次性收益
  - 2020年PCC减值110亿美元（巴菲特承认错误）

### [15:30] Batch 5 Processing - 2023-2025 Letters (PDF)
- **Operation**: Processed fifth and final batch of 3 Buffett letters (2023-2025)
- **PDF Extraction**: Successfully extracted text from 3 PDF files
  - 2023: 16 pages, 2024: 15 pages, 2025: 20 pages
- **Created Source Pages**:
  - source-buffett-letters-2023.md - Charlie Munger致敬，建筑师vs承包商，Bertie模型
  - source-buffett-letters-2024.md - 税收记录268亿，Pete Liegl致敬，Greg Abel继任
  - source-buffett-letters-2025.md - Greg Abel首信，文化价值观，OxyChem与Bell Labs
- **Created Entity Pages**:
  - （待补充：Charlie Munger、Bertie、Pete Liegl、Greg Abel等entity页面）
- **Created Concept Pages**:
  - （待补充：建筑师vs承包商、终身股东、错误文化、文化价值观等concept页面）
- **Updated**: wiki/index.md
- **Notes**:
  - All source pages created in Chinese Simplified
  - File names use English for URL compatibility
  - 2023年是Charlie Munger去世年（11月28日，接近100岁生日）
  - 2024年创造美国企业税收记录（268亿美元）
  - 2025年是Greg Abel首封CEO信件，系统阐述五大基础价值观
  - 1977-2025年（除1985年外）共44封信件全部处理完成
  - 所有5个批次均成功完成

### [21:59] Ingest - Wesco Financial 1997 Letter (Munger)
- **Operation**: Ingested Charlie Munger's Wesco Financial Corporation 1997 Letter to Shareholders
- **Source File**: raw/books/pdf/cm1997.pdf
- **Created Source Pages**:
  - source-wesco-letter-1997.md - 芒格撰写的Wesco股东信，超级巨灾再保险、内在价值估算、可转换优先股
- **Created Entity Pages**:
  - entity-charlie-munger.md - 查理·芒格，伯克希尔副董事长，Wesco董事长
  - entity-wesco-financial.md - Wesco Financial Corporation，伯克希尔持股80%
  - Updated: entity-kansas-bankers-surety.md - 补充1996年收购详情和财务表现
- **Created Concept Pages**:
  - concept-super-cat-reinsurance.md - 超级巨灾再保险，需要堡垒级资产负债表
  - Updated: concept-intrinsic-value.md - 添加芒格估算法（清算价值+递延税优势）
- **Updated**: wiki/index.md
- **Notes**:
  - 芒格以坦诚著称，公开承认Wesco质量不如伯克希尔
  - 提供了独特的内在价值估算方法：清算价值 + 递延税优势价值
  - 详细阐述了超级巨灾再保险的业务逻辑
  - 展示了可转换优先股投资的成功案例（Gillette、Salomon→Travelers）

---

## 2026-04-10

### [Ingest] 演讲文档 - The Superinvestors of Graham-and-Doddsville
- **Action**: Ingest
- **Source**: 网络搜索（哥伦比亚大学官网）
- **文档判断**: 类型=speech, 人物=buffett, 年份=1984, slug=columbia
- **Created**:
  - docs/people/buffett/source-buffett-speech-1984-columbia.md
- **Updated**:
  - docs/people/buffett/index.md（添加"演讲与文章"分类）
- **Notes**:
  - 测试 1：验证 speech 类型的新文档处理流程
  - 文件命名符合新规范 `source-{person}-{type}-{year}-{slug}.md`
  - 文件直接放在 `docs/people/buffett/` 下，无 letters 子目录
  - YAML frontmatter 包含 source 字段指向原始链接

### [Ingest] 文章文档 - Buy American. I Am.
- **Action**: Ingest
- **Source**: CNBC / 纽约时报（2008-10-17）
- **文档判断**: 类型=article, 人物=buffett, 年份=2008, slug=nytimes
- **Created**:
  - docs/people/buffett/source-buffett-article-2008-nytimes.md
- **Updated**:
  - docs/people/buffett/index.md（添加文章到"演讲与文章"列表）
- **Notes**:
  - 测试 2：验证 article 类型的新文档处理流程
  - 2008年全球金融危机期间发表的专栏文章
  - article 类型判断正确（报纸专栏特征）

