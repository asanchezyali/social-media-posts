#!/bin/bash

# Social Media Post Validator
# Usage: ./validate.sh <path-to-tex-file> [--compile]
#   --compile: Optional flag to run LaTeX compilation (may be slow)

# Parse arguments
COMPILE=false
for arg in "$@"; do
    if [ "$arg" == "--compile" ]; then
        COMPILE=true
    fi
done

# Remove --compile from arguments
TEX_FILE="$1"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if file path provided
if [ -z "$1" ]; then
    echo -e "${RED}Error: Please provide a .tex file path${NC}"
    echo "Usage: $0 <path-to-tex-file>"
    exit 1
fi

# Check file exists
if [ ! -f "$TEX_FILE" ]; then
    echo -e "${RED}Error: File not found: $TEX_FILE${NC}"
    exit 1
fi

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Social Media Post Validator${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Extract directory and filename
DIR=$(dirname "$TEX_FILE")
BASENAME=$(basename "$TEX_FILE" .tex)

echo -e "${YELLOW}Validating: $TEX_FILE${NC}"
echo ""

# Counter for checks
PASSED=0
FAILED=0
WARNINGS=0

# Function to check pattern (using extended regex for BSD grep compatibility)
check_pattern() {
    local pattern="$1"
    local description="$2"
    local critical="${3:-no}"
    
    if grep -E -q "$pattern" "$TEX_FILE" 2>/dev/null; then
        echo -e "  ${GREEN}✓${NC} $description"
        PASSED=$((PASSED + 1))
    else
        echo -e "  ${RED}✗${NC} $description"
        FAILED=$((FAILED + 1))
        if [ "$critical" == "yes" ]; then
            echo -e "     ${RED}CRITICAL: This is required!${NC}"
        fi
    fi
}

echo -e "${BLUE}1. Document Structure Checks${NC}"
echo "-----------------------------------"

check_pattern 'documentclass' "Document class defined" "yes"
check_pattern 'begin\{document\}' "Document begins" "yes"
check_pattern 'end\{document\}' "Document ends" "yes"
check_pattern 'section\{' "At least one section exists" "yes"
check_pattern 'begin\{titlepage\}' "Title page exists" "yes"

echo ""
echo -e "${BLUE}2. Required Components${NC}"
echo "-----------------------------------"

check_pattern 'languagetag' "Language tag present" "yes"
check_pattern 'titlepagecontents' "Title page content defined" "yes"
check_pattern 'finalpagecontents' "Final page content defined" "yes"
check_pattern 'elegantqr' "QR code present" "yes"

echo ""
echo -e "${BLUE}3. Code Blocks${NC}"
echo "-----------------------------------"

check_pattern 'begin\{macterminal\}' "Mac terminal environment used"
CODE_BLOCKS=$(grep -E -c 'begin\{macterminal\}' "$TEX_FILE" 2>/dev/null || echo "0")
echo -e "  ${BLUE}ℹ${NC} Found $CODE_BLOCKS code block(s)"

if [ -d "$DIR/codes" ]; then
    CODE_FILES=$(find "$DIR/codes" -type f \( -name "*.py" -o -name "*.js" \) 2>/dev/null | wc -l | tr -d ' ')
    echo -e "  ${GREEN}✓${NC} $CODE_FILES code file(s) in codes/ directory"
    PASSED=$((PASSED + 1))
else
    echo -e "  ${YELLOW}⚠${NC} No codes/ directory found"
    WARNINGS=$((WARNINGS + 1))
fi

echo ""
echo -e "${BLUE}4. Content Sections${NC}"
echo "-----------------------------------"

check_pattern 'section\{Conclusion' "Conclusion section exists"
check_pattern 'section\{References' "References section exists"
check_pattern 'section\{Explore' "Cross-promotion section exists"

echo ""
echo -e "${BLUE}5. Formatting & Styling${NC}"
echo "-----------------------------------"

check_pattern 'usepackage.*listings' "Listings package included"
check_pattern 'definecolor' "Custom colors defined"
check_pattern 'pagecolor' "Page background color set"

echo ""
echo -e "${BLUE}6. Header/Footer${NC}"
echo "-----------------------------------"

check_pattern 'fancyhead' "Header configuration exists"
check_pattern 'fancyfoot' "Footer configuration exists"
check_pattern 'Alejandro' "Profile name present" "yes"

echo ""
echo -e "${BLUE}7. External References${NC}"
echo "-----------------------------------"

check_pattern 'href\{https://' "External links present"
LINKS=$(grep -E -o 'href=\{https://[^}]*\}' "$TEX_FILE" 2>/dev/null | wc -l | tr -d ' ')
echo -e "  ${BLUE}ℹ${NC} Found $LINKS external link(s)"

echo ""
echo -e "${BLUE}8. Code Quality Checks${NC}"
echo "-----------------------------------"

if grep -E -q 'How to Run' "$TEX_FILE" 2>/dev/null; then
    echo -e "  ${GREEN}✓${NC} Run instructions included"
    PASSED=$((PASSED + 1))
else
    echo -e "  ${YELLOW}⚠${NC} No explicit 'How to Run' instructions found"
    WARNINGS=$((WARNINGS + 1))
fi

if grep -E -q 'Output:' "$TEX_FILE" 2>/dev/null; then
    echo -e "  ${GREEN}✓${NC} Expected output shown"
    PASSED=$((PASSED + 1))
else
    echo -e "  ${YELLOW}⚠${NC} No expected output shown"
    WARNINGS=$((WARNINGS + 1))
fi

# LaTeX compilation test (optional)
echo ""
echo -e "${BLUE}9. LaTeX Compilation Test${NC}"
echo "-----------------------------------"

if [ "$COMPILE" == "true" ]; then
    echo -e "  ${BLUE}ℹ${NC} Attempting to compile..."
    if pdflatex -interaction=nonstopmode -halt-on-error "$TEX_FILE" > /dev/null 2>&1; then
        echo -e "  ${GREEN}✓${NC} LaTeX compilation successful"
        PASSED=$((PASSED + 1))
        
        PDF_NAME="$DIR/$BASENAME.pdf"
        if [ -f "$PDF_NAME" ]; then
            PDF_SIZE=$(du -h "$PDF_NAME" | cut -f1)
            echo -e "  ${GREEN}✓${NC} PDF generated ($PDF_SIZE)"
        fi
    else
        echo -e "  ${RED}✗${NC} LaTeX compilation failed"
        echo -e "     ${RED}Run 'pdflatex $TEX_FILE' for details${NC}"
        FAILED=$((FAILED + 1))
    fi
else
    echo -e "  ${BLUE}ℹ${NC} Skipping compilation (use --compile to enable)"
    echo -e "     ${YELLOW}Tip: Run manually with: pdflatex $TEX_FILE${NC}"
fi

# Summary
echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Validation Summary${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo -e "  ${GREEN}Passed:${NC}    $PASSED"
echo -e "  ${RED}Failed:${NC}    $FAILED"
echo -e "  ${YELLOW}Warnings:${NC} $WARNINGS"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✓ All critical checks passed!${NC}"
    exit 0
else
    echo -e "${RED}✗ Some checks failed. Please review and fix.${NC}"
    exit 1
fi
