import pytest
from app.api.status_service import StatusService

@pytest.fixture
def status_service():
    """Fixture to initialize the StatusService instance."""
    return StatusService()

def test_status_service_success(status_service):
    """Test case for successful status request."""
    # Call the get_status method
    response = status_service.get_status()

    # Assert the response is not None and contains no errors
    assert response is not None, "The response should not be None"
    assert 'error' not in response, "The response should not contain an error"
    print("Test Passed. Status response:", response)

def test_status_service_failure(mocker, status_service):
    """Test case for failed status request, simulating API failure."""
    # Simulate a failed API response using mocker
    mocker.patch.object(status_service.api_client, 'send_request', return_value={"error": "API request failed."})
    
    # Call the get_status method
    response = status_service.get_status()

    # Assert the response contains an error
    assert response is None, "The response should be None when API fails"
    print("Test Passed. API request failed as expected.")