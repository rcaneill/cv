from pybtex.plugin import find_plugin
from pybtex.database import parse_file, parse_string, BibliographyData
import datetime

APA = find_plugin("pybtex.style.formatting", "apa7")()
HTML = find_plugin("pybtex.backends", "html")()


def bib_to_apa7_html(bibfile):
    with open(bibfile) as f:
        bibstr = "".join(f.readlines()).replace(
            r"\textbf{R. Caneill}", "Caneill, Romain"
        )
    bibliography = parse_string(bibstr, "bibtex")
    # We sort by date
    all_bib = {}
    all_years = {}
    for k, e in bibliography.entries.items():
        year = str(e.fields.get("year", "0000")).zfill(4)
        month = e.fields.get("month")
        if month is None:
            month = "00"
        else:
            try:
                month = str(datetime.datetime.strptime(month, "%B").month).zfill(2)
            except ValueError:
                month = str(datetime.datetime.strptime(month, "%b").month).zfill(2)
        all_bib[year + month + k] = list(
            entry.text.render(HTML)
            for entry in APA.format_bibliography(BibliographyData(entries={k: e}))
        )[0]
        all_years[year + month + k] = year
    all_keys = list(all_bib.keys())
    all_keys.sort(reverse=True)

    year = all_years[all_keys[0]]
    out = f"<h3>{year}</h3>\n<ul>"
    for k in all_keys:
        y = all_years[k]
        if y != year:
            year = y
            out += f"</ul>\n<h3>{year}</h3>\n<ul>"
        out += (
            "<li>" + all_bib[k].replace("Caneill, R.", r"<b>Caneill, R.</b>") + "</li>"
        )
    out += "</ul>"

    return out


if __name__ == "__main__":
    with open("publications.html", "w") as f:
        f.write(bib_to_apa7_html("publications.bib"))
