---

# **Revised Proposal: COMP4010-Project2-Group13 - aRt: Recreating Art With R**

## **Description**

This project explores the intersection of art and data visualization by recreating well-known artworks using R. We will use R's advanced plotting and graphics capabilities to translate selected pieces into code-generated representations. Our focus will be on styles where R's strengths — particularly in grid-based systems, vector graphics, and color manipulation — can be meaningfully applied.

## **Motivation**

This project allows us to expand our technical skills in R while exploring artistic expression. We are especially interested in how R's plotting ecosystem (e.g., `ggplot2`, `grid`, `ggforce`, `geomtextpath`, `patchwork`) can be used not only for data communication but also for creative visual storytelling.

While there are existing efforts in the R community to produce generative art or mimic certain visual aesthetics, our focus will be on **manually recreating iconic artworks**, using custom R code to explore techniques like layering, path creation, gradients, and geometric composition. Through this, we aim to deepen our understanding of programmatic art, explore different artistic styles, and potentially develop reusable patterns or helper functions to simplify recreating other pieces.

## **Scope and Technical Approach**

We will focus on the recreation of:

* **"Altarpiece – No 1"** – Group X. Hilma af Klint 1907 (geometric abstraction)
* **"Red Fuji"** by Hokusai (curves, gradients, and layering) - Located in `Red Fuji/images/Red Fuji by Hokusai.jpg`
* Potential bonus: **Minimalist reinterpretation of Van Gogh's "Starry Night"**

These works were selected because they present varying technical challenges — from geometric layout to line curves and color gradients — which align well with R's graphical capabilities.

We plan to use the following tools and techniques:

* **Packages**: `ggplot2`, `grid`, `ggforce`, `geomtextpath`, `colorspace`, `magick`
* **Techniques**: Layered plotting, coordinate manipulation, path construction, transparency/alpha blending, and text-based path drawing.

## **Deliverables**

By the end of the project, we will submit the following:

1. **Quarto Website Gallery**

   * Interactive site showcasing:

     * Original and recreated artworks side by side
     * Descriptions of each piece and commentary on the recreation process
     * Technical breakdown of R techniques and packages used
     * Reflections on challenges and creative choices

2. **R Codebase**

   * Clean, well-documented `.R` scripts for each artwork
   * Modular functions or reusable components where applicable

3. **Final Report**

   * Project overview
   * Artistic and technical reflections
   * Summary of design decisions and implementation challenges

4. **Slide Deck**

   * Concise visual summary of our project for in-class presentation

5. **Optional Package (stretch goal)**

   * A small helper package (or code template) for geometric or style-specific art recreation

* Downloadable `.R` scripts for each piece

## **Data Requirements**

We do not need traditional datasets, but we will source **reference images** of the original artworks from public domain repositories such as Wikimedia Commons or museum archives. These images are only for visual guidance and comparison — all visualizations will be manually constructed with R code.

## **Success Criteria**

We will evaluate our success based on:

* **Visual resemblance**: How closely the R recreation resembles the original artwork in layout, color, and overall feel.
* **Technical execution**: Use of clean, modular, and reusable code.
* **Creativity & interpretation**: Artistic merit and adaptation within R's constraints.
* **Documentation**: Quality of explanations and clarity of the final presentation.

## **Timeline**

| Task/Milestone                                | Start Date | End Date   | Deliverable          | Assigned Member(s) |
| --------------------------------------------- | ---------- | ---------- | -------------------- | ------------------ |
| **Week 1: Proposal**                          | 21/04/2025 | 27/04/2025 | Initial proposal     | All                |
| - Team Formation, Planning                    | 21/04      | 24/04      | Project plan         | Ekaterina, Dat     |
| - Proposal Draft & Review                     | 25/04      | 27/04      | Draft submission     | Lam, Dat           |
| **Week 2: Peer Review & Initial Development** | 27/04      | 04/05      | Peer feedback        | All                |
| - Initial Coding Setup                        | 27/04      | 28/04      | Basic plot skeletons | Ekaterina          |
| - Peer Reviews                                | 29/04      | 30/04      | Peer review          | Lam, Dat           |
| - Feedback Integration                        | 02/05      | 03/05      | Adjust plan/code     | Ekaterina, Lam     |
| **Week 3: Development & Revision**            | 05/05      | 15/05      | Revised proposal     | Dat, All           |
| - Revised Proposal                            | 05/05      | 07/05      | Detailed scope       | Dat                |
| - Core Development                            | 08/05      | 11/05      | Artwork scripts      | Ekaterina, Lam     |
| - Documentation Prep                          | 12/05      | 14/05      | Slide/report drafts  | Lam                |
| **Week 4: Finalization**                      | 16/05      | 30/05      | Final site & files   | All                |
| - Final Coding                                | 16/05      | 20/05      | Complete scripts     | Ekaterina          |
| - Complete Report & Presentation              | 21/05      | 25/05      | Slides, write-up     | Lam, Dat           |
| - Final Review & Submission                   | 26/05      | 30/05      | Website, repo, files | All                |

---


