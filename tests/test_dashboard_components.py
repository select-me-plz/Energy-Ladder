"""
Unit tests for dashboard components.
"""

import pytest
from dashboard.components.metrics import metric_card, status_indicator, progress_bar


class TestMetricsComponents:
    """Test suite for metrics components."""
    
    def test_status_indicator_operational(self):
        """Test status indicator for operational status."""
        result = status_indicator("operational")
        assert "operational" in result.lower()
        assert "🟢" in result
    
    def test_status_indicator_warning(self):
        """Test status indicator for warning status."""
        result = status_indicator("warning")
        assert "warning" in result.lower()
        assert "🟡" in result
    
    def test_status_indicator_error(self):
        """Test status indicator for error status."""
        result = status_indicator("error")
        assert "error" in result.lower()
        assert "🔴" in result


class TestLayoutComponents:
    """Test suite for layout components."""
    
    def test_module_imports(self):
        """Test all layout components can be imported."""
        from dashboard.components.layout import (
            create_header,
            create_section,
            create_sidebar_menu,
            create_info_box
        )
        
        assert callable(create_header)
        assert callable(create_section)
        assert callable(create_sidebar_menu)
        assert callable(create_info_box)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
