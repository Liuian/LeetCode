# Python 3 Topics Roadmap

## 1. 基礎語法與運算子 (Syntax & Operators)
- 縮排規則 (Indentation) 與程式區塊結構
- 變數命名慣例（包含底線 `_` 作為忽略變數的用法）
    - 避開關鍵字：變數別取 set、list、dict，否則會覆蓋內建函式導致報錯。如改用 seen = set()，而不是 set = set()。
- 基本資料型別：`int`、`float`、`str`、`bool`、`None`
    - `bool` 簡寫:
        ```python
        # 原本的寫法
        if len(set(nums)) < len(nums):
            return True
        else:
            return False

        # 簡潔寫法
        return len(set(nums)) < len(nums)
        ```
- 算術運算子：`+`、`-`、`*`、`/`、`%`（取餘數）、`**`（次方）
- **地板除 (Floor Division `//`)**
    - 取「小於或等於商的最大整數」
    - `7 // 3` → 數學商為 `2.33...` → 往下取整數是 `2`
    - `-7 // 3` → 數學商為 `-2.33...` → 地板除是 `-3`
    - Example: 用 `r // 3` 計算九宮格位置 [ref]`36. Valid Sudoku`
- 比較運算子（`==`、`!=`、`<`、`>`）與邏輯運算子（`and`、`or`、`not`）
- 成員運算子（Membership Operators：`in`、`not in`）

## 2. 流程控制 (Control Flow)
- 條件判斷：`if`、`elif`、`else`
- `for` 迴圈與 `range()` 函式（含巢狀迴圈遍歷二維陣列）
    - `for num in nums`: 直接取元素值（最簡潔）。
    - `for i in range(len(nums))`: 取索引位置（適合比較相鄰元素，如從 `range(1, len(nums))` 開始）。
    - for loop 可以倒著數 `for i in range(n - 1, -1, -1)`:
        - 起始值 n - 1：陣列最後一格的索引（因為索引從 0 開始算）。
        - 結束值 -1：range() 不包含結束值，所以要寫 -1，迴圈才會確實跑到索引 0 才停下。
        - 步長 -1：每次迴圈索引減 1，代表往左倒退走。
- `while` 迴圈
- **迴圈控制關鍵字**
    - `break`
    - `continue`: 跳過「這一次」迴圈剩下的程式碼，直接進入「下一次」迴圈。
        ```python
        for i in [1, 2, 3]:
            if i == 2:
                continue
            print(i)
        # 輸出：1, 3
        ```
    - `pass`: 什麼事都不做（空操作），純粹用來維持語法結構完整。
        ```python
        for i in [1, 2, 3]:
            if i == 2:
                pass  # 單純佔位，不影響後續執行
            print(i)
        # 輸出：1, 2, 3
        ```
- 結構化模式比對 (`match` / `case`)

## 3. 內建資料結構 (Built-in Data Structures)
- **字串 (String)**
  - **切片 (Slicing)**：`s[i : j]` 擷取索引 `i` 到 `j` 的片段，口訣為**「含頭不含尾」**（不包含 `s[j]`），切出來的長度剛好是 `j - i`。
  - **格式化字串 (f-string)**：`f"{len(s)}_{s}"` 可在字串中直接嵌入變數或運算式，自動將數字轉為字串（變數建議命名為 `s`，避開內建函式 `str`）。
  - **串列合併為字串**：`"".join(output)` 將 `list` 內的所有字串元素接成一個完整字串。

- **串列 (List)**
    - 索引、切片 (Slicing)、常用方法（`append`、`pop`、`sort`）與二維串列 (`list[list[str]]`)
    - 初始化 list 並設特定長度：`arr = [1] * n`
    - Sort:
        - `nums.sort()`：原地排序，不佔額外空間 O(1)。
        - `sorted(nums)`：回傳新列表，需額外空間 O(n)。
- **集合 (Set)**
    - 不重複元素特性、建立空集合 `set()`、新增元素 `.add()` 與 $O(1)$ 快速查詢
    - `seen = set()` + for loop 裡的 `seen.add(x)`：邊走邊查，可提早結束。
    - `set(nums)`：一次轉換去重，底層由 C 語言執行，通常整體最快。
- **字典 (Dictionary)**：
    - 鍵值對 (Key-Value) 操作、`.get()`、`.items()`
    - 建立與新增：用 {} 建立空字典 `counts = {}`；`counts[num] = 1` 新增鍵值對，`counts[num] += 1` 更新次數。
    - 檢查存在與否：用 `if num in counts`: 判斷 Key 是否已在字典中。
    - 預設迭代行為：直接將字典放進 `for` 迴圈或 `sorted()` 時，Python 預設只會取出所有的 Key。
    - 兩個 `dict` 可以直接用 `==` 比較而無需先排序，因為它是透過雜湊表比對所有的 key 與對應的 value 是否完全一致，與放入的順序無關。**範例**：`{'a': 1, 'b': 2} == {'b': 2, 'a': 1}` (也可以寫成 dict1 == dict2) 結果為 `True`。
- 元組 (Tuple)：不可變序列 (Immutable) 與解包 (Unpacking)
- **推導式 / 生成式 (Comprehensions)**：
  - 串列生成式（List Comprehension）
    - `[set() for _ in range(9)]`: 重複 9 次，每次都變出一個全新的空集合，然後把它們裝進一個大串列裡。
        ```python
        [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        # 0    1    2    3   4   5   6   7   8
        ```
  - 字典生成式 (Dict Comprehension) 
  - 集合生成式 (Set Comprehension)

