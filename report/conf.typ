#let adaptive_blank(..pairs) = {
  let rows = ()
  for pair in pairs.pos() {
    rows.push(
      grid(
        align: center, 
        columns: (auto, 1fr), 
        inset: 5pt, 
        stroke: (x, y) => if x == 1 {
          (bottom: black)
        }, 
        ..pair
      )
    )
  }

  grid(
    columns: (1fr,), 
    inset: 10pt,
    ..rows
  )
}

#let conf(
  class: none,
  title: none,
  author: none,
  author_num: none, 
  co_author: none, 
  co_author_num: none, 
  doc,
) = {
  set page(
    paper: "a4",
    margin: (
      top: 2.54cm,
      bottom: 2.54cm,
      left: 3.18cm,
      right: 3.18cm,
    )
  )

  set text(
    font: (
      "Times New Roman",
      (name: "FangSong", covers: "latin-in-cjk"),
    ),
    lang: "zh",
    size: 12pt,
  )

  set heading(
    numbering: "1.1"
  )

  align(
    center, 
    [
      #image("assets/cover.png")
      #block(height: 2em)
      #set text(
        font: (
          "Times New Roman",
          (name: "SimHei", covers: "latin-in-cjk")
        ), 
        size: 28pt
      )
      《Python与算法设计实验》 \
      课程设计报告

      #set text(
        font: (
          "Times New Roman",
          (name: "FangSong", covers: "latin-in-cjk")
        ), 
        size: 22pt
      )
      #block(
        width: 80%,
      )[
      #adaptive_blank(
        ([题目: ], title),
        ([学号: ], author_num),
        ([姓名: ], author),
        ([同组成员姓名: ], co_author),
        ([同组成员学号: ], co_author_num), 
        ([班级: ], class), 
        ([提交时间: ], datetime.today().display()), 
        ([成绩评定: ], )
      )]
    ]
  )

  pagebreak()

  outline()

  pagebreak()

  set page(
    header: grid(
      columns: (auto, 1fr), 
      align: (x, y) => if x == 1 {right} else {left},
      [Python与算法设计实验], 
      [课程设计报告]
    ), 
    numbering: "第1页 共1页"
  )

  set align(left)

  set par(
    first-line-indent: (
      amount: 2em,
      all: true,
    ),
    // hanging-indent: 0.5em,
    spacing: 10pt,
  )

  show list: it => block(
    inset: (left: 2em),
    it,
  )

  show enum: it => block(
    inset: (left: 2em),
    it,
  )

  show heading: it => text(
    it, 
    font: (
      "Times New Roman",
      (name: "SimHei", covers: "latin-in-cjk")
    ), 
  )
  doc
}
