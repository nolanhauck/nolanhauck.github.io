#let template(
  book: [],
  author: [],
  chapter: [],
  section: [],
  num: [],
  doc
) = [
  #set page(
    margin: 1in,
    numbering: "1"
  )
  // use + for problems
  #set enum(
  numbering: "1)",
  spacing: 1in
  )
  // for the formulas list
  #set list(
    spacing: 5mm
  )
  #set par(
    leading: 0.55em,
    spacing: 0.75em,
    first-line-indent: 1.8em,
    justify: true
  )
  #set text(
    font: "New Computer Modern",
    size: 12pt
  )
  #show raw: set text(font: "New Computer Modern")
  #show heading: set block(
    above: 1.4em,
    below: 1em
  )
  
  #align(left)[
    #text(size: 12pt)[
      #book, #author, Exercise #chapter.#section.#num
    ]
  ]

  #v(.5cm)

  *Solution.* 
  
  #doc
]

