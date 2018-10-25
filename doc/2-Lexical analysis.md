# 2 Lexical analysis（词法分析）

## 2.1.4. Encoding declarations（编码声明）

If a comment in the first or second line of the Python script matches the regular expression coding[=:]\s*([-\w.]+), 

如果python的第一行或第二行匹配正则表达式：coding[=:]\s*([-\w.]+)

this comment is processed as an encoding declaration; 

这行注释作为编码声明进行处理。

the first group of this expression names the encoding of the source code file. 

这个表达式的第一组，作为源代码文件的编码。

The encoding declaration must appear on a line of its own. 

这个编码声明必须出现在它自己的一行上（指不能换行吗？）

If it is the second line, the first line must also be a comment-only line.

如果它是第二行，第一行必须也是一行注释。

 The recommended forms of an encoding expression are

编码声明的推荐类型是：


    # -*- coding: <encoding-name> -*-

which is recognized also by GNU Emacs, and

这也被 GUN Emacs 识别，或者

    # vim:fileencoding=<encoding-name>

which is recognized by Bram Moolenaar’s VIM.

它能被 Bram Moolenaar's VIM 识别。

If no encoding declaration is found, the default encoding is UTF-8. In addition, if the first bytes of the file are the UTF-8 byte-order mark (b'\xef\xbb\xbf'), the declared file encoding is UTF-8 (this is supported, among others, by Microsoft’s notepad).

如果没有找到编码声明，默认编码为utf-8。此外，如果文件的开始的字节是utf-8字节顺序标记（b'\xef\xbb\xbf'），这个文件的编码也是utf-8（这是windows 记事本支持的）（注：实际上文件类型是 utf-8 +bom）

If an encoding is declared, the encoding name must be recognized by Python. The encoding is used for all lexical analysis, including string literals, comments and identifiers.

如果声明编码，编码必须被python识别，所有词法分析使用这个编码，包括字符串字面量、注释和标识符。

## 2.1.5 Explicit line joining 显式行连接

Two or more physical lines may be joined into logical lines using backslash characters (\), 

二或更多自然行，可以使用反斜线（\）连接成逻辑行，

as follows: 

如下，

when a physical line ends in a backslash that is not part of a string literal or comment, 

当一个自然行结尾是反斜线，并且不是字符串或注释的一部分，

it is joined with the following forming a single logical line, 

它与下列内容连接形成一个逻辑行，

deleting the backslash and the following end-of-line character. For example:

删除这个反斜线和后面的行的结束字符，比如：


    if 1900 < year < 2100 and 1 <= month <= 12 \
       and 1 <= day <= 31 and 0 <= hour < 24 \
       and 0 <= minute < 60 and 0 <= second < 60:   # Looks like a valid date
            return 1

A line ending in a backslash cannot carry a comment. 

以反斜线结尾的行不能注释。

A backslash does not continue a comment. 

反斜线之后不能有注释。


A backslash does not continue a token except for string literals 

反斜线之后不能有符号，除了字符串常量。

(i.e., tokens other than string literals cannot be split across physical lines using a backslash). 

（即，符号 另外 比 字符串常量 不能 切割 穿过 自然行 使用 一个反斜线 ）
（除字符串常量之外的标记，不能使用反斜线分割自然行。）
*（即，非字符串常量的标记，不能使用反斜线横跨自然行）

A backslash is illegal elsewhere on a line outside a string literal.

反斜线在字符串外的其他行上是非法的。
*反斜线出现在字符串之外的位置，是非法的。

## 2.1.6 implicit line joining (隐式行连接)

Expressions in parentheses, 

括号中的表达式，

square brackets or curly braces can be split over more than one physical line without using backslashes. 

方括号 或 花括号中，能够分割更多的物理行，而不使用反斜线。


For example:

例如

    month_names = ['Januari', 'Februari', 'Maart',      # These are the
               'April',   'Mei',      'Juni',       # Dutch names
               'Juli',    'Augustus', 'September',  # for the months
               'Oktober', 'November', 'December']   # of the year

Implicitly continued lines can carry comments. 

隐式的连续不断的行，能携带注释。
在隐式换行中，可以编写注释。

The indentation of the continuation lines is not important.

连续行的缩进，不重要。
在连续行范畴内，缩进不重要。

Blank continuation lines are allowed. 

空白的连续行是允许的。
可以出现空白行。

There is no NEWLINE token between implicit continuation lines.

隐式连续行之间没有 NEWLINE 标记。
连续行之间没有 newline 标记。

Implicitly continued lines can also occur within triple-quoted strings (see below); in that case they cannot carry comments.

在三个引号字符串中，也可以出现隐式连续行。在这种情况，他们不能携带注释。
在三个引号的注释中，也支持连续行，但不能包含注释。

## 2.1.7. Blank lines (空白行)

A logical line that contains only spaces, tabs, formfeeds and possibly a comment, is ignored (i.e., no NEWLINE token is generated).

一个逻辑行 仅仅 包含 空格、tabs、换页和可能的注释，是可以忽视的。（即，不生成NEWLINE标记）