## 4. 函式與型別提示 (Functions & Type Hints)
- 函式定義 (`def`) 與回傳值 (`return`)
- 參數傳遞：預設參數、關鍵字參數、`*args` 與 `**kwargs`
- 變數作用域 (Scope)：`local`、`global`、`nonlocal`
- 匿名函式 (`lambda`) 與高階函式（`map`、`filter`、`sorted`）
    - **sorted()**
        - 三個參數結構：`sorted(iterable, key=None, reverse=False)`
            - iterable：要被排序的對象。
            - key=：比大小的規則函式。`key=lambda x: counts[x]` （counts = {}）代表「拿每個數字 x 去查對應的次數（Value）來比大小」，但最終回傳的仍是原本的 Key。
            - reverse=：排序方向，True 為由大到小，預設 False 為由小到大。
        - 回傳型別：sorted() 永遠會回傳一個全新的 list。
- **型別提示 (Type Hints / Annotations)**
    - 函式參數與回傳值標註（如 `board: list[list[str]] -> bool`）

## 5. 物件導向程式設計 (OOP)
- **類別與方法基礎 (`class` & `self`)**
    - `class`（類別）：就像是「設計藍圖」。例如 class Solution: 定義了一個叫做 Solution 的藍圖，裡面規定這個物件具備哪些功能（方法）。
    - 物件 / 實例（`Instance`）：根據藍圖實際製造出來的「實體」。例如在本地測試時寫的 sol = Solution()，就是用 Solution 這張藍圖做出一個名為 sol 的實體工具。
    - 為什麼每個類別裡的方法（如 def isValidSudoku(self, board):）第一個參數都要寫 `self`？
        - 因為同一張藍圖可以做出很多個物件（例如 sol1 = Solution()、sol2 = Solution()）。當你執行 sol1.isValidSudoku(board) 時，Python 會在背景自動把 sol1 傳進 self 參數裡，讓程式知道「現在是 sol1 正在執行這個動作」。
        - 即使你在函式內部沒有用到 self（像這題），在類別裡定義一般實例方法時，self 依然是必填的第一個參數，否則呼叫時會發生參數數量不符的錯誤（TypeError）。
    - 為什麼需要創造多個物件（sol1, sol2）?
        - 生活化例子（銀行帳戶 class BankAccount）：
        - 藍圖規定每個帳戶都有「餘額（self.balance）」和「提款（withdraw）」功能。
        - 你建立兩個實體：alice_acc = BankAccount(1000) 和 bob_acc = BankAccount(500)。
        - 當執行 alice_acc.withdraw(200) 時，self 指向 alice_acc，只會扣掉 Alice 的錢，絕對不會動到 Bob 的餘額。如果全系統只用同一個物件，所有人的存款就會混在一起。
- 建構子 (`__init__`) 與魔術方法 (Dunder Methods)
- 繼承 (Inheritance)、封裝 (Encapsulation) 與多型 (Polymorphism)
- 裝飾器類別方法：`@staticmethod`、`@classmethod`、`@property`

## 6. 模組、標準函式庫與輸入輸出 (Modules & I/O)
- 模組匯入 (`import`、`from ... import ...`) 與 `if __name__ == "__main__":`
- **標準輸入輸出與資料解析**
    - `sys.stdin`
        - 一般初學者常用 `input()` 來讀取使用者輸入，但 `input()` 一次只能讀一行（遇到換行符號 `Enter` 就停了）。
        - `sys.stdin.read()` 可以一口氣把所有多行輸入全部讀進來，變成一整個長字串（`str`），直到 user 按下檔案結束符號（Windows 為 Ctrl+Z 後按 Enter，Mac/Linux 為 Ctrl+D）。
    - `ast.literal_eval()`
        - ast 是 Python 內建的抽象語法樹（Abstract Syntax Trees）模組，裡面的 literal_eval() 函式能安全地把「長得像 Python 資料結構的字串」還原成真正的 Python 資料型別（如 list、dict、tuple、int 等）。
        - 檢查這棵語法樹裡面的節點，只允許出現 Python 的「基本字面常數（Literals）」語法結構：
            - 看到 [...] → 直接對應建立 Python 的 list
            - 看到 {k: v} → 建立 dict
            - 看到 (...) → 建立 tuple
            - 看到 {1, 2} → 建立 set
            - 看到 '...' 或 "..." → 建立 str
            - 看到純數字 123 / 3.14 → 建立 int / float
            - 看到 True / False / None → 建立對應的布林值與空值
- 常用內建函式：`len()`、`enumerate()`、`zip()`、`id()`、`any()`、`all()`
- 常用標準庫：`collections`（`Counter`、`defaultdict`、`deque`）、`itertools`、`math`、`heapq`
- 檔案讀寫 (`open` 與 `with` 上下文管理器) 與 JSON 處理

## 7. 例外處理與進階特性 (Exceptions & Advanced Python)
- 例外處理：`try`、`except`、`else`、`finally`、`raise`
- 迭代器 (Iterators) 與生成器 (Generators / `yield`)
- 裝飾器 (Decorators) 與閉包 (Closures)
- 淺拷貝 (Shallow Copy) 與深拷貝 (Deep Copy / `copy` 模組)
- 非同步程式設計 (`async` / `await`) 與虛擬環境管理 (`venv`、`pip`)