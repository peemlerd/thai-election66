# Background

Thailand held a general election on May $14$th, $2023$. The $500$ seats for House of Representatives (HR) are elected from two systems: $400$ from single-member constituency (bang ket) and $100$ from party-list. The result suggested an overwhelming victory for the so-called \textit{pro-democracy} coalition ($8$ parties), which receives more than $74\%$ of the votes for party-list ballot and $312$ member of parliament (MP) seats. This translates to:

\begin{itemize}
    \item \textit{Pro-democracy coalition}: $238$ single-member and $74$ party lists ($3.2:1$).
    \item \textit{Conservative coalition}: $162$ single-member and $26$ party lists ($6.2:1$). 
\end{itemize}

Even if we consider major parties (defined as parties that win both the single-member and the party list), the picture does not change: 

\begin{itemize}
    \item \textit{Pro-democracy coalition}:  $236$ ($238-2$, excluding Pheu Thai Ruampalang) single-member and $71$ (excluding Seri Ruamthai, Palang Sangkom Mai, Pen Thum) party lists ($3.3:1)$
    \item \textit{Conservative coalition}: $162$ single-member and $19$ party lists ($8.5:1$). 
\end{itemize}

Considering their unpopularity, the conservative coalition achieved a spectacular election result in single-member constituency election. Despite receiving only $19\%$ of the party list votes, they won $40.5\%$ of single-member constituency seats. Conventional political wisdom suggests the former is driven by affection and the latter loyalty to local politicians (the so-called divided loyalty theory).However, there are several patterns that the theory could not explain. 

Take District $3$ of Kanchanaburi for instance. A candidate from Bhumjaithai won Pheu Thai by a razor-thin margin (less than $1\%$). However, Bhumjaithai receives only $5.24\%$ of the party list votes. Even if many voters have \textit{divided loyalty}, how did the Bhumjaithai candidate consolidate support among voters from the same ideological line so well?

In the opposite direction, Move Forward Party won all seats in Phuket due to the Palang Pracharat and Ruam Thai Sang Chart dividing votes. 


# Disclaimer on terms

Thai election is often viewed through binary lens — progressive versus conservative; pro-democracy versus pro-authoritarian; among others. I find these terms self-righteous and counterproductive in political discussions. Since every Member of Parliament (MP) is elected through the same electoral rules mandated by the 2017 Constitution, which criteria shall we use to determine how **authoritarian** an MP is? What makes those proclaiming to wear the mantle of democracy more democratic than others? That being said, for the sake of convention, I will use the progressive-conservative lens — the lesser of the two evils — to analyze the 2023 general election result. Henceforth, 
- Conservative parties include Democrat, Chart Thai Pattana, Chart Pattana Kla, Bhumjaithai, Palang Pracharath (PPRP), Ruam Thai Sang Chart, and Thai Pukdee.
- Progressive parties include Pheu Thai, Move Forward, Thai Sang Thai, Prachachart, Seri Ruam Thai, Pheu Thai Ruampalang.

# 
# Appendix
## About the dataset

The [original dataset](https://docs.google.com/spreadsheets/d/1SmD4-xZQLOka6_0u4NG7_nTxHRjoFr0YprUiU8PbaxU/edit?usp=sharing) was curated by volunteers from 9geek, a Discord community organized by Mr. Nuttapong Ruengpanyawut (a Member of the House of Representative from the Move Forward Party). However, the dataset in its original form contains many numerical errors that threaten the validity of subsequent analyses. For this project, I cross-checked inputs in the candidate constituency with the ThaiPBS and Election Commission of Thailand (ECT) and corrected any mismatch. For a detailed list of sanity check I performed on the original dataset, please refer to [data_check.ipynb](https://github.com/peemlerd/thai-election66/data_check.ipynb).

# Reference
1. Thailand's 2023 Election result from [ThaiPBS](https://election66.thaipbs.or.th/result).
2. Official Thailand's 2023 election result from [ECT](https://official.ectreport.com/overview).
3. Pumjai Chatmaitri's [analysis of election fraud](https://smiley159.github.io/Unveiling-Electoral-Deception/?fbclid=IwAR1vIpo-T-hMOfgXGwH_BniEq0FUHQc_MaCehqZoP-zeb3byc_5CgQ-HDrE).