During interactive input of statements, 

在声明交互式输入期间，

 handling of a blank line may differ depending on the implementation of the read-eval-print loop. 

根据read-eval-print循环，空白行的处理可能有所不同。

 In the standard interactive interpreter, 

在标准交互式解释器中，

 an entirely blank logical line (i.e. one containing not even whitespace or a comment) terminates a multi-line statement.

完全空白的逻辑行（即：不包含空格或注释）终止多行语句。

## 2.1.8. Indentation（缩进）

Leading whitespace (spaces and tabs) at the beginning of a logical line is used to compute the indentation level of the line, which in turn is used to determine the grouping of statements.

逻辑行开始的空白（空格、tab）用于计算行的缩进级别，这个用于确定语句分组。

Tabs are replaced (from left to right) by one to eight spaces such that the total number of characters up to and including the replacement is a multiple of eight (this is intended to be the same rule as used by Unix). 

tab 被替换(从左到右)为一个到八个空格，字符总数和包含替换者是8的倍数。（这是为了与unix使用的规则相同）

The total number of spaces preceding the first non-blank character then determines the line’s indentation. 

第一个非空白字符前面的空格总数，决定了行的缩进。


Indentation cannot be split over multiple physical lines using backslashes; 

缩进不能分割使用反斜线的多个物理行。

the whitespace up to the first backslash determines the indentation.

空格 到 第一个反斜线决定了缩进。

Indentation is rejected as inconsistent if a source file mixes tabs and spaces in a way that makes the meaning dependent on the worth of a tab in spaces; 


如果源文件混合tab和空格的方式，那么意义依赖于tab在空格中的价值，导致缩进不一致而被拒绝。

a TabError is raised in that case.

这种情况，引发一个TabError。

Cross-platform compatibility note: 

跨平台一致性提醒：

because of the nature of text editors on non-UNIX platforms, 

由于 文本编辑器在非unix平台上的性质，

it is unwise to use a mixture of spaces and tabs for the indentation in a single source file. 

在单个源码文件中，使用混合tab和空格的缩进，是不明智的。

It should also be noted that different platforms may explicitly limit the maximum indentation level.

也应当说明，在不同的平台，可能明确的限制最大的缩进等级。

A formfeed character may be present at the start of the line; 

换行符可能出现在行首。


it will be ignored for the indentation calculations above.

上面的缩进计算，将被忽略。


 Formfeed characters occurring elsewhere in the leading whitespace have an undefined effect (for instance, they may reset the space count to zero).

在前导空白中其他位置出现换行符，作用未定义。（ 例如，他们可能重置空格数量为0 ）

The indentation levels of consecutive lines are used to generate INDENT and DEDENT tokens, using a stack, as follows.

连续行的缩进等级 用于 生成 INDENT 和 DEDENT 令牌，这个过程使用栈，如下所述。

Before the first line of the file is read, 

读取文件首行之前，

a single zero is pushed on the stack; 

一个 0 被推入到栈;

this will never be popped off again. 

这将不会再弹出。

The numbers pushed on the stack will always be strictly increasing from bottom to top. 

推入栈的数字，总是从下到上严格的递增。

At the beginning of each logical line,

每个逻辑行的起点， 

the line’s indentation level is compared to the top of the stack. 

行的缩进级别与栈的顶部进行比较。

If it is equal, nothing happens. 

如果它是相同的，不会发生任何事。

If it is larger,

如果大于栈，

 it is pushed on the stack, 

它会推入栈中，

 and one INDENT token is generated.

并且产生一个INDENT token。

If it is smaller,

如果它小于栈，

 it must be one of the numbers occurring on the stack; 
 
它必须是栈中数字之一，


 all numbers on the stack that are larger are popped off, 

栈中的所有数字，大于它的全部弹出离开，

 and for each number popped off a DEDENT token is generated.

并为每个弹出离开的数字，生成一个DEDENT token。

  At the end of the file, 

到达文件的结尾时，

  a DEDENT token is generated for each number remaining on the stack that is larger than zero.

为栈中剩余的每个大于0的数字生成一个 DEDENT token。


Here is an example of a correctly (though confusingly) indented piece of Python code:

这是一个正确的例子，python代码的缩进块：

  def perm(l):
          # Compute the list of all permutations of l
      if len(l) <= 1:
                    return [l]
      r = []
      for i in range(len(l)):
               s = l[:i] + l[i+1:]
               p = perm(s)
               for x in p:
                r.append(l[i:i+1] + x)
      return r

The following example shows various indentation errors:

接下来的例子展示各种缩进错误：

     def perm(l):                       # error: first line indented
    for i in range(len(l)):             # error: not indented
      s = l[:i] + l[i+1:]
          p = perm(l[:i] + l[i+1:])   # error: unexpected indent
          for x in p:
                  r.append(l[i:i+1] + x)
              return r                # error: inconsistent dedent

