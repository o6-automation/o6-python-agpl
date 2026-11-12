# Public documentation guidelines

## Scope

- Write for Python developers who use o6\Python to build OPC UA clients and
  servers. Assume they know Python and asyncio basics, but not open62541 or the
  internals of o6\Python. Link OPC UA concepts to the
  [OPC UA Fundamentals](manual/opcua-fundamentals/index.md) pages instead of
  assuming the reader already knows them.
- Cover installation, usage, public interfaces and troubleshooting. Put binding
  mechanics that users need for debugging or support decisions in
  [Implementation details](manual/implementation-details/index.md). Keep design
  notes, source walkthroughs and contributor procedures in `dev_docs/`.
- Document the supported behavior of the target version. State limitations and
  where behavior differs between client and server, sync and async use, or the
  AGPL and commercial builds. Assume the reader installs `o6` with pip; don't
  document building from source. The one exception is the minimal AGPL install
  on the Install page, which links to the AGPL repository's README for details.
- Describe the current state only. Leave out migration notes, earlier behavior
  and wording such as "previously", "no longer", "now returns" or "renamed
  from". Changes between versions belong in `RELEASE_NOTES.md`.

## Sections

Each section has its own job and source. Before you add a page, decide which
section it belongs in.

| Section | Location | Job | Edit here |
|---|---|---|---|
| Home | `docs/index.md`, `docs/home/` | Overview, pip installation, AGPL and commercial wheels | The Markdown pages |
| Tutorials | `docs/tutorials/` | One task per page. Each page builds on earlier pages and runs against the tutorial server | The Markdown pages. Listings on *Set the Stage* come from `examples/advanced_applications/tutorial_server/` |
| Manual | `docs/manual/` | Explains a topic completely: concepts, options, behavior, edge cases. Its last chapter is the release notes | The Markdown pages. The release notes page includes `RELEASE_NOTES.md`; edit that file |
| Examples | `docs/examples/` | Complete runnable scripts with a walkthrough | The scripts in `examples/` and their `# BEGIN MD`/`# BEGIN CODE` markers. The pages are generated |
| API Reference | `docs/api_reference/` | Signatures and per-symbol behavior | Docstrings in `o6/`. The pages are generated and contain no prose |

- Add every new hand-written page to `nav` in `zensical.toml`. The generator
  rewrites the `Examples` nav block, so don't edit it by hand.
- Write API docstrings in Google style (`Args:`, `Returns:`, `Raises:`). A
  docstring states the contract of one symbol. Workflows and explanations
  belong on manual or tutorial pages, which link to the reference.
- Links in API docstrings are relative to `docs/`, because the build resolves
  them from there. Use `manual/...` or `tutorials/...` for links to those
  sections; `docs/check_links.py` reports a wrong prefix.

## Structure and style

- Start a tutorial with the goal and the code the reader will run. Briefly
  explain the result and what to try next. Link to the manual for options and
  edge cases.
- Start a manual page with what the feature is for and when to use it, then
  cover the details.
- Keep pages short. Write plain technical prose: one idea per sentence, one
  topic per paragraph. State the fact or step directly. Leave out introductions,
  recaps, filler and hedging such as "simply", "basically" or "it is worth
  noting".
- Explain only what the reader needs to do the task or predict the behavior.
  Give background or rationale in one sentence or a link, not a detour.
- When a snippet, table or list says the same as a paragraph, use it instead.
- Define unfamiliar terms and use consistent names.
- Name the product o6\Python; write `o6\\Python` in the Markdown source. Use
  `o6` for the package and import name, open62541 for the C stack and OPC UA
  (with a space) for the standard. Keep command names, imports and paths
  unchanged.
- Spell OPC UA terms as the specification does (NodeId, BrowseName, ObjectType,
  companion specification). Use code formatting when you refer to the Python
  identifier, as in `o6.NodeId`.
- Give each topic one home and link to it from other pages. Don't link to
  source files.
