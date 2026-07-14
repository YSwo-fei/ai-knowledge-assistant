from __future__ import annotations

from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED


OUTPUT = Path("后续学习路线图_详细版.docx")


def xml_escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def paragraph(text: str, style: str | None = None) -> str:
    escaped = xml_escape(text)
    style_xml = f"<w:pPr><w:pStyle w:val=\"{style}\"/></w:pPr>" if style else ""
    return (
        "<w:p>"
        f"{style_xml}"
        "<w:r><w:rPr><w:rFonts w:ascii=\"Calibri\" w:eastAsia=\"宋体\"/>"
        "<w:sz w:val=\"24\"/></w:rPr>"
        f"<w:t xml:space=\"preserve\">{escaped}</w:t></w:r></w:p>"
    )


def build_document_xml(lines: list[tuple[str | None, str]]) -> str:
    body = []
    for style, text in lines:
        body.append(paragraph(text, style))
    sect = (
        "<w:sectPr>"
        "<w:pgSz w:w=\"11906\" w:h=\"16838\"/>"
        "<w:pgMar w:top=\"1440\" w:right=\"1440\" w:bottom=\"1440\" w:left=\"1440\" "
        "w:header=\"708\" w:footer=\"708\" w:gutter=\"0\"/>"
        "</w:sectPr>"
    )
    return (
        "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
        "<w:document xmlns:wpc=\"http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas\" "
        "xmlns:mc=\"http://schemas.openxmlformats.org/markup-compatibility/2006\" "
        "xmlns:o=\"urn:schemas-microsoft-com:office:office\" "
        "xmlns:r=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships\" "
        "xmlns:m=\"http://schemas.openxmlformats.org/officeDocument/2006/math\" "
        "xmlns:v=\"urn:schemas-microsoft-com:vml\" "
        "xmlns:wp14=\"http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing\" "
        "xmlns:wp=\"http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing\" "
        "xmlns:w10=\"urn:schemas-microsoft-com:office:word\" "
        "xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\" "
        "xmlns:w14=\"http://schemas.microsoft.com/office/word/2010/wordml\" "
        "xmlns:wpg=\"http://schemas.microsoft.com/office/word/2010/wordprocessingGroup\" "
        "xmlns:wpi=\"http://schemas.microsoft.com/office/word/2010/wordprocessingInk\" "
        "xmlns:wne=\"http://schemas.microsoft.com/office/word/2006/wordml\" "
        "xmlns:wps=\"http://schemas.microsoft.com/office/word/2010/wordprocessingShape\" "
        "mc:Ignorable=\"w14 wp14\">"
        f"<w:body>{''.join(body)}{sect}</w:body></w:document>"
    )


CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>
"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>
"""

DOC_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>
"""

STYLES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal"/>
    <w:qFormat/>
    <w:rPr>
      <w:rFonts w:ascii="Calibri" w:eastAsia="宋体"/>
      <w:sz w:val="24"/>
    </w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Title">
    <w:name w:val="Title"/>
    <w:basedOn w:val="Normal"/>
    <w:qFormat/>
    <w:rPr>
      <w:rFonts w:ascii="Calibri" w:eastAsia="黑体"/>
      <w:b/>
      <w:sz w:val="36"/>
    </w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading1">
    <w:name w:val="heading 1"/>
    <w:basedOn w:val="Normal"/>
    <w:qFormat/>
    <w:rPr>
      <w:rFonts w:ascii="Calibri" w:eastAsia="黑体"/>
      <w:b/>
      <w:sz w:val="30"/>
    </w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading2">
    <w:name w:val="heading 2"/>
    <w:basedOn w:val="Normal"/>
    <w:qFormat/>
    <w:rPr>
      <w:rFonts w:ascii="Calibri" w:eastAsia="黑体"/>
      <w:b/>
      <w:sz w:val="26"/>
    </w:rPr>
  </w:style>
