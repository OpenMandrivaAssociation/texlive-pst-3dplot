# revision 32843
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-3dplot
# catalog-date 2014-02-01 16:35:19 +0100
# catalog-license lppl
# catalog-version 1.99
Name:		texlive-pst-3dplot
Version:	1.99
Release:	1
Summary:	Draw 3D objects in parallel projection, using PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-3dplot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-3dplot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-3dplot.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package using PSTricks to draw a large variety of graphs and
plots, including 3D maths functions. Data can be read from
external data files, making this package a generic tool for
graphing within TeX/LaTeX, without the need for external tools.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-3dplot/pst-3dplot.pro
%{_texmfdistdir}/tex/generic/pst-3dplot/pst-3dplot.tex
%{_texmfdistdir}/tex/latex/pst-3dplot/pst-3dplot.sty
%doc %{_texmfdistdir}/doc/generic/pst-3dplot/Changes
%doc %{_texmfdistdir}/doc/generic/pst-3dplot/README
%doc %{_texmfdistdir}/doc/generic/pst-3dplot/pst-3dplot-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-3dplot/pst-3dplot-doc.dat
%doc %{_texmfdistdir}/doc/generic/pst-3dplot/pst-3dplot-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-3dplot/pst-3dplot-doc.tex
%doc %{_texmfdistdir}/doc/generic/pst-3dplot/tb72voss3d.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
