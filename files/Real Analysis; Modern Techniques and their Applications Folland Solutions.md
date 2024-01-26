$$
\text{\textbf{Commands}}
%Fancy letters%
\newcommand{\R}{\mathbb{R}}
\newcommand{\N}{\mathbb N}
\newcommand{\cE}{\mathcal E}
\newcommand{\cM}{\mathcal M}
\newcommand{\cF}{\mathcal F}
\newcommand{\bb}[1]{\mathbb{#1}}
\newcommand{\cal}[1]{\mathcal{#1}}

%non-built-in functions%
\newcommand{\card}[1]{\text{card}\left(#1\right)}
$$

# Chapter 1
## Section 2: $\sigma$-algebras
### Exercise 1
A family of sets $\mathcal R\subset\mathcal P(X)$ is a called a **ring** if it is closed under finite unions and set differences. A ring that is closed under countable unions is called a $\sigma$-ring. Prove the following:
**a.** Rings (resp. $\sigma$-rings) are closed under finite (resp. countable) intersections. 
**b.** If $\mathcal R$ is a ring (resp. $\sigma$-ring), then $\mathcal R$ is an algebra (resp. $\sigma$-algebra) if and only if $X\in\mathcal R.$
**c.** If $\mathcal R$ is a $\sigma$-ring, then $\{E\subset X:E\in\mathcal R\text{ or }E^c\in\mathcal R\}$ is a $\sigma$-algebra.
**d.** If $\mathcal R$ is a $\sigma$-ring, then $\{E\subset X:E\cap F\in\mathcal R\text{ for all }F\in\mathcal R\}$ is a $\sigma$-algebra.
#### Solution.
**a.** Let $\mathcal R$ be a ring. Let $E_1,\ldots,E_n\in\mathcal R$ and let $E=\bigcup_{j=1}^n E_j.$ Then $E\in\mathcal R.$ Now,
$$
\begin{align}
	E\setminus\left(\bigcap_{j=1}^nE_j\right)&=\bigcup_{j=1}^nE\setminus E_j\in\mathcal R
\end{align}
$$ since each $E\setminus E_j\in\mathcal R.$ Then 
$$
\bigcap_{j=1}^nE_j=E\setminus\left(E\setminus\left(\bigcap_{j=1}^nE_j\right)\right)\in\mathcal R.
$$
Now let $\mathcal R$ be a $\sigma$-ring, and let $\{E_j\}_1^\infty\subset\mathcal R.$ The exact same argument as above works, since DeMorgan's laws work for arbitrary intersections and unions.
**b.** Let $\mathcal R$ be a ring and suppose it is also an algebra. Then $\mathcal R$ is closed under complements, so if $E\in\mathcal R,$ then $E^c\in\mathcal R.$ But then $\mathcal R$ is closed under finite unions, so $X=E\cup E^c\in\mathcal R.$ Conversely, suppose $\mathcal R$ is a ring and $X\in\mathcal R.$ Then if $E\in\mathcal R,$ $E^c=X\setminus E\in\mathcal R$ as well since rings are closed under set differences. So $\mathcal R$ is an algebra.

Again, an exactly analogous argument works since rings are to algebras as $\sigma$-rings are to $\sigma$-algebras. The only difference from the former to the latter is closedness under complements.
**c.** Let $\mathcal A=\{E\subset X:E\in\mathcal R\text{ or }E^c\in\mathcal R\}.$ Then let $E\in\mathcal A$ and show $E^c\in\mathcal A.$ There are two cases. If $E\in\mathcal R,$ then $E^c\in\mathcal A$ since $(E^c)^c=E\in\mathcal R.$ On the other hand, if $E^c\in\mathcal R,$ then immediately $E^c\in\mathcal A.$ 
First, let $E,F\in\mathcal A.$ Then if both $E$ and $F$ are in $\mathcal R,$ then $E\cup F\in\mathcal A.$ If $E,F^c\in\mathcal R,$ then by the above, $F=(F^c)^c\in\mathcal R$ and we are in the first case. A similar logic handles the other two possibilities. By induction, $\mathcal A$ is closed under finite unions. By part **a.,** $\mathcal A$ is also closed under finite intersections. So, given a collection $\{E_j\}_1^\infty\subset\mathcal A,$ we can define a new collection $\{F_j\}_1^\infty$ by setting $F_k=E_k\setminus\bigcup_{j=1}^{k-1}E_j$ for each $k.$ Then these $F_j$ are disjoint and $\bigcup F_j=\bigcup E_j.$ Also $F_k=E_k\cap\left(\bigcup_{j=1}^{k-1}E_j\right)$, so $F_k\in\mathcal A$ since each $E_k\in\mathcal A$ and $\mathcal A$ is closed under finite unions and intersections. Thus, we have reduced our problem to showing that $\mathcal A$ is closed under countable disjoint unions. 
So let $\{E_j\}_1^\infty\subset\mathcal A$ be a collection of disjoint sets in $\mathcal A.$ Let $F\subset\mathbb N$ be the collection of indices $j$ such that $E_j\in\mathcal R.$ Then $F^c=\mathbb N\setminus F$ is the collection of indices so that $E_j^c\in\mathcal R.$ Then define
$$
E=\bigcup_{j\in F}E_j
$$
which is in $\mathcal R$ as a countable union. Then
$$
E\setminus\left(\bigcup_{j=1}^\infty E_j\right)^c=E\cap\bigcup_{j=1}^\infty E_j=\bigcup_{j\in F}E_j\in\mathcal R
$$
since the $E_j$ are all disjoint. Then
$$
E\setminus\left(E\setminus\left(\bigcup_{j=1}^\infty E_j\right)^c\right)=\left(\bigcup_{j=1}^\infty E_j\right)^c\in\mathcal R,
$$
meaning $\bigcup_{j=1}^\infty E_j\in\mathcal A.$  
**d.** Let $\mathcal A=\{E\subset X:E\cap F\in\mathcal R\text{ for all }F\in\mathcal R\}.$ Then $X\in\mathcal A$ since $X\cap F=F\in\mathcal R$ for all $F\in\mathcal R.$ Let $E_1,E_2\in\mathcal A$ and $F\in\mathcal R$. Then show
$$
(E_1\setminus E_2)\cap F=(E_1\cap F)\setminus(E_2\cap F).\tag{1}
$$
If $x$ is an element in the LHS, then $x\in E_1$ and not in $E_2$ and $x\in F.$ This means $x\notin E_2\cap F$, so we have shown $\subseteq.$ Now suppose $x$ is an element in the RHS. Then $x\in E_1$ and in $F$, but $x$ is not in the intersection $E_2\cap F.$ If $x\in F$ and $x\notin E_2\cap F,$ then $x$ cannot be in $E_2.$ So we have shown $\supseteq$ (note that this equality has nothing to do with the rings or $\sigma$-algebras, and is general to set theory). Now since $F\in\mathcal R$ and $E_1,E_2\in\mathcal A,$ $E_j\cap F\in\mathcal R$ for $j=1,2.$ Since $\mathcal R$ is closed under set differences, the RHS of (1) is in $\mathcal R,$ meaning $E_1\setminus E_2\in\mathcal A.$
Now suppose $\{E_j\}_1^\infty\subset\mathcal A.$ Then for all $F\in\mathcal R,$
$$
F\cap\bigcup E_j=\bigcup(F\cap E_j)\in\mathcal R
$$
as a countable union. So $\mathcal A$ is a $\sigma$-ring which contains $X,$ meaning it is a $\sigma$-algebra by part **b.** 
### Exercise 2
Complete the proof of Proposition 1.2, which states that $\mathcal B_{\mathbb R}$ is generated by each of the following:
**a.** the open intervals $\mathcal E_1=\{(a,b):a<b\}$;
**b.** the closed intervals $\mathcal E_2=\{[a,b]:a<b\}$;
**c.** the half-open intervals: $\mathcal E_3=\{(a,b]:a<b\}\text{ or }\mathcal E_4=\{[a,b):a<b\}$;
**d.** The open rays in either direction; and
**e.** The closed rays in either direction.
#### Solution.
First, note that $\mathcal B_{\mathbb R}=\sigma(\tau),$ where $\tau$ is the open sets on $\mathbb R$ in the usual topology, which has as countable basis the open intervals with rational endpoints. Thus, any open set in $\mathbb R$ is a countable union of open intervals. 
**a.** Clearly, $\mathcal E_1\subset\tau$ since open intervals are, well, open. So $\sigma(\cal E_1)\subset\sigma(\tau)=\cal B_\R.$ Conversely, consider an open set $E\in\tau.$ Then as in the introduction, $E=\bigcup_1^\infty(a_j,b_j)$, a countable union of open intervals (an infinite number of these could be empty, like if $E$ were itself an open interval). But this means $E\in\sigma(\cal E_1)$ since $\sigma$-algebras are closed under countable unions. So $\tau\subset\sigma(\cal E_1)\implies\sigma(\tau)\subset\sigma(\cal E_1).$
**b.** We will show $\sigma(\cal E_1)=\sigma(\cal E_2)$ and apply **a.** For an open interval $(a,b)\in\cal E_1,$ 
$$
(a,b)=\bigcup_{n=1}^\infty\left[\frac{a+b}{2}-\left(1-\frac{1}{n+1}\right)\frac{b-a}{2},\frac{a+b}2+\left(1-\frac{1}{n+1}\right)\frac{b-a}2\right],
$$
since $\frac{a+b}2$ is the exact midpoint between $a$ and $b$ and $1-\frac{1}{n+1}\to1$ as $n\to\infty,$ but is never equal to one, and $\frac{b-a}{2}$ is the distance of the endpoints of an interval $(a,b)$ to their midpoint. We choose $n+1$ for the denominator of our proportion because the union starts from $1$ and if the denominator were just $n,$ the first "interval" would not be an element of $\cal E_2.$ Anyway, this shows any element of $\cal E_1$ is a countable union of $\cal E_2$ and thus $\cal E_2\subset\sigma(\cal E_2).$ 
Conversely, for any closed interval $[a,b]\in\cal E_2,$ 
$$
[a,b]=\bigcap_{n=1}^\infty\left(a-\frac{1}{n},b+\frac{1}n\right),
$$
and $\sigma$-algebras are closed under countable intersections, so $\cal E_2\subset\sigma(\cal E_1)$ and we have shown both inclusions.
**c.** Here we show that $\sigma(\cal E_1)=\sigma(\cal E_3)$ and $\sigma(\cal E_1)=\sigma(\cal E_4).$ For any open interval $(a,b)$, there exists $N\in\bb N$ so that for all $n\geq N$, we have $b-\frac{1}n>a.$ Then 
$$
(a,b)=\bigcup_{n=N}^\infty\left(a,b-\frac{1}n\right]
$$
so that $\cal E_1\subset\sigma(\cal E_3).$ 
Conversely, for any half-open interval $(a,b],$ 
$$
(a,b]=\bigcap_{n=1}^\infty\left(a,b+\frac{1}n\right)
$$
so that $\cal E_3\subset\sigma(\cal E_1).$ Thus $\sigma(\cal E_1)=\sigma(\cal E_3).$ An exactly analogous argument can be used to show the second equality.
**d.** The left-open rays are $\cal E_5=\{(-\infty,a):a\in\R\}$. As before, it suffices to show $\sigma(\cal E_4)=\sigma(\cal E_5),$ for which it suffices to show that $\cal E_4\subset\sigma(\cal E_5)$ and $\cal E_5\subset\sigma(\cal E_4).$ For a left-open ray $(-\infty,a)\in\cal E_5,$ we have
$$
(-\infty,a)=\bigcup_{n=1}^\infty\left[a-n,a\right)
$$
so $\cal E_5\subset\sigma(\cal E_4).$ For any half-closed interval $[a,b)\in\cal E_4,$ $(-\infty,b)\setminus(-\infty,a)=[a,b)\in\sigma(\cal E_5)$ since $\sigma$-algebras are closed under set differences. The same argument can be used to show that $\sigma(\cal E_6)=\sigma(\{(a,\infty):a\in\R\})=\sigma(\cal E_3).$ 
**e.** The left-closed rays are $\cal E_7=\{(-\infty,a]:a\in\R\}.$ Here, it suffices to show that $\sigma(\cal E_7)=\sigma(\cal E_3).$ For a closed interval $(a,b]\in\cal E_3,$ we have $(a,b]=(-\infty,b]\setminus(-\infty,a].$ So $\cal E_3\subset\sigma(\cal E_7).$ 
Conversely, for any left-closed ray $(-\infty,a]\in\cal E_7,$
$$
(-\infty,a]=\bigcup_{n=1}^\infty(a-n,b]
$$
so that $\cal E_7\subset\sigma(\cal E_3).$ So the desired equality is shown. The same argument can be used to show that $\sigma(\cal E_8)=\sigma(\{[a,\infty):a\in\R\})=\sigma(\cal E_4).$ 

#### Note. 
This result is rather useful, since we have basically shown the following:
$$
\cal B_\R=\sigma(\cal E_i)=\sigma(\cal E_j)
$$
for any $i,j\in\{1,2,3,\ldots,8\}.$ Whether we have explicitly written the expression or not, any set in one family can be expressed using only sets from any other family.
### Exercise 3
Let $\cal M$ be an infinite $\sigma$-algebra. Then show the following:
**a.** $\cal M$ contains an infinite sequence of disjoint sets.
**b.** $\card{\cal M}\geq\mathfrak{c}.$ 
#### Solution.
**a.**  Since $\cal M$ is infinite, there exists a countable collection $\{E_n\}_1^\infty\subset\cal M$ comprised of distinct sets. If this collection is already pairwise disjoint we are done. If $F_k=E_k\setminus\left(\bigcup_{n=1}^{k-1}E_n\right)\neq\emptyset$ for all $k\underset{\neq}{>} 1$ (it's fine if $E_1=F_1=\emptyset$), then we are also done, as the collection $\{F_k\}$ will be a subset of $\cal M$ and pairwise disjoint. So suppose there is at least one such $F_k$ with $k\underset{\neq}{>} 1$ which is empty, and that $E_1\neq\emptyset.$ Note that $F_2=E_1\setminus E_2$ is never empty, since the $E_n$ are distinct. We prove that $F_k=\emptyset\implies F_{k+1}\neq\emptyset$ for all $k$. If
$$
F_k=E_k\setminus\left(\bigcup_{n=1}^{k-1}E_n\right)=\emptyset,
$$
then $E_k=\bigcup_{n=1}^{k-1}E_n.$ Then if $$F_{k+1}=E_{k+1}\setminus\left(\bigcup_{n=1}^{k}E_n\right)=E_{k+1}\setminus \left(E_k\cup\bigcup_{n=1}^{k-1}E_n\right)=E_{k+1}\setminus E_k=\emptyset,$$ then $E_{k+1}=E_k$, contradicting the distinctness of the collection. Now, if there are only finitely many non-empty $F_k$, then there exists $K\in\bb N$ so that $F_k=\emptyset$ for all $k\geq K.$ But this is a contradiction since there cannot be consecutive empty $F_k$'s. Thus there is a countably infinite sub-collection $\{F_{k_j}\}_{j=1}^\infty$ of disjoint sets. Finally, each $F_k\in\cal M$ since $\sigma$-algebras are closed under finite unions and set differences.
**b.** Suppose $\cal M$ were countable. Then suppose $\cal M=\{E_n\}_1^\infty$ is a distinct labelling of all the elements of $\cal M.$ If all the $E_n$ are disjoint, then $E_1\cup E_2\in\cal M$ and is not equal to any $E_n$ for $n\geq 3.$ This contradicts that we have labelled all elements of $\cal M.$ If not all the elements of $E_n$ are disjoint, then by part **a.,** we can construct a disjoint sequence $\{F_{k}\}_1^\infty$ from the $E_n$'s. At least one of these $F_k$'s must be distinct from all the $E_n$'s as otherwise the original labelling would be disjoint and we are in the first case. Thus the original labelling cannot be complete. So $\cal M$ is uncountable. 
### Exercise 4
Given an algebra $\cal A,$ show that $\cal A$ is a $\sigma$-algebra if and only if $\cal A$ is closed under countable increasing unions (i.e. if $\{E_j\}_1^\infty\subset\cal A$ and $E_1\subset E_2\subset E_3\subset\dots,$ then $\bigcup_1^\infty E_j\in\cal A$).
#### Solution.
($\implies$) This direction is immediate, since $\sigma$-algebras are closed under any countable unions.
( $\Longleftarrow$ ) Conversely, suppose that $\cal A$ is an algebra which is closed under increasing unions, as described in the problem. Since $\cal A$ is an algebra, all that remains to be shown is that $\cal A$ is closed under any countable unions. Let $\{E_j\}_1^\infty$ be a collection of sets in $\cal A.$ Define a new collection $\{F_k\}_1^\infty$ via the definition
$$
F_k=\bigcup_{j=1}^kE_j
$$
for each $k.$ Since $\cal A$ is an algebra, each $F_k\in \cal A$ as a finite union. Also $F_1\subset F_2\subset F_3\subset\dots,$ so this is an increasing collection of sets in $\cal A.$ Thus $\bigcup_{k=1}^\infty F_k\in\cal A.$ But 
$$
\bigcup_{k=1}^\infty F_k=\bigcup_{k=1}^\infty\bigcup_{j=1}^kE_j=\bigcup_{j=1}^\infty E_j,
$$
so $\bigcup_{j=1}^\infty E_j\in\cal A.$ 
### Exercise 5
If $\cal M$ is a $\sigma$-algebra generated by $\cal E,$ then $\cal M$ is the union of the $\sigma$-algebras generated by $\cal F$ as $\cal F$ ranges over all the countable subsets of $\cal E$ (Hint: show the latter object is itself a $\sigma$-algebra).
#### Solution.
Let $K=\{\cal F:\cal F\text{ is a countable subset of \cal E}\}.$ Then we must show that
$$
\cal M:=\sigma(\cal E)=\bigcup_{\cal F\in K}\sigma(\cal F).\tag{1}
$$
Let the RHS of (1) be $\cal A.$  We will show that $\cal A$ is a $\sigma$-algebra. Let $E\in\cal A.$ Then $E\in\sigma(\cal F)$ for some $\cal F\in K,$ so $E^c\in\sigma(\cal F),$ meaning $E^c\in\cal A.$ 
Now let $\{E_j\}_1^\infty$ be a collection of sets in $\cal A.$ For each $j\in\N,$ there is a countable $\cal F_j\subset\cal E$ so that $E_j\in\sigma(\cal F_j)$ meaning
$$
\{E_j\}_1^\infty\subset\bigcup_{j=1}^\infty\sigma(\cal F_j).
$$
Then $\bigcup_{j=1}^\infty\cal F_j$ is also countable as a countable union of countable sets, and is thus in $K.$ Since $\cal F_\ell\subset\bigcup_{j=1}^\infty\cal F_j$ for each $\ell$, $\sigma(\cal F_\ell)\subset\sigma(\bigcup_{j=1}^\infty\cal F_j)$ for each $\ell.$ But this means that
$$
\bigcup_{j=1}^\infty\sigma(\cal F_j)\subset\sigma\left(\bigcup_{j=1}^\infty\cal F_j\right).
$$
Then since the latter object is $\sigma$-algebra in which the countable collection $\{E_j\}$ is contained, and since the latter object is a subset of $\cal A,$ we have
$$
\bigcup_{j=1}^\infty E_j\in\sigma\left(\bigcup_{j=1}^\infty\cal F_j\right)\subset\bigcup_{\cal F\in K}\sigma(\cal F).
$$
Thus $\cal A$ is closed under countable unions.
Given that the $\cal A$ is a $\sigma$-algebra, we now show the identity in (1). Suppose $E\in\cal E.$ Then $\{E\}$ is a countable subset of $\cal E,$ so that $\sigma(\{E\})\subset \cal A.$ But $E\in\sigma(\{E\}),$ so $E\in\cal A.$ Thus $\cal E\subset\cal A,$ and since $\cal A$ is a $\sigma$-algebra, $\sigma(\cal E)\subset\cal A.$
Conversely, suppose $A\in \cal A.$ Then $A\in\sigma(\cal F)$ for some $\cal F\in K.$ But $\cal F\subset\cal E,$ so $\sigma(\cal F)\subset\sigma(\cal E),$ meaning $A\in\sigma(\cal E).$ Thus $\cal A\subset\sigma(\cal E).$ We have shown inclusion in both directions, so the identity in (1) holds.
## Section 3: Measures

### Exercise 6
Prove Theorem 1.9, which states: Suppose that $(X,\cal M,\mu)$ is a measure space. Let $\cal N=\{N\in\cal M:\mu(N)=0\}$ and $\overline{\cal M}=\{E\cup F:E\in\cal M\text{ and }F\subset N\text{ for some }N\in\cal N\}.$ Then $\overline{\cal M}$ is a $\sigma$-algebra, and there is a unique extension $\overline\mu$ of $\mu$ to a complete measure on $\overline{\cal M}.$ This the "Completion Theorem."
#### Solution.
Since $\cal M$ and $\cal N$ are closed under countable unions, so is $\overline{\cal M}$ ($\cal N$ is due to the subadditivity of $\mu$). Let $E\cup F\in\overline{\cal M}$ so that $E\in\cal M$ and $F\subset N$ for some $N\in\cal N.$ Then we can assume $E$ and $F$ are disjoint, since $F\setminus E\subset N$ and $E\cup F=(F\setminus E)\cup E.$ But then we can assume that $E$ and $N$ are disjoint as well, since if $E$ and $F$ are disjoint but $E\cap N\neq\emptyset,$ we have $N\setminus E\in\cal M$ and $\mu(N\setminus E)\leq \mu(N)=0$ and $F\subset N\setminus E.$ So the collection with these restrictions is the same as the collection without them. So we have
$$
(E\cup F)^c=E^c\cap F^c=(E^c\cap N^c)\cup(F^c\cap N) 
$$
and $E^c\cap N^c\in\cal M$ and $F^c\cap N\subset N$, so $(E\cup F)^c\in\overline{\cal M}.$ Thus $\overline{\cal M}$ is closed under complements. 

Now define $\overline{\mu}:\overline{\cal M}\to[0,\infty]$ by $\overline{\mu}(E\cup F)=\mu(E).$ This is well-defined since if $E_1\cup F_1=E_2\cup F_2$ are two different representations of the same set in $\overline{\cal M}$ so that $F_j\subset N_j\in\cal N$ for $j=1,2,$ then $\overline{\mu}(E_1\cup F_1)=\mu(E_1)\leq\mu(E_2\cup N_2)=\mu(E_2)=\overline\mu(E_2\cup F_2).$ The same can be done in the other direction, so $\overline{\mu}(E_1\cup F_1)=\overline\mu(E_2\cup F_2).$ 

Now show $\overline\mu$ is a measure: $\overline\mu(\emptyset)=\overline\mu(\emptyset\cup\emptyset)=\mu(\emptyset)=0.$ Suppose $\{E_j\cup F_j\}_1^\infty\subset\overline{\cal M}.$ Then there is $N_j\in\cal N$ so that $F_j\subset N_j$ for all $j.$ Thus
$$
\bigcup_1^\infty (E_j\cup F_j)=\bigcup_{j=1}^\infty E_j\cup\bigcup_{j=1}^\infty F_j
$$
and $\bigcup E_j\in\cal M$ and $\bigcup F_j\subset\bigcup N_j$ and $\mu(\bigcup N_j)\leq\sum\mu(N_j)=0,$ so 
$$
\overline\mu\left(\bigcup_{j=1}^\infty (E_j\cup F_j)\right)=\mu\left(\bigcup_{j=1}^\infty E_j\right)\leq\sum_{j=1}^\infty\mu(E_j)=\sum_{j=1}^\infty \overline\mu(E_j\cup F_j).
$$
Thus $\overline\mu$ is a measure on $\overline{\cal M}.$ 

Now show $\overline{\mu}$ is complete. Let $E\cup F\in\overline{\cal M}$ be such that $\overline\mu(E\cup F)=0$ and let $A\subset E\cup F.$ Since $\overline\mu(E\cup F)=0,$ we have $\mu(E)=0.$ If $F\subset N$ so that $N\in\cal M$ and $\mu(N)=0,$ then $E\cup F\subset E\cup N$ and $E\cup N\in\cal M$ and $\mu(E\cup N)\leq\mu(E)+\mu(N)=0.$ Then notice that $A=A\cap (E\cup F)= (A\cap E)\cup(A\cap F),$ and $A\cap E$ and $A\cap F$ are both subsets of null sets in $\cal M,$ since $\mu(E)=0,$ meaning both are in $\overline{\cal M}.$ Thus $A\in\overline{\cal M},$ so $\overline\mu$ is complete. 

Finally, suppose $\nu:\overline{\cal M}\to[0,+\infty]$ is another complete measure on $\overline{\cal M}$ so that $\nu(E)=\mu(E)$ for all $E\in\cal M.$ Then for $E\cup F\in\overline{\cal M},$ 
$$
\overline\mu(E\cup F)=\mu(E)=\nu(E)\leq\nu(E\cup F)
$$ since $E\subset E\cup F$ and $\nu$ is a measure on $\overline{\cal M}.$ Conversely,
$$
\nu(E\cup F)\leq \nu(E)+\nu(F)=\nu(E)=\overline\mu(E\cup F),
$$
as $\nu(F)=0$ since $\nu$ is complete. So $\overline{\mu}$ is the unique complete extension of $\mu$ to $\overline{\cal M}.$
### Exercise 7
If $\mu_1,\ldots,\mu_n$ are measures on $(X,\cal M)$ and $a_1,\ldots,a_n\in[0,\infty),$ then $\mu=\sum_{j=1}^na_j\mu_j$ is a measure on $(X,\cal M).$
#### Solution.
Since $\mu_j$ is a measure for all $j=1,\ldots,n,$ $\mu_j(\emptyset)=0$ for all $j.$ Thus
$$
\mu(\emptyset)=\sum_{j=1}^na_j\mu_j(\emptyset)=\sum_{j=1}^na_j\cdot0=0.
$$
Now suppose $\{E_k\}_1^\infty\subset\cal M.$ Then since all $a_j\geq0$ and all $\mu_j$ are subadditive,
$$
\begin{align}
\mu\left(\bigcup_{k=1}^\infty E_k\right)&=\sum_{j=1}^na_j\mu_j\left(\bigcup_{k=1}^\infty E_k\right)\leq\sum_{j=1}^na_j\sum_{k=1}^\infty\mu_j(E_k) \\
&=\sum_{j=1}^n\sum_{k=1}^\infty a_j\mu_j(E_k)=\sum_{k=1}^\infty\sum_{j=1}^na_j\mu_j(E_k)=\sum_{k=1}^\infty\mu(E_k)
\end{align}
$$
so $\mu$ is subadditive. This interchanging of finite and infinite sums works since it is equivalent to the identity
$$
\begin{multline}
\sum_{k=1}^\infty a_1\mu_1(E_k)+\sum_{k=1}^\infty a_2\mu_2(E_k)+\dots+\sum_{k=1}^\infty a_n\mu_n(E_k) \\
=\sum_{k=1}^\infty\left[a_1\mu_1(E_k)+a_2\mu_2(E_k)+\dots+a_n\mu_n(E_k)\right],
\end{multline}
$$
which is itself equivalent to rearranging the terms in the left hand side. The sum of an absolutely convergent series, as this one is, is independent of any rearrangement of the terms.
### Exercise 8
Show that if $(X,\cal M,\mu)$ is a measure space and $\{E_j\}_1^\infty\subset\cal M,$ then $\mu(\liminf E_j)\leq\liminf\mu(E_j).$ Also, $\mu(\limsup E_j)\geq\limsup\mu(E_j),$ provided that $\mu(\bigcup_1^\infty E_j)<\infty.$ 
#### Solution.
**Lemma.** Given $E\in\cal M$ with $\mu(E)<\infty$ and $F\subset E$ measurable, $\mu(E\setminus F)=\mu(E)=\mu(F).$
**Proof.** Notice $(E\setminus F)\cup F=E,$ and $E\cap F$ and $F$ are disjoint, so
$$
\begin{align}
\mu(E)=\mu(E\setminus F)+\mu(F)
\end{align}
$$and the equality is shown. $\square$
First, note that since $\cal M$ is closed under countable unions and countable intersections, $\bigcup_{j=k}^\infty E_j\in\cal M$ for all $k\in\N$ and thus $\liminf E_j=\bigcup_{k=1}^\infty\bigcap_{j=k}^\infty E_j\in\cal M.$ Then by subadditivity,
$$
\mu(\liminf E_j)\leq \sum_{k=1}^\infty\mu\left(\bigcap_{j=k}^\infty E_j\right).
$$
Since $\mu(\bigcap_{j=k}^\infty E_j)\leq \mu(E_j)$ for all $j\geq k$ and $k\in\N,$ 
$$
\mu\left(\bigcap_{j=k}^\infty E_j\right)\leq\inf_{j\geq k}\mu(E_j)
$$
for all $k\in\N.$ Then
$$
\mu(\liminf E_j)\leq\sum_{k=1}^\infty\inf_{j\geq k}\mu(E_j)
$$
If $\sum_{k=1}^\infty\inf_{j\geq k}\mu(E_j)=\infty,$ then the sequence $\{\inf_{j\geq k}\mu(E_j)\}_{k=1}^\infty$ cannot converge to a finite number, so $\sup_k\inf_{j\geq k}\mu(E_j)=\infty$ also. On the other hand, if $\sum_{k=1}^\infty\inf_{j\geq k}\mu(E_j)<\infty,$ then the sequence $\inf_{j\geq k}\mu(E_j)\to0$ as $k\to\infty.$ But since this is an increasing sequence and $\mu$ is nonnegative, $\inf_{j\geq k}\mu(E_j)=0$ for all $k\in\N.$ In either case,
$$
\sum_{k=1}^\infty\inf_{j\geq k}\mu(E_j)\leq\sup_k\inf_{j\geq k}\mu(E_j)=\liminf\mu(E_j).
$$
For the other inequality, notice that for similar reasoning, $\limsup E_j\in\cal M.$ Then notice that 
$$
\begin{align}
	\limsup E_j&=\bigcap_{k=1}^\infty\bigcup_{j=k}^\infty E_j \\
	&=\bigcap_{k=1}^\infty\left(\bigcap_{j=k}^\infty E_j^c\right)^c \\
	&=\left(\bigcup_{k=1}^\infty \bigcap_{j=k}^\infty E_j^c\right)^c \\
	&=(\liminf E_j^c)^c.
\end{align}
$$
Next, knowing that $\mu\left(\bigcup_{j=1}^\infty E_j\right)<\infty,$ we would like to have $(\liminf E_j^c)^c\subset\bigcup E_j.$ But
$$
\liminf E_j^c=\bigcup_{k=1}^\infty\bigcap_{j=k}^\infty E_j^c\supseteq\bigcap_{j=1}^\infty E_j^c\implies (\liminf E_j^c)^c\subseteq\left(\bigcap_{j=1}^\infty E_j^c\right)^c=\bigcup_{j=1}^\infty E_j
$$
Then we want to be able to discuss the measure of $\left(\bigcup_{j=1}^\infty E_j\right)\cap(\liminf E_j^c)$ to convert this $\liminf$ back into a $\limsup.$ If $E=\bigcup_{j=1}^\infty E_j,$ we have 
$$
\begin{align*}
E\cap(\liminf E_j^c)&=E\cap\left(\bigcup_{k=1}^\infty\bigcap_{j=k}^\infty E_j^c\right) \\
&=\bigcup_{k=1}^\infty\left(E\cap\left(\bigcap_{j=k}^\infty E_j^c\right)\right) \\
&=\bigcup_{k=1}^\infty\bigcap_{j=k}^\infty E\cap E_j^c=\liminf(E\cap E_j^c).
\end{align*}
$$
So since the union has finite measure, and since for a sequence of real numbers $\{a_n\},$ $\limsup a_n=-\liminf(-a_n)$, and by the first proof, and by the lemma,
$$
\begin{align}
\mu(\limsup E_j)&=\mu((\liminf E_j^c)^c) \\
&=\mu(E)-\mu\left(E\setminus(\liminf E_j^c)^c\right) \\
&=\mu\left(E\right)-\mu\left(E\cap(\liminf E_j^c)\right) \\
&=\mu\left(E\right)-\mu(\liminf(E\cap E_j^c)) \\
&\geq\mu\left(E\right)-\liminf\mu(E\cap E_j^c) \\
&=\mu\left(E\right)-\liminf\mu(E\setminus E_j) \\
&=\mu(E)-\liminf(\mu(E)-\mu(E_j)) \\
&=\mu(E)+\limsup(\mu(E_j)-\mu(E))=\limsup(E_j).
\end{align}
$$
### Exercise 9
If $(X,\mathcal{M},\mu)$ is a measure space and $E,F\in\mathcal{M},$ then show $\mu(E)+\mu(F)=\mu(E\cup F)+\mu(E\cap F).$ 
#### **Solution.** 
First notice that $E\cup F=E\cup(F\setminus(E\cap F))$. This choice of rewriting $E\cup F$ is motivated by the desire to have some expression which includes $E\cap F.$ The sets $E$ and $F\setminus(E\cap F)$ are disjoint so we have 
$$\mu\big[E\cup(F\setminus(E\cap F))\big]=\mu(E)+\mu(F\setminus(E\cap F)).$$
If $\mu(F)=+\infty,$ then $\mu(E)+\mu(F)=+\infty$ and $\mu(E\cup F)=+\infty$ since $F\subset E\cup F.$ Thus the desired equality holds. If, on the other hand, $\mu(F)<+\infty,$ then $\mu(E\cap F)<+\infty$ since $E\cap F\subset F.$ Thus we can write 
$$\mu\big[E\cup(F\setminus(E\cap F))\big]=\mu(E)+\mu(F)-\mu(E\cap F),$$
which implies the desired equality.
### Exercise 10
Given a measure space $(X,\cal M,\mu)$ and $E\in\cal M,$ define $\mu_E(A)=\mu(A\cap E)$ for $A\in\cal M.$ Then show that $\mu_E$ is a measure on $\cal M.$
#### Solution.
We already know $(X,\cal M)$ is a measurable space. Since $\mu\geq0,$ $\mu_E\geq0$ as well. $\mu_E$ is well-defined since $E\cap A$ is entirely determined by $A.$ First, we have $\mu_E(\emptyset)=\mu(\emptyset\cap E)=\mu(\emptyset)=0.$ Now let $\{A_j\}_1^\infty\subset\cal M.$ Then since each $A_j\in\cal M,$ each $E\cap A_j\in\cal M.$ Then
$$
\mu_E\left(\bigcup_{j=1}^\infty A_j\right)=\mu\left(E\cap\bigcup_{j=1}^\infty A_j\right)=\mu\left(\bigcup_{j=1}^\infty E\cap A_j\right)\leq\sum_{j=1}^\infty\mu(E\cap A_j)=\sum_{j=1}^\infty\mu_E(A_j).
$$
So $\mu$ is a measure.
### Exercise 11
Given a finitely additive measure $\mu$ on a measurable space $(X,\mathcal{M})$, show the following:
a) $\mu$ is a measure if and only if it is continuous from below.
b) If $\mu(X)<\infty,$ then $\mu$ is a measure if and only if $\mu$ is continuous from above.
#### Solution.
The forwards direction on both of these follows from Theorem 1.8. For the backwards direction, all that must be shown is the countable additivity over disjoint unions.
(a) Suppose $\mu$ is a finitely additive measure which is continuous from below and let $\{E_j\}\subset\mathcal{M}$ be a collection of pairwise disjoint measurable subsets of $X$. Define $F_k$ to be $\bigcup_{j=1}^kE_j$ for each $k\in\mathbb{N}.$ Then $\bigcup_{k=1}^\infty F_k=\bigcup_{j=1}^\infty E_j$ and $F_1\subset F_2\subset F_3\subset\dots$ and all $F_k$ are measurable. So by the continuity from below and finite additivity of $\mu$,
$$
\begin{align*}
	\mu\left(\bigcup_{j=1}^\infty E_j\right)&=\mu\left(\bigcup_{k=1}^\infty F_k\right) \\
	&=\lim_{k\to\infty}\mu(F_k) \\
	&=\lim_{k\to\infty}\mu\left(\bigcup_{j=1}^kE_j\right) \\
	&=\lim_{k\to\infty}\sum_{j=1}^k\mu(E_j) \\
	&=\sum_{j=1}^\infty\mu(E_j).
\end{align*}
$$
(b) Suppose $\mu$ is a finitely additive measure which is continuous from above and let $\{E_j\}\subset\mathcal{M}$ be a collection of pairwise disjoint measurable subsets of $X.$ Then define $F_k$ to be $\bigcup_{j=1}^kE_j$ as in part (a) so that the unions of each collection are the same and $F_1\subset F_2\subset\dots$ Then define $G_k$ to be $F_k^c$ for each $k.$ Thus $\mu\left(\bigcap_{k=1}^\infty G_k\right)=\mu\left(X\setminus\left(\bigcup_{j=1}^\infty E_j\right)\right)=\mu(X)-\mu\left(\bigcup_{j=1}^\infty E_j\right)$. Then we have $G_1\supset G_2\supset G_3\supset\dots$ and $\mu(G_1)<\infty$ since $\mu(X)<\infty,$ so the continuity from above and finite additivity of $\mu$ give
$$
\begin{align*}
	\mu\left(\bigcap_{k=1}^\infty G_k\right)&=\lim_{k\to\infty}\mu(G_k) \\
	&=\lim_{k\to\infty}\left[\mu(X)-\mu\left(\bigcup_{j=1}^k E_j\right)\right] \\
	&=\mu(X)-\lim_{k\to\infty}\sum_{j=1}^k\mu(E_j) \\
	&=\mu(X)-\sum_{j=1}^\infty\mu(E_j),
\end{align*}
$$
so $\mu\left(\bigcup_{j=1}^\infty E_j\right)=\sum_{j=1}^\infty\mu(E_j).$ 
### Exercise 12
Let $(X,\cal M,\mu)$ be a finite measure space. Show the following:
**a.** If $E,F\in\cal M$ and $\mu(E\triangle F)=0,$ then $\mu(E)=\mu(F).$ 
**b.** Say that $E\sim F$ if $\mu(E\triangle F)=0;$ then $\sim$ is an equivalence relation on $\cal M.$ 
**c.** For $E,F\in\cal M,$ define $\rho(E,F)=\mu(E\triangle F).$ Then $\rho(E,G)\leq\rho(E,F)+\rho(F,G)$ for all $G\in\cal M,$ and hence $\rho$ defines a metric on the space $\cal M/\sim$ of equivalence classes.
#### Solution.
A note about the interpretation of this exercise. The statement "$(X,\cal M,\mu)$ is a finite measure space" could be ambiguous: does it mean that the space $X$ is finite? The collection $\cal M$? One can try to complete this exercise using one of these assumptions, but will quickly find that the correct interpretation is that $\mu$ is in fact a finite measure on $(X,\cal M),$ an arbitrary measurable space.
**a.** Let $E,F\in\cal M$ so that $\mu(E\triangle F)=0.$ Since $\mu(X)<\infty,$ $\mu(E\cup F)<\infty.$ Also $E\cap F\subset E\cup F$ and all are measurable. Then by the lemma in Exercise 8,
$$
0=\mu(E\triangle F)=\mu((E\cup F)\setminus(E\cap F))=\mu(E\cup F)-\mu(E\cap F),
$$
meaning $\mu(E\cup F)=\mu(E\cap F).$ Then
$$
\begin{align*}
	\mu(E)&\leq\mu(E\cup F)=\mu(E\cap F)\leq\mu(F) \\
	\text{and }\mu(F)&\leq\mu(E\cup F)=\mu(E\cap F)\leq\mu(E)
\end{align*}
$$
so $\mu(E)=\mu(F).$ 
**b.** For $E\in\cal M,$ $E\sim E$ since $\mu(E\triangle E)=\mu(\emptyset)=0.$ Suppose $E,F\in\cal M$ are such that $E\sim F.$ Then $F\sim E$ since $E\triangle F=F\triangle E.$ 
Now suppose $E\sim F$ and $F\sim G$ for $E,F,G\in\cal M.$ Then showing $E\sim G$ amounts to showing that $\mu(E\triangle G)=\mu((E\setminus G)\cup(G\setminus E))=\mu(E\setminus G)+\mu(G\setminus E)=0.$ But since $\mu$ is positive, this can only happen if $\mu(E\setminus G)=\mu(G\setminus E)=0.$ Since $E\sim F$ and $F\sim G$ we have
$$
\mu(E\setminus F)=\mu(F\setminus E)=\mu(F\setminus G)=\mu(G\setminus F)=0.
$$
But
$$
E\setminus G\subset(E\setminus F)\cup(F\setminus G)\quad\text{and}\quad G\setminus E\subset(G\setminus F)\cup(F\setminus E),
$$
so $\mu(E\setminus G)=\mu(G\setminus E)=0.$ 
**c.** To be pedantic here, the question is asking the reader to show that $\rho^\ast$ defined as $\rho^\ast([E],[F])=\rho(E,F)$ for $[E],[F]\in \cal M/\sim$ is a metric, so that's what we will do. The triangle inequality is proven to be satisfied using the same method as when showing transitivity in part **b:** for $[E],[F],[G]\in\cal M/\sim,$
$$
\begin{align*}
\rho^\ast([E],[G])=\rho(E,G)&=\mu(E\triangle G)=\mu(E\setminus G)+\mu(G\setminus E) \\
&\leq\mu(E\setminus F)+\mu(F\setminus G)+\mu(G\setminus F)+\mu(F\setminus E) \\
&=\mu(E\setminus F)+\mu(F\setminus E)+\mu(F\setminus G)+\mu(G\setminus F) \\
&=\mu(E\triangle F)+\mu(F\triangle G) \\
&=\rho(E,F)+\rho(F,G)=\rho^\ast([E],[F])+\rho^\ast([F],[G]).
\end{align*}
$$
The remaining conditions of being a metric are now shown. 
- $\rho^\ast([E],[E])=\rho(E,E)=\mu(E\triangle E)=0.$ 
- $\rho^\ast([E],[F])=\mu(E\triangle F)=\mu(F\triangle E)=\rho^\ast([F],[E]).$
- For $[E]\neq [F],$ we have $\mu(E\triangle F)\neq0,$ so $\rho^\ast([E],[F])\neq 0.$ (This condition is really the whole point of modding out by $\sim.$ The symmetric difference of two sets might be null set if we aren't dealing with equivalence classes.)

### Exercise 13
Show that every $\sigma$-finite measure is semi-finite.
#### Solution.
Let $(X,\cal M,\mu)$ be a $\sigma$-finite measure space. Then there are sets $\{X_j\}_1^\infty$ so that $X=\bigcup_{j=1}^\infty X_j$ and $\mu(X_j)<\infty$ for all $j.$ Let $E\in\cal M$ have infinite measure. Then $E=E\cap X=\bigcup_{j=1}^\infty E\cap X_j,$ so $\infty=\mu(E)\leq\sum_{j=1}^\infty\mu(E\cap X_j).$ But this means that there must be some $k\in\N$ so that $\mu(E\cap X_k)>0.$ But also $\mu(E\cap X_k)<\mu(X_k)<\infty.$ So $\mu$ is $\sigma$-finite. 
### Exercise 14
If $\mu$ is a semifinite measure and $\mu(E)=\infty,$ then for any $C>0$ there is $F\subset E$ so that $0<\mu(F)<\infty.$ 
#### Solution.
Basically, we need a sequence of sets $\{F_j\}$ which have finite measure diverging to $\infty,$ for then we can choose one of arbitrarily large (finite) measure. So consider the collection $A=\{F\subset E\text{ such that }\mu(F)<\infty\}.$ If the supremum of the measures of sets in this collection is $\infty,$ then there must be a sequence contained therein whose measures converges to that supremum. So let $s=\sup_{F\in A}\mu(F).$ Then suppose for contradiction that $s<\infty.$ Then there is a sequence $\{F_j\}\subset A$ so that $\lim_{j\to\infty}\mu(F_j)\to s.$ Let $G_k=\bigcup_{j=1}^k F_j.$ Then $\mu(G_k)\leq\sum_{j=1}^k\mu(F_j)<\infty$ since each $F_j\in A.$ So $G_k\in A$ for all $k,$ meaning $\mu(G_k)\leq s$ for all $k.$ Thus $\lim_{k\to\infty}\mu(G_k)\leq s,$ and by continuity from below, $\mu\left(\bigcup_{j=1}^\infty F_j\right)=\mu\left(\bigcup_{k=1}^\infty G_k\right)=\lim_{k\to\infty}\mu(G_k).$ Thus the union of the $G_k's$ (call it $G$) is in $A.$ But since $\lim_{j\to\infty}\mu(F_j)=s,$ we have $\mu(G)=s.$ Then $E\setminus G$ has infinite measure, so there exists $H\subset (E\setminus G)$ so that $0<\mu(H)<\infty$ and $H$ is disjoint from $G.$ Then $s=\mu(G)<\mu(H)+\mu(G)=\mu(H\cup G).$ But since $H$ has finite measure and $s$ is finite, $\mu(H\cup G)<\infty,$ meaning $H\cup G\in A,$ contradicting that $s$ is the supremum. Thus $s=\infty.$
### Exercise 15 
Given a measure $\mu$ on $(X,\cal M),$ define $\mu_0(E)=\sup\{\mu(F):F\subset E\text{ and }\mu(F)<\infty\}$ for each $E\in\cal M.$ Show the following:
**a.** $\mu_0$ is a semifinite measure. It is called the **semifinite part** of $\mu.$ 
**b.** If $\mu$ is semifinite, then $\mu=\mu_0$ (Use Exercise 14).
**c.** There is a measure $\nu$ on $\cal M$ (in general, not unique) which assumes only the values 0 and $\infty$ and such that $\mu=\mu_0+\nu.$ 
#### Solution.
**a.** First, $\mu_0(\emptyset)=\mu(\emptyset)=0$ since $\emptyset\subset\emptyset$ and $\mu(\emptyset)<\infty.$ Actually for any set $E\in\cal M$ with $\mu(E)<\infty,$ the measure $\mu_0(E)=\mu(E)$ since $E$ will be in the collection $\{F\subset E\text{ such that }\mu(F)<\infty\}$. Now suppose $\{E_j\}\subset\cal M$ is a collection of measurable sets. Then let $E=\bigcup_{j=1}^\infty E_j,$ let $A=\{F\in\cal M:F\subset E\text{ and }\mu(F)<\infty\}$ and let $A_j=\{F\in\cal M:F\subset E_j\text{ and }\mu(F)<\infty\}.$ Then showing that
$$
\mu_0\left(\bigcup_{j=1}^\infty E_j\right)\leq\sum_{j=1}^\infty\mu_0(E_j)
$$
is the same as showing
$$
\sup_{F\in A}\mu(F)\leq\sum_{j=1}^\infty\sup_{F\in A_j}\mu(F).
$$
Further, this will be equivalent to showing that for every $\epsilon>0,$ 
$$
\sup_{F\in A}\mu(F)\leq\sum_{j=1}^\infty\left(\sup_{F\in A_j}\mu(F)+\epsilon2^{-j}\right)=\sum_{j=1}^\infty\sup_{F\in A_j}\mu(F)+\epsilon.
$$
So let $\epsilon>0.$ By definition of supremum, for every $j\in\N,$ there exists $F_j\subset E_j$ with $\mu(F_j)<\infty$ so that 
$$
\mu(F_j)<\sup_{F\in A_j}\mu(F)+\epsilon2^{-j}=\mu_0(E_j)+\epsilon2^{-j}.
$$
Then since $\mu$ is a measure and all the $F_j$ are measurable,
$$
\begin{align}
\mu\left(\bigcup_{j=1}^\infty F_j\right)\leq\sum_{j=1}^\infty\mu(F_j)<\sum_{j=1}^\infty\left(\mu_0(E_j)+\epsilon2^{-j}\right)=\sum_{j=1}^\infty\mu_0(E_j)+\epsilon.\tag{1}
\end{align}
$$
Now define $B$ to be the collection $\{\bigcup_{j=1}^\infty F_j:F_j\subset E_j\text{ for all }j\text{ and }\mu(F_j)<\infty\}.$ Then inequality (1) shows that
$$
\sup_{F\in B}\mu(F)\leq\sum_{j=1}^\infty\mu_0(E_j).
$$
### Exercise 16
## Section 4: Outer Measures
### Exercise 24 
Let $\mu$ be a finite measure on $(X,\mathcal{M})$ and let $\mu^\ast$ be the outer measure induced by $\mu.$ Suppose that $E\subset X$ is such that $\mu^\ast(E)=\mu^\ast(X)$, but not necessarily that $E\in\mathcal{M}.$ Show the following:
(a) If $A,B\in\mathcal{M}$ and $A\cap E=B\cap E$, then $\mu(A)=\mu(B).$ 
(b) Let $\mathcal{M}_E=\{A\cap E\colon A\in\mathcal{M}\}$, and define the function $\nu\colon\mathcal{M}_E\to[0,\infty)$ by $\nu(A\cap E)=\mu(A).$ This is well-defined by part (a). Then $\mathcal{M}_E$ is a $\sigma$-algebra on $E$ and $\nu$ is a measure on $\mathcal{M}_E$. 
#### Solution.
(a) First we show that $\mu^\ast(A\cap E)=\mu(A).$ This will also apply to $B$. Since $A\in\mathcal{M},$ the HKC Extension theorem says that $A$ is $\mu_\ast$-measurable, since $\mathcal{M}\subset\mathcal{M}^\ast,$ the set of $\mu^\ast$-measurable sets. Thus, $\mu^\ast(A)=\mu(A).$ Since $A\cap E\subset A$ and $\mu^\ast$ is monotone, $\mu^\ast(A\cap E)\leq \mu^\ast(A)=\mu(A).$ 

Now, since $\mu$ is finite, $\mu(X)<\infty$, so we can say that $\mu(X)=\mu(A)+\mu(A^c)$. Note that $A^c\in\mathcal{M},$ and is thus also $\mu^\ast$-measurable, so $\mu(A^c)=\mu^\ast(A^c).$ By definition of $\mu^\ast$-measurability and since $\mu^\ast(X)=\mu^\ast(E),$ we have
$$
\mu^\ast(A)+\mu^\ast(A^c)=\mu^\ast(X)=\mu^\ast(E)=\mu^\ast(A\cap E)+\mu^\ast(A^c\cap E),
$$
meaning
$$
\mu^\ast(A\cap E)=\mu^\ast(A)+\mu^\ast(A^c)-\mu^\ast(A^c\cap E).
$$
Then by the monotonicity of $\mu^\ast$, $\mu^\ast(A^c\cap E)\leq\mu^\ast(A^c),$ so $\mu^\ast(A^c)-\mu^\ast(A\cap E)\geq0.$ Thus $\mu^\ast(A\cap E)\geq\mu^\ast(A).$ So the two are equal. 
(b) First show $\mathcal{M}_E$ is a $\sigma$-algebra. $\emptyset\in\mathcal{M}_E$ since $\emptyset\in\mathcal M$ and $\emptyset=\emptyset\cap E.$ Also $E\in\mathcal{M}_E$ since $E=X\cap E$ and $X\in\mathcal M$. Now let $F\in\mathcal{M}_E$. Then $F=A\cap E$ for some $A\in\mathcal{M}$. Then $E\setminus F=A^c\cap E\in\mathcal{M}_E$ since $A^c\in\mathcal{M}.$ Now let $\{F_j\}_1^\infty\subset\mathcal{M}_E.$ Then there is $\{A_j\}_1^\infty\subset\mathcal{M}$ so that $\{F_j\}=\{A_j\cap E\}.$ Thus
$$
\bigcup_{j=1}^\infty F_j=E\cap\bigcup_{j=1}^\infty A_j\in\mathcal{M}_E
$$
since $\bigcup A_j\in\mathcal{M}.$ 
Now show $\nu$ is a measure on $\mathcal{M}_E.$ First, $\nu(\emptyset)=\nu(\emptyset\cap E)=\mu(\emptyset)=0.$ Now we prove a lemma to show the countable additivity of $\nu.$ 
**Lemma.** Given a measure space $(X,\mathcal{M},\mu)$ and a collection of sets $\{A_j\}_1^\infty\subset\mathcal M,$ so that $\mu(A_i)\cap\mu(A_j)=0$ for all $i\neq j,$ the following equality holds:
$$
\mu\left(\bigcup_{j=1}^\infty A_j\right)=\sum_{j=1}^\infty\mu(A_j).
$$
**Proof.** Let $A=\bigcup_{j=1}^\infty A_j$ and let $N=\bigcup_{i\neq j}\mu(A_i\cap A_j).$ By subadditivity of $\mu$, we have $\mu(N)\leq\sum_{i\neq j}\mu(A_i\cap A_j)=0,$ so $\mu(N)=0.$ Thus $\mu(A\setminus N)=\mu(A).$ But 
$$
\begin{align*}
A\setminus N&=\left(\bigcup_{j=1}^\infty A_j\right)\setminus\left(\bigcup_{i\neq j}A_i\cap A_j\right) \\
&=\bigcup_{j=1}^\infty\left[A_j\setminus\left(\bigcup_{\substack{i=1 \\ i\neq j}}^\infty A_i\cap A_j\right)\right].
\end{align*}
$$
This is a disjoint union, so 
$$
\begin{align*}
\mu(A\setminus N)=\sum_{j=1}^\infty\mu\left(A_j\setminus\left(\bigcup_{\substack{i=1 \\ i\neq j}}^\infty A_i\cap A_j\right)\right).
\end{align*}
$$ The inner unions all have zero measure as subsets of $N$, so $\mu(A\setminus N)=\sum_{j=1}^\infty\mu(A_j)$. $\square$ 
So let $\{A_j\cap E\}_1^\infty\subset\mathcal{M}_E$ be a disjoint collection of sets. Since the sets are disjoint, we have that $\nu((A_i\cap E)\cap(A_j\cap E))=\nu(\emptyset)=0$ for all $i\neq j$. But $(A_i\cap E)\cap (A_j\cap E)=(A_i\cap A_j)\cap E$, so by definition $\mu(A_i\cap A_j)=0$ for all $i\neq j.$ Then by the lemma,
$$
\begin{align*}
 \nu\left(\bigcup_{j=1}^\infty(A_j\cap E)\right)=\mu(\bigcup_{j=1}^\infty A_j)=\sum_{j=1}^\infty\mu(A_j)=\sum_{j=1}^\infty\nu(A_j\cap E).
\end{align*}
$$
## Section 5: Borel measures on the Real line
### Exercise 25
### Exercise 26
Prove Proposition 1.20, which says the following: If $E\in\mathcal{M}_\mu,$ the collection of sets measurable by a Lebesgue-Stieltjes measure $\mu$, then for every $\epsilon>0$, there exists a set $A\subset\mathbb{R}$ which is a finite disjoint union of open intervals so that $\mu(A\triangle E)<\epsilon$ ($\triangle$ is the symmetric difference).  
#### Solution.
Let $\epsilon>0$. By Theorem 1.18 and the definition of infimum, there exists an open set $U$ with $E\subset U$ so that $\mu(E)+\frac{\epsilon}{2}>\mu(U)$. Since $\mathbb{R}$ is a second-countable topological space, $U$ can be written as a disjoint union of open intervals $I_j=(a_j,b_j)$. Some of these intervals could be unbounded; it makes no difference to our purpose. Since $\mu(E)<\infty$ and $\epsilon$ is finite, we also have $\mu(U)<\infty.$ Thus $\mu(U\setminus E)=\mu(U)-\mu(E)<\frac{\epsilon}{2}$. Also, since 
$$
\mu(U)=\sum_{j=1}^\infty\mu(I_j)<\infty,
$$
and the tail of a convergent series is arbitrarily small, there exists an $N\in\mathbb N$ so that $\sum_{j=N+1}^\infty\mu(I_j)<\frac{\epsilon}{2}.$ Now let $A$ be the part of the union corresponding to the head of this series: $\bigcup_{j=1}^N I_j.$ Then since $A\setminus E\subset U\setminus E$ and $E\setminus A\subset \bigcup_{j=N+1}^\infty I_j$, we have 
$$
\begin{align*}
	\mu(A\triangle E)&=\mu(A\setminus E)+\mu(E\setminus A) \\
	&\leq\mu(U\setminus E)+\mu(\bigcup_{j=N+1}^\infty I_j) \\
	&<\frac{\epsilon}{2}+\sum_{j=N+1}^\infty\mu(I_j) \\
	&<\frac{\epsilon}{2}+\frac{\epsilon}{2}=\epsilon.
\end{align*}
$$
### Exercise 27
# Chapter 2
## Section 1: Measurable Functions
### Exercise 1
## Section 2: Integration of Nonnegative Functions
### Exercise 12
Prove Proposition 2.20, which states that if $f\in L^+$ and $\int f<\infty,$ then $\{x\;\colon f(x)=\infty\}$ is a null set and $\{x\;\colon f(x)>0\}$ is $\sigma$-finite. The reader is instructed to refer to Proposition 0.20, which proves a special case.
#### Solution.
First we state and prove, as a lemma, Chebyshev's inequality.
**Lemma.** Given $f\in L^+$ and $\lambda>0$,
$$
\begin{align}
	\mu(\{x:f(x)>\lambda\})\leq\frac{1}{\lambda}\int_X f\;d\mu.	
\end{align}
$$
**Proof.** Note that the set $\{x:f(x)>\lambda\}\in\mathcal M$ since it is merely $f^{-1}((\lambda,\infty))$ and $f$ is measurable. First we prove the case when $\lambda=1.$ This reduces the problem to showing that $$\mu(\{x:f(x)>1\})\leq\int f\;d\mu.\tag{1}$$ Since $f\in L^+$, the set on the left hand side can be written in terms of the supremum of all simple functions $\phi$ such that $0\leq\phi\leq f$:
$$
\begin{align}
	\mu(\{x:f(x)>1\})=\sup_\phi\mu(\{x:\phi(x)>1\}).
\end{align}
$$
For any such $\phi,$ there is a standard expression $\phi=\sum_{j=1}^na_j\chi_{E_j}$ for disjoint $E_j$ and distinct $a_j.$ Then, there is a subset of indices $J$ so that $a_j>1$ for all $j\in J$ ($J$ could be empty). So, since measures are always positive and all $a_j$ are positive,
$$
\begin{align}
	\mu(\{x:\phi(x)>1\})=\sum_{j\in J}\mu(E_j)\leq\sum_{j\in J}a_j\mu(E_j)\leq\sum_{j=1}^na_j\mu(E_j)=\int\phi.	
\end{align}
$$
Thus,
$$
\begin{align}
	\sup_\phi\mu(\{x:\phi(x)>1\})\leq\sup_\phi\left\{\int\phi\right\}=\int f,
\end{align}
$$
where the supremums are taken over the collection of all simple functions $\phi$ with $0\leq\phi\leq f.$ It should be mentioned that these supremums exist by Theorem 2.10, the approximation theorem.
Since inequality (1) is true for any $L^+$ function, and $\frac{1}{\lambda}f\in L^+$ for any $f\in L^+$ and $\lambda>0,$ we have
$$
\mu(\{x:\frac{1}{\lambda}f(x)>1\})\leq\int\frac{1}{\lambda}f
$$
which reduces to the desired inequality. $\square$

To prove the first set is a null set, consider that for all $n\in\mathbb N,$
$$
\mu(\{x:f(x)>n\})\leq\frac{1}{n}\int f
$$
by the lemma. Since $\int f<\infty$ and the continuity from below of measures gives that $\mu(\{x:f(x)=\infty\})=\lim_{n\to\infty}\mu(\{x:f(x)>n\}),$ we have
$$
\mu(\{x:f(x)=\infty\})\leq\lim_{n\to\infty}\frac{1}{n}\int f=0.
$$
For the second set, the conclusion follows from noting that 
$$\{x:f(x)>0\}=\bigcup_{n=1}^\infty\{x:f(x)>\frac{1}{n}\}$$
and $\mu(\{x:f(x)>\frac{1}{n}\})\leq n\int f<\infty$ for all $n$ by the lemma.
### Exercise 13
### Exercise 14
Let $(X,\mathcal M,\mu)$ be a measure space. If $f\in L^+$, let $\lambda(E)=\int_E fd\mu$ for $E\in\mathcal M$. Then show that $\lambda$ is a measure on $\mathcal M$ and that for any $g\in L^+$, $\int gd\lambda=\int fgd\mu.$ 
#### Solution. 
First, $\lambda(\emptyset)=\int_\emptyset fd\mu=0$. Now let $\{E_j\}_1^\infty\subset \mathcal M$ be a collection of pairwise disjoint sets. Then if $E=\bigcup_{j=1}^\infty E_j,$ since the $E_j$ are all disjoint, the integral of any $L^+$ simple function over $E$ (being a finite sum) can be split into a countable sum of integrals over each individual $E_j$. Also taking the supremum of a sum of values which are dependent on disjoint sets is the same as the taking the sum of the supremums over each individual set. Thus 
$$
\begin{align*}
\lambda(E)&=\sup\left\{\int_E\phi\; d\mu\mid\phi\text{ is simple and }0\leq\phi\leq f\right\} \\
&=\sup\left\{\sum_{j=1}^\infty\int_{E_j}\phi\; d\mu\right\} \\
&=\sum_{j=1}^\infty\sup\left\{\int_{E_j}\phi\; d\mu\right\} \\
&=\sum_{j=1}^\infty\int_{E_j}f\;d\mu=\sum_{j=1}^\infty\lambda(E_j),
\end{align*}
$$
and $\lambda$ is a measure. 

Suppose $g\in L^+$ is simple. Then $g$ has standard expression $g=\sum_{j=1}^na_j\chi_{E_j}$ for disjoint sets $E_j$ and distinct $a_j.$ Then in the following string of equalities, we can switch the order of sum and integral since the sets over which we are integrating are all disjoint, by adding the relevant characteristic functions:
$$
\begin{align*}
	\int g\;d\lambda&=\sum_{j=1}^na_j\lambda(E_j) \\
	&=\sum_{j=1}^na_j\int_{E_j}f\;d\mu \\
	&=\sum_{j=1}^n\int_{E_j}a_jf\;d\mu \\
	&=\int_X\sum_{j=1}^na_j\chi_{E_j}f\;d\mu \\
	&=\int_Xgf\;d\mu.
\end{align*}
$$
Now let $g$ be any $L^+$ function. Then by the approximation theorem, there is an increasing sequence $\{\phi_n\}$ of simple functions with $0\leq\phi_n\leq g$ for all $n$ so that $\phi_n\to g$ pointwise on $X.$ Then since $f\in L^+,$ the sequence $\phi_nf\to gf$ as well. Then by the Monotone Convergence theorem (applied twice) and the previous identity,
$$
\begin{align*}
	\int g\;d\lambda&=\lim_{n\to\infty}\int\phi_n\;d\lambda=\lim_{n\to\infty}\int\phi_nf\;d\mu=\int\lim_{n\to\infty}\phi_nf\;d\mu=\int gf\;d\mu.
\end{align*}
$$
### Exercise 15
If $\{f_n\}\subset L^+,$ $f_n$ decreases pointwise to $f$, and $\int f_1<\infty,$ then show $\int f=\lim\int f_n.$ 
#### Solution. 
Since $f_n$ decreases to $f,$ which is measurable as the limit of a sequence of measurable functions, we have $f_1\geq f_n$ for all $n$ and thus $\infty>\int f_1\geq\int f_n$ for all $n$. Then $f_1-f_n\geq0$ so that $f_1-f_n\in L^+$ for all $n$. So for each $n,$
$$
\begin{align}
	\int f_1=\int(f_1-f_n+f_n)=\int(f_1-f_n)+\int f_n \tag{1}
\end{align}
$$
i.e. $\int f_1-\int f_n=\int(f_1-f_n)$ for each $n.$ Similarly, since $f_1\geq f$, $f_1-f\in L^+$ and the following equality holds: 
$$
\begin{align}
	\int f_1-\int f=\int(f_1-f).
\end{align}
$$
Since $f_1-f_n$ increases to $f_1-f$ as $n\to\infty$ and all are measurable, the MCT gives
$$
\begin{align*}
	\int f_1=\lim\left[\int(f_1-f_n)+\int f_n\right]=\int (f_1-f)+\lim\int f_n
\end{align*}
$$
so that
$$
\begin{align}
	\int f_1=\int f_1-\int f+\lim\int f_n,
\end{align}
$$
i.e. $\int f=\lim\int f_n.$ 
### Exercise 16
Given $f\in L^+$ and $\int f<\infty,$ show that for every $\epsilon>0$ there exists $E\in\mathcal M$ such that $\mu(E)<\infty$ and $\int_Ef>(\int f)-\epsilon.$ 
#### Solution. 
Notice that the desired inequality is equivalent to $\int f-\int_E f<\epsilon.$ This motivates one to try describing a sequence of sets $\{E_n\}$ so that $\int_{E_n}f\to\int f,$ since $\int_E f=\int f\chi_ E.$ This necessitates that this sequence converges from below to $X.$ Well, define $E_n=\{x:f(x)>\frac{1}{n}\}$ for all $n\in\mathbb N.$ Then by the Lemma in 2.12, the following inequality holds for all $n$:
$$
\mu(E_n)\leq n\int f<\infty.
$$
So $\mu(E_n)$ is always finite. Also it is clear that $E_1\nearrow X$, since $f(x)>\frac{1}n\implies f(x)>\frac{1}{n+1}.$ Now define the sequence $\{f_n\}$ of functions by $f_n=\chi_{E_n}f$ for all $n.$ Then $f_n\in L^+$ for all $n$ and $f_1\leq f_2\leq f_3\leq\dots$ and $f_n\nearrow f$. By the Monotone Convergence Theorem,
$$
\int f=\lim\int f_n.
$$
Thus, for any $\epsilon>0,$ there exists $N\in\mathbb N$ so that $\int f-\int f_n<\epsilon$ for all $n\geq N.$ But $\int f_n=\int f\chi_{E_n}=\int_{E_n}f.$ So
$$
\int_{E_n}>\left(\int f\right)-\epsilon
$$
for all $n\geq N.$ 
## Section 3: Integration of Complex Functions
## Section 4: Modes of Convergence
## Section 5: Product Measures
## Section 6: The $n$-dimensional Lebesgue Integral
## Section 7: Integration in Polar Coordinates