</w:styles>
"""

CORE = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>后续学习路线图</dc:title>
  <dc:creator>Codex</dc:creator>
  <cp:lastModifiedBy>Codex</cp:lastModifiedBy>
</cp:coreProperties>
"""

APP = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Microsoft Office Word</Application>
</Properties>
"""


def build_lines() -> list[tuple[str | None, str]]:
    lines: list[tuple[str | None, str]] = []
    add = lines.append

    add(("Title", "后续学习路线图（详细版）"))
    add((None, "适用对象：当前处于 Python、FastAPI、数据库、AI 应用入门阶段的学习者。"))
    add((None, "核心目标：在基础打稳后，逐步完成 AI 全栈、RAG、部署上线、模型微调与求职包装的完整成长路径。"))

    add(("Heading1", "一、总学习目标"))
    add((None, "最终目标不是单点掌握某个库，而是形成完整能力：能独立完成一个可以上线、可以演示、可以写进简历的 AI 应用项目，并能解释其中的技术设计。"))
    add((None, "最终希望具备四类能力：第一，编码能力；第二，系统设计能力；第三，部署与交付能力；第四，项目表达与求职能力。"))

    add(("Heading1", "二、整体阶段规划"))
    add((None, "建议将后续学习分为八个阶段推进：1. Python 与 Web 基础强化；2. 数据库与数据库强化；3. FastAPI 后端工程化；4. RAG 核心能力；5. 前端与产品交互；6. Docker 与部署；7. 大模型微调与进阶 AI 工程；8. 项目包装与求职准备。"))

    add(("Heading1", "三、阶段一：Python 与 Web 基础强化"))
    add(("Heading2", "目标"))
    add((None, "把当前能看懂、能跟着写的状态，提升到能自己写出中小型后端逻辑。"))
    add(("Heading2", "重点内容"))
    add((None, "1. Python 基础再强化：函数、类、模块、异常处理、文件操作、列表推导式、字典操作。"))
    add((None, "2. 面向对象基础：类、对象、实例属性、方法、继承。"))
    add((None, "3. Web 基础：HTTP 请求与响应、状态码、JSON、GET 与 POST、接口调试。"))
    add((None, "4. 调试能力：看懂 Traceback、定位报错行、分清语法错误、导入错误、类型错误。"))
    add(("Heading2", "验收标准"))
    add((None, "能够独立写出一个包含多个接口的小型 FastAPI 服务；看到报错时能自己定位到大致模块。"))
    add(("Heading2", "实例"))
    add((None, "示例项目：待办事项 API。要求支持新增任务、查看任务列表、标记完成、删除任务。这个项目虽然小，但能把路由、请求体、响应、列表操作、文件读写串起来。"))

    add(("Heading1", "四、阶段二：数据库与数据库强化"))
    add(("Heading2", "目标"))
    add((None, "不再只是会照着写 SQLAlchemy，而是真正理解数据库设计、增删改查、关系建模和项目中的数据流。"))
    add(("Heading2", "基础数据库内容"))
    add((None, "1. 核心概念：表、行、列、主键、外键、索引、约束、事务。"))
    add((None, "2. SQL 基础：CREATE TABLE、INSERT、SELECT、UPDATE、DELETE、WHERE、ORDER BY、LIMIT、COUNT、GROUP BY。"))
    add((None, "3. SQLite 入门：单文件数据库，适合作为第一个项目的持久化方案。"))
    add((None, "4. ORM 理解：为什么有 SQLAlchemy，它如何把表映射成类，把一行记录映射成对象。"))
    add(("Heading2", "数据库强化内容"))
    add((None, "1. 表设计能力：什么字段必须有、什么字段可以为空、默认值如何设置、时间字段如何统一。"))
    add((None, "2. 关系设计：一对多、多对一、多对多。"))
    add((None, "3. 查询强化：模糊查询、分页、排序、聚合统计。"))
    add((None, "4. 工程实践：如何在 FastAPI 中安全管理 Session，为什么要 commit、refresh、close。"))
    add(("Heading2", "验收标准"))
    add((None, "能够独立设计文档表、聊天记录表、会话表；能解释请求模型和数据库模型的区别；能写出完整 CRUD。"))
    add(("Heading2", "实例"))
    add((None, "实例一：文档表 documents。字段包括 id、title、content、file_type、file_size、created_at。"))
    add((None, "实例二：聊天记录表 chat_messages。字段包括 id、session_id、role、content、created_at。"))
    add((None, "实例三：会话表 sessions。字段包括 id、title、created_at。之后通过 session_id 将聊天记录关联到会话。"))

    add(("Heading1", "五、阶段三：FastAPI 后端工程化"))
    add(("Heading2", "目标"))
    add((None, "从会写几个接口，提升到能组织一个后端项目。"))
    add(("Heading2", "重点内容"))
    add((None, "1. 项目结构：main、schemas、models、database、routers、services。"))
    add((None, "2. 请求与响应分层：请求模型、响应模型、数据库模型分开。"))
    add((None, "3. 文件上传：接收 txt、pdf、docx。"))
    add((None, "4. 错误处理：400、404、422、500 的区别。"))
    add((None, "5. 配置管理：.env、环境变量、敏感信息隔离。"))
    add((None, "6. 日志与调试：基础日志输出、请求排错。"))
    add(("Heading2", "验收标准"))
    add((None, "能完成一个结构清晰的 FastAPI 项目，包含文档上传、文档列表、文档详情、聊天接口。"))
    add(("Heading2", "实例"))
    add((None, "示例：将当前练习版 main.py 重构为可维护结构。比如将 /api/documents 路由拆到单独模块，将数据库读写逻辑放到 service 层。"))

    add(("Heading1", "六、阶段四：RAG 核心能力"))
    add(("Heading2", "目标"))
    add((None, "完成 AI 知识库项目的核心价值：让模型基于用户上传的文档回答问题，而不是空想。"))
    add(("Heading2", "重点内容"))
    add((None, "1. 文档解析：txt、pdf、docx 内容抽取。"))
    add((None, "2. 文本切块：chunk size、chunk overlap、按段落和句子优先切分。"))
    add((None, "3. Embedding：把文本转成向量。"))
    add((None, "4. 向量数据库：ChromaDB 入门。"))
    add((None, "5. 检索：相似度搜索、Top K 返回。"))
    add((None, "6. Prompt 组装：把检索片段和用户问题拼给大模型。"))
    add((None, "7. 溯源：答案后面标明来源文档。"))
    add(("Heading2", "强化方向"))
    add((None, "1. 分块优化：递归切分、重叠窗口。"))
    add((None, "2. 检索优化：向量召回加 rerank。"))
    add((None, "3. 混合检索：BM25 加向量检索。"))
    add((None, "4. 多轮问答：让问题理解上下文。"))
    add(("Heading2", "验收标准"))
    add((None, "用户上传 2 到 3 篇文档后，系统能根据文档内容回答问题，并给出引用来源。"))
    add(("Heading2", "实例"))
    add((None, "示例问题：用户上传《Python 学习笔记》和《SQL 入门》后，提问“Python 列表和 SQL 表有什么相似点？”。系统应先检索文档片段，再生成基于文档的回答。"))

    add(("Heading1", "七、阶段五：前端与产品交互"))
    add(("Heading2", "目标"))
    add((None, "把一个只有接口的后端项目，变成用户可见、可用、可演示的产品。"))
    add(("Heading2", "可选路线"))
    add((None, "路线 A：继续走 Streamlit，开发快，适合快速上线和演示。"))
    add((None, "路线 B：学习基础前端或 Vue，做更完整的前后端分离。"))
    add(("Heading2", "重点内容"))
    add((None, "1. 上传文档页面。"))
    add((None, "2. 聊天问答页面。"))
    add((None, "3. 历史记录显示。"))
    add((None, "4. 错误提示、加载状态、空状态设计。"))
    add((None, "5. 基础 UI 规范与交互体验。"))
    add(("Heading2", "验收标准"))
    add((None, "能在浏览器中完成上传文档、提问、查看回答、查看来源。"))

    add(("Heading1", "八、阶段六：Docker 与部署"))
    add(("Heading2", "目标"))
    add((None, "把“只能在你电脑上跑”的项目，升级成“别人也能启动和访问”的项目。"))
    add(("Heading2", "Docker 基础"))
    add((None, "1. 镜像是什么：项目的可打包运行环境。"))
    add((None, "2. 容器是什么：镜像运行起来的实例。"))
    add((None, "3. Dockerfile 是什么：如何把项目打包成镜像。"))
    add((None, "4. docker-compose 是什么：如何同时启动后端、数据库、向量库等多个服务。"))
    add(("Heading2", "部署内容"))
    add((None, "1. 本地容器化。"))
    add((None, "2. 云服务器部署。"))
    add((None, "3. 环境变量配置。"))
    add((None, "4. 端口映射。"))
    add((None, "5. 基础日志查看和重启。"))
    add(("Heading2", "验收标准"))
    add((None, "别人拿到仓库后，能用统一命令启动项目；或项目能够在云端公网访问。"))
    add(("Heading2", "实例"))
    add((None, "示例：为 FastAPI + SQLite + ChromaDB + Streamlit 组合写出 Dockerfile 和 docker-compose.yml。即使初期不用全套，也要理解为什么要这样做。"))

    add(("Heading1", "九、阶段七：大模型微调与进阶 AI 工程"))
    add(("Heading2", "目标"))
    add((None, "理解什么时候应该用提示工程，什么时候应该做微调，什么时候应该做 RAG。"))
    add(("Heading2", "重点内容"))
    add((None, "1. 提示工程：通过 prompt 改善输出。"))
    add((None, "2. RAG：让模型基于外部知识回答。"))
    add((None, "3. 微调：让模型在某个风格、任务、格式上更稳定。"))
    add((None, "4. Function Calling / Tool Use：让模型学会调用工具。"))
    add(("Heading2", "微调学习要点"))
    add((None, "1. 什么情况下适合微调：固定输出格式、特定领域风格、稳定问答模板。"))
    add((None, "2. 什么情况下不适合微调：只是想让模型知道新知识，这通常更适合 RAG。"))
    add((None, "3. 微调流程：准备数据集、构造指令对、选择基础模型、训练、评估。"))
    add((None, "4. 常见技术关键词：LoRA、QLoRA、SFT、对话数据集、验证集。"))
    add(("Heading2", "实例"))
    add((None, "示例一：将若干条客服问答整理成 instruction-response 数据，用于让模型更稳定地输出“客服风格”回复。"))
    add((None, "示例二：把招聘问答数据做成小型数据集，训练一个更符合简历辅导风格的模型。"))
    add(("Heading2", "验收标准"))
    add((None, "不要求你立刻自己训练一个大型模型，但要能清楚区分“微调”和“RAG”的边界，并能说出一个适合做微调的真实场景。"))

    add(("Heading1", "十、阶段八：工程化强化与性能意识"))
    add(("Heading2", "目标"))
    add((None, "从“能跑”提升到“更稳、更清晰、更像真实项目”。"))
    add(("Heading2", "内容"))
    add((None, "1. 配置分层：开发环境、生产环境。"))
    add((None, "2. 依赖管理：requirements.txt、虚拟环境。"))
    add((None, "3. 代码结构清理：文件命名、模块职责、重复逻辑抽离。"))
    add((None, "4. 简单测试：接口测试、关键逻辑测试。"))
    add((None, "5. 安全意识：API Key 管理、敏感信息不上 GitHub。"))
    add((None, "6. 基础性能意识：为什么分页、为什么限制返回条数、为什么缓存有时有用。"))

    add(("Heading1", "十一、阶段九：项目包装与求职准备"))
    add(("Heading2", "目标"))
    add((None, "把做出来的项目，转化成能打动面试官的作品。"))
    add(("Heading2", "重点内容"))
    add((None, "1. README 编写：项目介绍、技术栈、运行步骤、截图、架构图。"))
    add((None, "2. 演示准备：录制上传文档、提问、查看答案来源的完整流程。"))
    add((None, "3. 简历描述：突出你解决了什么问题，而不是只堆技术名词。"))
    add((None, "4. 面试表达：能说清楚为什么用 FastAPI、为什么用 SQLite、为什么后来要上 Docker、为什么 RAG 比纯对话更适合知识库。"))
    add(("Heading2", "实例"))
    add((None, "简历表述示例：独立完成基于 FastAPI 与 ChromaDB 的 RAG 知识库系统，实现文档上传、语义检索、来源溯源与对话式问答，并完成容器化部署。"))

    add(("Heading1", "十二、建议学习顺序"))
    add((None, "建议你不要并行学太多，而是按这个顺序推进："))
    add((None, "第一步：Python、FastAPI、请求与响应、接口调试。"))
    add((None, "第二步：数据库基础与 SQLAlchemy。"))
    add((None, "第三步：真正完成文档 CRUD。"))
    add((None, "第四步：做文档上传与解析。"))
    add((None, "第五步：做 RAG。"))
    add((None, "第六步：做前端与产品演示。"))
    add((None, "第七步：Docker 和部署。"))
    add((None, "第八步：数据库强化、检索优化、微调与进阶路线。"))

    add(("Heading1", "十三、每个阶段的最小交付物"))
    add((None, "阶段一交付物：一个可运行的 FastAPI 小项目。"))
    add((None, "阶段二交付物：一个真正连上 SQLite 的文档 CRUD。"))
    add((None, "阶段三交付物：一个结构清晰的后端骨架。"))
    add((None, "阶段四交付物：一个可用的 RAG 问答链路。"))
    add((None, "阶段五交付物：一个能演示的 Web 界面。"))
    add((None, "阶段六交付物：一个能部署的容器化项目。"))
    add((None, "阶段七交付物：对微调与 RAG 边界的明确认知，以及至少一个微调实验方案。"))
    add((None, "阶段八交付物：一份能写进简历、能在面试中讲出来的项目成果。"))

    add(("Heading1", "十四、你当前最该做什么"))
    add((None, "你当前不该同时冲 Docker、微调、RAG 深化、前端框架这些大块，因为这样会在每一层都卡住。"))
    add((None, "你当前最应该做的，是把基础主线先彻底打通：FastAPI 接口 -> Pydantic 请求模型 -> SQLAlchemy 数据库模型 -> SQLite 持久化。"))
    add((None, "只要这条线打通，后面的文档上传、RAG、部署都会顺很多。"))

    add(("Heading1", "十五、一句话总目标"))
    add((None, "后续学习的总方向，不是成为单点工具使用者，而是成为一个能独立交付 AI 应用项目、能讲清技术设计、能拿项目找工作的开发者。"))

    return lines


def main():
    document_xml = build_document_xml(build_lines())
    with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", CONTENT_TYPES)
        docx.writestr("_rels/.rels", RELS)
        docx.writestr("word/document.xml", document_xml)
        docx.writestr("word/_rels/document.xml.rels", DOC_RELS)
        docx.writestr("word/styles.xml", STYLES)
        docx.writestr("docProps/core.xml", CORE)
        docx.writestr("docProps/app.xml", APP)

    print(f"已生成: {OUTPUT.resolve()}")


if __name__ == "__main__":
    main()
