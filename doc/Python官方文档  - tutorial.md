<!-- TOC -->

- [1. 勾起你的欲望 (Whetting Your Appetite)](#1-勾起你的欲望-whetting-your-appetite)
- [2. 使用PYthon解释器 (Using the Python Interpreter)](#2-使用python解释器-using-the-python-interpreter)
    - [2.1. 调用解释器 (Invoking the Interpreter)](#21-调用解释器-invoking-the-interpreter)
        - [2.1.1. 参数传递 (Argument Passing)](#211-参数传递-argument-passing)
        - [2.1.2. 交互模式 (Interactive Mode)](#212-交互模式-interactive-mode)
    - [2.2. 解释器及其环境(The Interpreter and Its Environment)](#22-解释器及其环境the-interpreter-and-its-environment)
        - [2.2.1. 源代码编码(Source Code Encoding)](#221-源代码编码source-code-encoding)
- [3. PY 的非正式介绍(An Informal Introduction to Python)](#3-py-的非正式介绍an-informal-introduction-to-python)
    - [3.1. PY作为计算器？(Using Python as a Calculator)](#31-py作为计算器using-python-as-a-calculator)
        - [3.1.1. 数字 (Numbers)](#311-数字-numbers)
        - [3.1.2. 字符 (Strings)](#312-字符-strings)
        - [3.1.3. 列表 (Lists)](#313-列表-lists)
    - [3.2. 编程的第一步 (First Steps Towards Programming)](#32-编程的第一步-first-steps-towards-programming)
- [4. 更多控制流工具 (More Control Flow Tools)](#4-更多控制流工具-more-control-flow-tools)
    - [4.1. if 语句(if Statements)](#41-if-语句if-statements)
    - [4.2. for 语句(for Statements)](#42-for-语句for-statements)
    - [4.3. range() 函数 (The range() Function)](#43-range-函数-the-range-function)
    - [4.4. break、continue、else(break and continue Statements, and else Clauses on Loops)](#44-breakcontinueelsebreak-and-continue-statements-and-else-clauses-on-loops)
    - [4.5. pass 语句(pass Statements)](#45-pass-语句pass-statements)
    - [4.6. 定义函数(Defining Functions)](#46-定义函数defining-functions)
    - [4.7. 更多关于定义函数的内容(More on Defining Functions)](#47-更多关于定义函数的内容more-on-defining-functions)
        - [4.7.1. 默认参数 (Default Argument Values)](#471-默认参数-default-argument-values)
        - [4.7.2. 关键字参数 (Keyword Arguments)](#472-关键字参数-keyword-arguments)
        - [4.7.3. 任意的参数列表 (Arbitrary Argument Lists)](#473-任意的参数列表-arbitrary-argument-lists)
        - [4.7.4. 拆包参数列表 (Unpacking Argument Lists)](#474-拆包参数列表-unpacking-argument-lists)
        - [4.7.5. lambda 表达式(Lambda Expressions)](#475-lambda-表达式lambda-expressions)
        - [4.7.6. 文档字符串 (Documentation Strings)](#476-文档字符串-documentation-strings)
        - [4.7.7. 函数注释 (Function Annotations)](#477-函数注释-function-annotations)
    - [4.8. 代码风格 (Intermezzo: Coding Style)](#48-代码风格-intermezzo-coding-style)
- [5. 数据结构 (Data Structures)](#5-数据结构-data-structures)
    - [5.1. 更多关于列表(More on Lists)](#51-更多关于列表more-on-lists)
        - [5.1.1. 使用列表作为堆栈 (Using Lists as Stacks)](#511-使用列表作为堆栈-using-lists-as-stacks)
        - [5.1.2. 使用列表作为小弟队列 (Using Lists as Queues)](#512-使用列表作为小弟队列-using-lists-as-queues)
        - [5.1.3. 列表理解 (List Comprehensions)](#513-列表理解-list-comprehensions)
        - [5.1.4. 嵌套列表理解 (Nested List Comprehensions)](#514-嵌套列表理解-nested-list-comprehensions)
    - [5.2. del 语句(The del statement)](#52-del-语句the-del-statement)
    - [5.3. 元组和序列 (Tuples and Sequences)](#53-元组和序列-tuples-and-sequences)
    - [5.4. 集合 (Sets)](#54-集合-sets)
    - [5.5. 字典 (Dictionaries)](#55-字典-dictionaries)
    - [5.6. 循环技术 (Looping Techniques)](#56-循环技术-looping-techniques)
    - [5.7. 更多条件 (More on Conditions)](#57-更多条件-more-on-conditions)
    - [5.8. 比较序列和其他类型 (Comparing Sequences and Other Types)](#58-比较序列和其他类型-comparing-sequences-and-other-types)
- [6. 模块 (Modules)](#6-模块-modules)
    - [6.1. 关于更多模块 (More on Modules)](#61-关于更多模块-more-on-modules)
        - [6.1.1. 将模块作为脚本执行(Executing modules as scripts)](#611-将模块作为脚本执行executing-modules-as-scripts)
        - [6.1.2. 模块搜索路径 (The Module Search Path)](#612-模块搜索路径-the-module-search-path)
        - [6.1.3. 编译 PY 文件 (“Compiled” Python files)](#613-编译-py-文件-compiled-python-files)
    - [6.2. 标准模块 (Standard Modules)](#62-标准模块-standard-modules)
    - [6.3. dir() 函数(The dir() Function)](#63-dir-函数the-dir-function)
    - [6.4. 包 (Packages)](#64-包-packages)
        - [6.4.1. 从包中导入* (Importing * From a Package)](#641-从包中导入-importing--from-a-package)
        - [6.4.2. 引用intra包 (Intra-package References)](#642-引用intra包-intra-package-references)
        - [6.4.3. 多个目录中的包 (Packages in Multiple Directories)](#643-多个目录中的包-packages-in-multiple-directories)
- [7. 输入和输出 (Input and Output)](#7-输入和输出-input-and-output)
    - [7.1. fancier 输出格式 (Fancier Output Formatting)](#71-fancier-输出格式-fancier-output-formatting)
        - [7.1.1. 格式化字符串 (Formatted String Literals)](#711-格式化字符串-formatted-string-literals)
        - [7.1.2. 字符串 format() 方法 (The String format() Method)](#712-字符串-format-方法-the-string-format-method)
        - [7.1.3. 手动字符串格式 (Manual String Formatting)](#713-手动字符串格式-manual-string-formatting)
        - [7.1.4. 旧的字符串格式 (Old string formatting)](#714-旧的字符串格式-old-string-formatting)
    - [7.2. 读写文件 (Reading and Writing Files)](#72-读写文件-reading-and-writing-files)
        - [7.2.1. 文件对象的方法 (Methods of File Objects)](#721-文件对象的方法-methods-of-file-objects)
        - [7.2.2. 用json保存结构化数据 (Saving structured data with json)](#722-用json保存结构化数据-saving-structured-data-with-json)
- [8. 错误和异常 (Errors and Exceptions)](#8-错误和异常-errors-and-exceptions)
    - [8.1. 语法错误 (Syntax Errors)](#81-语法错误-syntax-errors)
    - [8.2. 异常 (Exceptions)](#82-异常-exceptions)
    - [8.3. 处理异常 (Handling Exceptions)](#83-处理异常-handling-exceptions)
    - [8.4. 抛出异常 (Raising Exceptions)](#84-抛出异常-raising-exceptions)
    - [8.5. 用户自定义异常 (User-defined Exceptions)](#85-用户自定义异常-user-defined-exceptions)
    - [8.6. 定义清理动作？ (Defining Clean-up Actions)](#86-定义清理动作-defining-clean-up-actions)
    - [8.7. 预定义的清理动作 (Predefined Clean-up Actions)](#87-预定义的清理动作-predefined-clean-up-actions)
- [9. 类 (Classes)](#9-类-classes)
    - [9.1. 关于名字和物体的一个单词 (A Word About Names and Objects)](#91-关于名字和物体的一个单词-a-word-about-names-and-objects)
    - [9.2. 作用域和命名空间 (Python Scopes and Namespaces)](#92-作用域和命名空间-python-scopes-and-namespaces)
        - [9.2.1. 作用域和命名空间例子 (Scopes and Namespaces Example)](#921-作用域和命名空间例子-scopes-and-namespaces-example)
    - [9.3. 第一眼看到的类 (A First Look at Classes)](#93-第一眼看到的类-a-first-look-at-classes)
        - [9.3.1. 类定义语法 (Class Definition Syntax)](#931-类定义语法-class-definition-syntax)
        - [9.3.2. 类对象 (Class Objects)](#932-类对象-class-objects)
        - [9.3.3. 实例对象 (Instance Objects)](#933-实例对象-instance-objects)
        - [9.3.4. 对象方法 (Method Objects)](#934-对象方法-method-objects)
        - [9.3.5. 类变量 与 实例变量(Class and Instance Variables)](#935-类变量-与-实例变量class-and-instance-variables)
    - [9.4. 随机备注 (Random Remarks)](#94-随机备注-random-remarks)
    - [9.5. 继承 (Inheritance)](#95-继承-inheritance)
        - [9.5.1. 多重继承 (Multiple Inheritance)](#951-多重继承-multiple-inheritance)
    - [9.6. 私有变量 (Private Variables)](#96-私有变量-private-variables)
    - [9.7. 零碎的知识 (Odds and Ends)](#97-零碎的知识-odds-and-ends)
    - [9.8. 迭代器 (Iterators)](#98-迭代器-iterators)
    - [9.9. 生成器 (Generators)](#99-生成器-generators)
    - [9.10. 生成器表达式 (Generator Expressions)](#910-生成器表达式-generator-expressions)
- [10. 标准库简介 (Brief Tour of the Standard Library)](#10-标准库简介-brief-tour-of-the-standard-library)
    - [10.1. 操作系统接口 (Operating System Interface)](#101-操作系统接口-operating-system-interface)
    - [10.2. 文件通配符 (File Wildcards)](#102-文件通配符-file-wildcards)
    - [10.3. 命令行参数 (Command Line Arguments)](#103-命令行参数-command-line-arguments)
    - [10.4. 错误输出重定向和程序终止 (Error Output Redirection and Program Termination)](#104-错误输出重定向和程序终止-error-output-redirection-and-program-termination)
    - [10.5. 字符串模式匹配 (String Pattern Matching)](#105-字符串模式匹配-string-pattern-matching)
    - [10.6. 数学 (Mathematics)](#106-数学-mathematics)
    - [10.7. 互联网 (Internet Access)](#107-互联网-internet-access)
    - [10.8. 日期和时间 (Dates and Times)](#108-日期和时间-dates-and-times)
    - [10.9. 数据压缩 (Data Compression)](#109-数据压缩-data-compression)
    - [10.10. 性能测试 (Performance Measurement)](#1010-性能测试-performance-measurement)
    - [10.11. 质量控制 (Quality Control)](#1011-质量控制-quality-control)
    - [10.12. 包含电池？？ (Batteries Included)](#1012-包含电池-batteries-included)
- [11. 标准库2 (Brief Tour of the Standard Library — Part II)](#11-标准库2-brief-tour-of-the-standard-library--part-ii)
    - [11.1. 输出格式 (Output Formatting)](#111-输出格式-output-formatting)
    - [11.2. 模板 (Templating)](#112-模板-templating)
    - [11.3. 二进制记录布局 (Working with Binary Data Record Layouts)](#113-二进制记录布局-working-with-binary-data-record-layouts)
    - [11.4. 多线程 (Multi-threading)](#114-多线程-multi-threading)
    - [11.5. 日志记录 (Logging)](#115-日志记录-logging)
    - [11.6. 弱引用 (Weak References)](#116-弱引用-weak-references)
    - [11.7. 使用列表的工具 (Tools for Working with Lists)](#117-使用列表的工具-tools-for-working-with-lists)
    - [11.8. 十进制浮点运算 (Decimal Floating Point Arithmetic)](#118-十进制浮点运算-decimal-floating-point-arithmetic)
- [12. 虚拟环境和包 (Virtual Environments and Packages)](#12-虚拟环境和包-virtual-environments-and-packages)
    - [12.1. 介绍 (Introduction)](#121-介绍-introduction)
    - [12.2. 创建虚拟环境 (Creating Virtual Environments)](#122-创建虚拟环境-creating-virtual-environments)
    - [12.3. 用 pip 管理包 (Managing Packages with pip)](#123-用-pip-管理包-managing-packages-with-pip)
- [13. 现在怎么办？ (What Now?)](#13-现在怎么办-what-now)
- [14. 交互式输入编辑和历史替换 (Interactive Input Editing and History Substitution)](#14-交互式输入编辑和历史替换-interactive-input-editing-and-history-substitution)
    - [14.1. 制表和历史编辑(Tab Completion and History Editing)](#141-制表和历史编辑tab-completion-and-history-editing)
    - [14.2. 交互式解释器的替代品(Alternatives to the Interactive Interpreter)](#142-交互式解释器的替代品alternatives-to-the-interactive-interpreter)
- [15. 浮点数的问题和约束(Floating Point Arithmetic: Issues and Limitations)](#15-浮点数的问题和约束floating-point-arithmetic-issues-and-limitations)
    - [15.1. 错误 (Representation Error)](#151-错误-representation-error)
- [16. 附录 (Appendix)](#16-附录-appendix)
    - [16.1. 互动模式 (Interactive Mode)](#161-互动模式-interactive-mode)
        - [16.1.1. 错误处理 (Error Handling)](#1611-错误处理-error-handling)
        - [16.1.2. 可执行的PY脚本(Executable Python Scripts)](#1612-可执行的py脚本executable-python-scripts)
        - [16.1.3. 交互式启动文件 (The Interactive Startup File)](#1613-交互式启动文件-the-interactive-startup-file)
        - [16.1.4. 制作模块 (The Customization Modules)](#1614-制作模块-the-customization-modules)

<!-- /TOC -->
# 1. 勾起你的欲望 (Whetting Your Appetite)

# 2. 使用PYthon解释器 (Using the Python Interpreter)

## 2.1. 调用解释器 (Invoking the Interpreter)

### 2.1.1. 参数传递 (Argument Passing)

### 2.1.2. 交互模式 (Interactive Mode)

## 2.2. 解释器及其环境(The Interpreter and Its Environment)

### 2.2.1. 源代码编码(Source Code Encoding)

# 3. PY 的非正式介绍(An Informal Introduction to Python)

## 3.1. PY作为计算器？(Using Python as a Calculator)

### 3.1.1. 数字 (Numbers)

### 3.1.2. 字符 (Strings)

### 3.1.3. 列表 (Lists)

## 3.2. 编程的第一步 (First Steps Towards Programming)

# 4. 更多控制流工具 (More Control Flow Tools)

## 4.1. if 语句(if Statements)

## 4.2. for 语句(for Statements)

## 4.3. range() 函数 (The range() Function)

## 4.4. break、continue、else(break and continue Statements, and else Clauses on Loops)

## 4.5. pass 语句(pass Statements)

## 4.6. 定义函数(Defining Functions)

## 4.7. 更多关于定义函数的内容(More on Defining Functions)

### 4.7.1. 默认参数 (Default Argument Values)

### 4.7.2. 关键字参数 (Keyword Arguments)

### 4.7.3. 任意的参数列表 (Arbitrary Argument Lists)

### 4.7.4. 拆包参数列表 (Unpacking Argument Lists)

### 4.7.5. lambda 表达式(Lambda Expressions)

### 4.7.6. 文档字符串 (Documentation Strings)

### 4.7.7. 函数注释 (Function Annotations)

## 4.8. 代码风格 (Intermezzo: Coding Style)

# 5. 数据结构 (Data Structures)

## 5.1. 更多关于列表(More on Lists)

### 5.1.1. 使用列表作为堆栈 (Using Lists as Stacks)

### 5.1.2. 使用列表作为小弟队列 (Using Lists as Queues)

### 5.1.3. 列表理解 (List Comprehensions)

### 5.1.4. 嵌套列表理解 (Nested List Comprehensions)

## 5.2. del 语句(The del statement)

## 5.3. 元组和序列 (Tuples and Sequences)

## 5.4. 集合 (Sets)

## 5.5. 字典 (Dictionaries)

## 5.6. 循环技术 (Looping Techniques)

## 5.7. 更多条件 (More on Conditions)

## 5.8. 比较序列和其他类型 (Comparing Sequences and Other Types)

# 6. 模块 (Modules)

## 6.1. 关于更多模块 (More on Modules)

### 6.1.1. 将模块作为脚本执行(Executing modules as scripts)

### 6.1.2. 模块搜索路径 (The Module Search Path)

### 6.1.3. 编译 PY 文件 (“Compiled” Python files)

## 6.2. 标准模块 (Standard Modules)

## 6.3. dir() 函数(The dir() Function)

## 6.4. 包 (Packages)

### 6.4.1. 从包中导入* (Importing * From a Package)

### 6.4.2. 引用intra包 (Intra-package References)

### 6.4.3. 多个目录中的包 (Packages in Multiple Directories)

# 7. 输入和输出 (Input and Output)

## 7.1. fancier 输出格式 (Fancier Output Formatting)

### 7.1.1. 格式化字符串 (Formatted String Literals)

### 7.1.2. 字符串 format() 方法 (The String format() Method)

### 7.1.3. 手动字符串格式 (Manual String Formatting)

### 7.1.4. 旧的字符串格式 (Old string formatting)

## 7.2. 读写文件 (Reading and Writing Files)

### 7.2.1. 文件对象的方法 (Methods of File Objects)

### 7.2.2. 用json保存结构化数据 (Saving structured data with json)

# 8. 错误和异常 (Errors and Exceptions)

## 8.1. 语法错误 (Syntax Errors)

## 8.2. 异常 (Exceptions)

## 8.3. 处理异常 (Handling Exceptions)

## 8.4. 抛出异常 (Raising Exceptions)

## 8.5. 用户自定义异常 (User-defined Exceptions)

## 8.6. 定义清理动作？ (Defining Clean-up Actions)

## 8.7. 预定义的清理动作 (Predefined Clean-up Actions)

# 9. 类 (Classes)

## 9.1. 关于名字和物体的一个单词 (A Word About Names and Objects)

## 9.2. 作用域和命名空间 (Python Scopes and Namespaces)

### 9.2.1. 作用域和命名空间例子 (Scopes and Namespaces Example)

## 9.3. 第一眼看到的类 (A First Look at Classes)

### 9.3.1. 类定义语法 (Class Definition Syntax)

### 9.3.2. 类对象 (Class Objects)

### 9.3.3. 实例对象 (Instance Objects)

### 9.3.4. 对象方法 (Method Objects)

### 9.3.5. 类变量 与 实例变量(Class and Instance Variables)

## 9.4. 随机备注 (Random Remarks)

## 9.5. 继承 (Inheritance)

### 9.5.1. 多重继承 (Multiple Inheritance)

## 9.6. 私有变量 (Private Variables)

## 9.7. 零碎的知识 (Odds and Ends)

## 9.8. 迭代器 (Iterators)

## 9.9. 生成器 (Generators)

## 9.10. 生成器表达式 (Generator Expressions)

# 10. 标准库简介 (Brief Tour of the Standard Library)

## 10.1. 操作系统接口 (Operating System Interface)

## 10.2. 文件通配符 (File Wildcards)

## 10.3. 命令行参数 (Command Line Arguments)

## 10.4. 错误输出重定向和程序终止 (Error Output Redirection and Program Termination)

## 10.5. 字符串模式匹配 (String Pattern Matching)

## 10.6. 数学 (Mathematics)

## 10.7. 互联网 (Internet Access)

## 10.8. 日期和时间 (Dates and Times)

## 10.9. 数据压缩 (Data Compression)

## 10.10. 性能测试 (Performance Measurement)

## 10.11. 质量控制 (Quality Control)

## 10.12. 包含电池？？ (Batteries Included)

# 11. 标准库2 (Brief Tour of the Standard Library — Part II)

## 11.1. 输出格式 (Output Formatting)

## 11.2. 模板 (Templating)

## 11.3. 二进制记录布局 (Working with Binary Data Record Layouts)

## 11.4. 多线程 (Multi-threading)

## 11.5. 日志记录 (Logging)

## 11.6. 弱引用 (Weak References)

## 11.7. 使用列表的工具 (Tools for Working with Lists)

## 11.8. 十进制浮点运算 (Decimal Floating Point Arithmetic)

# 12. 虚拟环境和包 (Virtual Environments and Packages)

## 12.1. 介绍 (Introduction)

## 12.2. 创建虚拟环境 (Creating Virtual Environments)

## 12.3. 用 pip 管理包 (Managing Packages with pip)

# 13. 现在怎么办？ (What Now?)

# 14. 交互式输入编辑和历史替换 (Interactive Input Editing and History Substitution)

## 14.1. 制表和历史编辑(Tab Completion and History Editing)

## 14.2. 交互式解释器的替代品(Alternatives to the Interactive Interpreter)

# 15. 浮点数的问题和约束(Floating Point Arithmetic: Issues and Limitations)

## 15.1. 错误 (Representation Error)

# 16. 附录 (Appendix)

## 16.1. 互动模式 (Interactive Mode)

### 16.1.1. 错误处理 (Error Handling)

### 16.1.2. 可执行的PY脚本(Executable Python Scripts)

### 16.1.3. 交互式启动文件 (The Interactive Startup File)

### 16.1.4. 制作模块 (The Customization Modules)
