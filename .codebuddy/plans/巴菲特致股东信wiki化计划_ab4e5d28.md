---
name: 巴菲特致股东信wiki化计划
overview: 将44封巴菲特致股东信（1977-2025年，缺1998-2002）分批处理，每批10封，创建中文wiki内容，提取实体和概念，建立知识网络
todos:
  - id: batch-1-1978-1987
    content: 处理第1批：读取1978-1987年HTML信件，创建10个中文source页面及相关entity/concept页面，更新索引和日志
    status: completed
  - id: batch-2-1988-1997
    content: 处理第2批：读取1988-1997年HTML信件，创建10个中文source页面及相关entity/concept页面，更新索引和日志
    status: completed
    dependencies:
      - batch-1-1978-1987
  - id: batch-3-2003-2012
    content: 处理第3批：使用[skill:pdf]读取2003-2012年PDF信件，创建10个中文source页面及相关entity/concept页面，更新索引和日志
    status: completed
    dependencies:
      - batch-2-1988-1997
  - id: batch-4-2013-2022
    content: 处理第4批：使用[skill:pdf]读取2013-2022年PDF信件，创建10个中文source页面及相关entity/concept页面，更新索引和日志
    status: completed
    dependencies:
      - batch-3-2003-2012
  - id: batch-5-2023-2025
    content: 处理第5批：使用[skill:pdf]读取2023-2025年PDF信件，创建3个中文source页面及相关entity/concept页面，更新索引和日志
    status: completed
    dependencies:
      - batch-4-2013-2022
  - id: update-1977-chinese
    content: 将1977年已有英文source页面转为中文版本，保持内容一致性
    status: completed
    dependencies:
      - batch-5-2023-2025
  - id: final-health-check
    content: 执行wiki健康检查：验证所有链接有效、无孤立页面、内容完整
    status: completed
    dependencies:
      - update-1977-chinese
---

## 产品概述

将巴菲特致股东信（1977-2025，共44封）批量处理成中文简体的wiki知识库内容

## 核心功能

- 每批次处理10封信件，共5个批次
- 为每封信创建中文source页面（遵循source.md模板结构）
- 提取并创建entity页面（人物、公司、机构等）
- 提取并创建concept页面（投资理念、商业原则、估值方法等）
- 建立双向链接关系
- 更新wiki/index.md索引
- 记录操作日志到wiki/log.md

## 信件资源分布

- HTML格式：1977-1997（21封）
- PDF格式：2003-2025（23封）
- 缺失年份：1998-2002（5年无信件）
- 已处理：1977年（英文版，需考虑是否转为中文）

## 批次计划

1. 第1批：1978-1987（10封HTML）
2. 第2批：1988-1997（10封HTML）
3. 第3批：2003-2012（10封PDF）
4. 第4批：2013-2022（10封PDF）
5. 第5批：2023-2025（3封PDF）

## 技术方案

### 处理流程

每批次执行以下步骤：

1. **读取原文**：批量读取10封信件内容（HTML或PDF格式）
2. **创建source页面**：为每封信创建`wiki/sources/source-buffett-letters-[年份].md`，使用source.md模板结构，内容全部使用中文简体
3. **提取实体**：识别信中提到的人物、公司、机构，创建或更新`wiki/entities/entity-[名称].md`
4. **提取概念**：识别投资理念、商业原则、估值方法等，创建或更新`wiki/concepts/concept-[名称].md`
5. **建立链接**：使用`[[]]`格式建立双向链接关系
6. **更新索引**：更新`wiki/index.md`，添加新页面条目
7. **记录日志**：在`wiki/log.md`中记录批次处理信息

### 文件命名规范

- source页面：`source-buffett-letters-[年份].md`（如：source-buffett-letters-1978.md）
- entity页面：`entity-[英文名].md`（如：entity-berkshire-hathaway.md）
- concept页面：`concept-[英文名].md`（如：concept-value-investing.md）

### 内容语言要求

- wiki正文内容：全部使用**中文简体**
- 文件名：使用英文（符合URL兼容要求）
- 链接ID：使用英文文件名

### 目录结构

```
wiki/
├── index.md                 # [更新] 添加新页面条目
├── log.md                   # [更新] 记录操作日志
├── sources/                 # [新增] 信件source页面
│   ├── source-buffett-letters-1978.md
│   ├── source-buffett-letters-1979.md
│   └── ...                  # 共43个新文件
├── entities/                # [更新] 添加新实体页面
│   └── entity-xxx.md        # 按需创建
├── concepts/                # [更新] 添加新概念页面
│   └── concept-xxx.md       # 按需创建
└── synthesis/               # [可选] 综合分析页面
```

### 模板应用

严格遵循`templates/`目录下的模板结构：

- source页面：使用`templates/source.md`结构
- entity页面：使用`templates/entity.md`结构
- concept页面：使用`templates/concept.md`结构

## Agent Extensions

### Skill

- **pdf**
- Purpose: 读取和处理PDF格式的巴菲特信件（2003-2025年共23封）
- Expected outcome: 成功提取PDF信件的文本内容用于wiki生成

### SubAgent

- **code-explorer**
- Purpose: 在需要查找现有entity或concept页面时快速搜索wiki目录
- Expected outcome: 确认实体或概念是否已存在，避免重复创建