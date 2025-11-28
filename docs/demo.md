---
layout: default
title: Demo – UBPD LLM Classifier
---

# Demo – UBPD LLM Testimonial Classifier

[English](#english-version) · [Español](#spanish-version)

---

# English Version {#english-version}

This is a **front-end mockup** of the classifier user interface.  
It does not call real APIs, but simulates JSON output based on simple keyword rules.

<form id="demo-form-2">
  <label for="demo-text-2"><strong>Testimonial Text</strong></label><br>
  <textarea id="demo-text-2" name="demo-text-2" rows="8" style="width:100%;"></textarea><br><br>
  <button type="button" id="demo-run-2">Run Classifier (Mock)</button>
</form>

<pre id="demo-output-2" style="margin-top:1rem;">
{
  "document_type": null,
  "actors": [],
  "events": [],
  "territory": {},
  "priority": null
}
</pre>

<script>
  (function() {
    var btn = document.getElementById('demo-run-2');
    var txt = document.getElementById('demo-text-2');
    var out = document.getElementById('demo-output-2');
    if (!btn || !txt || !out) return;

    btn.addEventListener('click', function() {
      var text = (txt.value || "").toLowerCase();
      var result = {
        document_type: "unknown",
        actors: [],
        events: [],
        territory: {},
        priority: "medium"
      };

      if (text.includes("desapar") || text.includes("missing")) {
        result.events.push("forced_disappearance");
        result.priority = "high";
      }
      if (text.includes("farc")) {
        result.actors.push("FARC");
      }
      if (text.includes("auc")) {
        result.actors.push("AUC");
      }
      if (text.includes("meta")) {
        result.territory.region = "Meta";
      }

      out.textContent = JSON.stringify(result, null, 2);
    });
  })();
</script>

---

# Versión en Español {#spanish-version}

Esta es una **maqueta de interfaz** del clasificador.  
No llama servicios reales, sino que genera una salida JSON simulada para ilustrar el flujo de trabajo.

- Es segura para demostraciones públicas  
- No requiere claves de API  
- Puede reemplazarse en el futuro por un backend real (FastAPI, etc.)  
