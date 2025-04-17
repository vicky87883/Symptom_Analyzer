import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class SymptomAnalyzer(APIView):
    def post(self, request):
        symptom_input = request.data.get("symptoms", "")
        if not symptom_input:
            return Response({"error": "Symptom input required."}, status=status.HTTP_400_BAD_REQUEST)

        prompt = f"""

Now analyze:
Symptoms: {symptom_input}
Diagnosis:"""

        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama3-70b-8192"
            )
            answer = chat_completion.choices[0].message.content
            return Response({"diagnosis": answer.strip()})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
