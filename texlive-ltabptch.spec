# revision 17533
# category Package
# catalog-ctan /macros/latex/contrib/ltabptch
# catalog-date 2010-03-07 16:35:25 +0100
# catalog-license lppl
# catalog-version 1.74d
Name:		texlive-ltabptch
Version:	1.74d
Release:	11
Summary:	Bug fix for longtable
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ltabptch
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltabptch.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltabptch.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A patch for LaTeX bugs tools/3180 and tools/3480. The patch
applies to version 4.11 of longtable.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ltabptch/ltabptch.sty
%doc %{_texmfdistdir}/doc/latex/ltabptch/README
%doc %{_texmfdistdir}/doc/latex/ltabptch/ltabptch.pdf
%doc %{_texmfdistdir}/doc/latex/ltabptch/ltabptch.tex
%doc %{_texmfdistdir}/doc/latex/ltabptch/ltabtest.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.74d-2
+ Revision: 753572
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.74d-1
+ Revision: 718909
- texlive-ltabptch
- texlive-ltabptch
- texlive-ltabptch
- texlive-ltabptch