- Format text by what it is, never for stress:
  - `code` for anything the reader types or sees in code: identifiers,
    arguments, values, NodeIds, file names, paths and commands.
  - *Italics* for a term at the place it is defined, once per page, as in
    "A *continuation point* marks where a browse stopped."
  - **Bold** only for a lead-in label at the start of a list item or
    paragraph, as in "**Scalar targets:** return one value."
  - To stress a point, rewrite the sentence so the point stands out, or use an
    admonition for a warning. Don't use bold, italics or capitals for stress.
    Write counts in words instead of variables: "one round trip instead of one
    per target", not "instead of *n*".
- Use tables for comparisons and mappings, numbered steps for procedures, and
  diagrams only when they make a flow or relationship clearer. Use admonitions
  (`!!! warning`, `!!! tip`, `!!! info`) sparingly and put them next to the step
  they apply to.
- Use fenced `mermaid` blocks for relationship, flow and sequence diagrams.
  Keep folder structures, address-space trees, structure field layouts and
  message layouts as text trees. Keep code and console output as text.
  Use descriptive labels and check the rendered diagram at the docs content
  width; split dense diagrams when their labels become too small.

## Contents and navigation links

- Use a two-column table headed `Topic | What it covers` for collections of
  navigation links. This includes overview pages, Home's "Where to Find What",
  tutorial follow-ups, and related reading, even when there is only one entry.
- Put the linked topic in the first column and a short description in the
  second. Give each destination its own row. Explain its scope without repeating
  the title; keep descriptions to one concise sentence or phrase.
- Use `## Contents` for an overview's main catalogue, `## Next steps` for
  tutorial follow-up reading, and `## Related topics` for supplementary references.
  Home can keep its `Where to Find What` heading. Use `###` headings for groups
  within Contents, with the same table format under each group.
- The Manual follows a book-like reading order. Chapter overviews guide readers
  through their Contents and the navigation footer; do not add a `Next steps`
  section that directs readers to other chapters, tutorials, or the API reference.
  Link supporting material where it is relevant in the explanation.
- Match the sidebar's labels, grouping, and order in Contents. Put additional
  reading outside that catalogue. State prerequisites and reading order in
  prose rather than adding a number column or numbering the links.
- Keep numbered lists for procedures and ordinary bullets for non-navigation
  lists. The generated API symbol directory remains a grouped list.

## Content and examples

- Explain each feature's purpose, how to use it and the expected result.
- For every public API, document parameters and their defaults, return values,
  raised exceptions, side effects and thread or event-loop requirements.
- Keep concept examples focused on the feature being explained. State assumed
  setup briefly instead of repeating imports, server construction, publication,
  and cleanup in every fragment. Do not add `try/finally` or other exception
  handling merely to make a teaching fragment production-ready.
- Examples presented as complete programs include their imports, construction,
  required namespaces, and ordinary lifetime. Explain error handling where it
  is the topic or necessary to understand the API's result.
- When an API has sync and async forms, show the form the page is about and
  link to the other.
- Use `opc.tcp://localhost:4840` as the endpoint, and realistic placeholders for
  the reader's own nodesets, NodeIds and credentials. Keep names consistent
  within a page. Label placeholders and partial snippets. Tutorial snippets must
  run against the tutorial server as shown.
- For a common failure, explain the symptom (the exception or `StatusCode`), the
  cause and the fix. Put it next to the step where the failure occurs.

## Validation

- Check claims against the code, docstrings and `dev_docs/api_manifest.md`. Run
  changed snippets when practical. When behavior changes, check related
  tutorials, manual pages, examples and nav entries.
- Before building, stage the theme once with
  `git submodule update --init deps/o6-theme` and
  `python tools/stage_docs_theme.py`.
- From the repository root, run:

  ```bash
  python docs/gen_tutorial_server.py --check
  python examples/check_examples.py      # when examples/ changed
  python docs/gen_examples.py            # when examples/ changed
  python docs/gen_api_reference.py       # when the public API inventory changed
  zensical build --clean
  python docs/gen_examples.py --copy-markdown-downloads site
  python docs/check_links.py
  ```

  Don't use `zensical build --strict`. Raw example Markdown downloads such as the
  LDS `README.md` exist only after the copy step, so strict mode reports them as
  missing pages.