(Actually, the first three errors are detected by the parser; only the last error is found by the lexical analyzer — the indentation of return r does not match a level popped off the stack.)

（
实际上，最早三个错误时格式化时发现的，仅仅最后的错误时此法分析发现的。这个``return r``的缩进 与 弹出堆栈的级别不匹配。
）

## 2.1.9. Whitespace between tokens 字符(token)之间的空白

Except at the beginning of a logical line or in string literals, 

除了逻辑行开头或字符串文字之外，

the whitespace characters space, 

空白字符空间

tab and formfeed can be used interchangeably to separate tokens. 

tab和换页符能够互换使用分隔token。


Whitespace is needed between two tokens only if their concatenation could otherwise be interpreted as a different token

仅当它们的连接可以解释为不同的令牌时，两个令牌之间才需要空白。

 (e.g., ab is one token, but a b is two tokens).

（即 ab 时一个符号，但是 a b 是两个符号）

## 2.2. Other tokens （其他符号）

Besides NEWLINE, INDENT and DEDENT,

除了 NEWLINE，INDENT 和 DEDENT，

 the following categories of tokens exist: 

存在以下符号的类别：

 identifiers, keywords, literals, operators, and delimiters. 

标识符、关键字、文字、运算符和分隔符。

 Whitespace characters (other than line terminators, discussed earlier) are not tokens, 

空白字符（出前面讨论过的行终止符之外）不是有效的符号。

 but serve to delimit tokens.

但是用于划分符号。

  Where ambiguity exists, 

在哪里存在歧义，

  a token comprises the longest possible string that forms a legal token, 

合法符号的形式由最长可能的字符串组成。
一个令牌由合法令牌的最长可能字符组成。

  when read from left to right.

在从左到右阅读时。

## 2.3. Identifiers and keywords （标识符和关键字）

Identifiers (also referred to as names) are described by the following lexical definitions.

标识符（也被称为名称）由以下词汇定义来描述。

The syntax of identifiers in Python is based on the Unicode standard annex UAX-31, with elaboration and changes as defined below; see also PEP 3131 for further details.

python中的标识符的语法，基于Unicode标准附件UAX-31，跟详细定义和修改，如下；对于进一步的细节也可以看 PEP 3131。

Within the ASCII range (U+0001..U+007F), the valid characters for identifiers are the same as in Python 2.x: the uppercase and lowercase letters A through Z, the underscore _ and, except for the first character, the digits 0 through 9.

在 ASCII 范围内（U+0001...U+007F）标识符的有效字符 与 Python 2.x 中一致：大写和小写字母 A-Z 和 下划线 "_"，除第一个字符外的数字0-9。

Python 3.0 introduces additional characters from outside the ASCII range (see PEP 3131). For these characters, the classification uses the version of the Unicode Character Database as included in the unicodedata module.

python3.0 采用 来自ASCII范围之外的其他字符（看PEP 3131），对于这些字符，分类使用在unicode数据模块中包含的unicode字符数据库版本。

Identifiers are unlimited in length. Case is significant.

标识符的长度是无限的，case 很重要。

    identifier   ::=  xid_start xid_continue*
    id_start     ::=  <all characters in general categories Lu, Ll, Lt, Lm, Lo, Nl, the underscore, and characters with the Other_ID_Start property>
    id_continue  ::=  <all characters in id_start, plus characters in the categories Mn, Mc, Nd, Pc and others with the Other_ID_Continue property>
    xid_start    ::=  <all characters in id_start whose NFKC normalization is in "id_start xid_continue*">
    xid_continue ::=  <all characters in id_continue whose NFKC normalization is in "id_continue*">

    identifier ::= xid_start xid_continue*
    id_start ::= 在通用类别Lu, Ll, Lt, Lm, Lo, Nl, 中所有的字符、下划线 具有other_id_start 属性的字符 >

The Unicode category codes mentioned above stand for:

上面提及的unicode分类代码表，包含：

- Lu - uppercase letters
- 大写字母
- Ll - lowercase letters
- 小写字母
- Lt - titlecase letters
- 首字母大写
- Lm - modifier letters
- 修改字母
- Lo - other letters
- 其他字母
- Nl - letter numbers
- 数字
- Mn - nonspacing marks
- 非间距标志
- Mc - spacing combining marks
- 间距组合标记
- Nd - decimal numbers
- 小数点
- Pc - connector punctuations
- 连接符
- Other_ID_Start - explicit list of characters in PropList.txt to support backwards compatibility
- 在 proplist.txt 中明确定义的字符列表，支持向后兼容
- Other_ID_Continue - likewise
- 同样??

All identifiers are converted into the normal form NFKC while parsing; comparison of identifiers is based on NFKC.

所有标识符在解析时转换为标准形式的NFKC。标识符的比较基于NFKC。

A non-normative HTML file listing all valid identifier characters for Unicode 4.1 can be found at https://www.dcl.hpi.uni-potsdam.de/home/loewis/table-3131.html.

包含所有 unicode4.1中所有有效标识符的非规范HTML文件，可以在 http://xxx 找到。

